#!/usr/bin/env python3
"""
APUSH Map Quiz Automated Solver Bot
Target: https://apush-mapquiz.vercel.app/
"""

import sys
import time
import argparse

if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
from playwright.sync_api import sync_playwright

QUIZ_URL = "https://apush-mapquiz.vercel.app/"

SOLVER_JS = """
(() => {
    const FEATS = [
        {"name": "Pacific Ocean", "x": 55, "y": 470},
        {"name": "Atlantic Ocean", "x": 1150, "y": 430},
        {"name": "Gulf of Mexico", "x": 745, "y": 700},
        {"name": "Lake Superior", "x": 780, "y": 130},
        {"name": "Lake Michigan", "x": 797, "y": 235},
        {"name": "Lake Huron", "x": 874, "y": 186},
        {"name": "Lake Erie", "x": 917, "y": 258},
        {"name": "Lake Ontario", "x": 985, "y": 210},
        {"name": "Hudson River", "x": 1056, "y": 227},
        {"name": "Chesapeake Bay", "x": 1050, "y": 320},
        {"name": "Appalachian Mountains", "x": 918, "y": 420},
        {"name": "Mississippi River", "x": 727, "y": 537},
        {"name": "Great Plains", "x": 525, "y": 285},
        {"name": "Missouri River", "x": 516, "y": 143},
        {"name": "Rocky Mountains", "x": 396, "y": 368},
        {"name": "Great Basin", "x": 172, "y": 333},
        {"name": "Great Salt Lake", "x": 263, "y": 292},
        {"name": "Rio Grande", "x": 499, "y": 631},
        {"name": "Cascade Mountains", "x": 112, "y": 170},
        {"name": "Colorado River", "x": 262, "y": 423},
        {"name": "Sierra Nevada Mountains", "x": 135, "y": 388},
        {"name": "Mexico", "x": 429, "y": 703},
        {"name": "Canada", "x": 330, "y": 30}
    ];

    const badges = document.querySelectorAll('#marks > g.badge');
    if (!badges || badges.length === 0) {
        return { success: false, error: "No badges found on map." };
    }

    const answers = [];
    badges.forEach((badge, slot) => {
        const dot = badge.querySelector('.dot');
        if (!dot) return;
        const cx = parseFloat(dot.getAttribute('cx'));
        const cy = parseFloat(dot.getAttribute('cy'));
        const match = FEATS.find(f => Math.abs(f.x - cx) < 2 && Math.abs(f.y - cy) < 2);
        if (match) {
            const input = document.getElementById('in' + slot);
            if (input) {
                input.value = match.name;
                answers.push({ slot, name: match.name });
            }
        }
    });

    const checkBtn = document.getElementById('check');
    if (checkBtn) {
        checkBtn.click();
    }

    const scoreEl = document.getElementById('score');
    const scoreText = scoreEl ? scoreEl.innerText : '';

    return {
        success: true,
        filledCount: answers.length,
        score: scoreText,
        answers: answers
    };
})()
"""

def solve_quiz(url=QUIZ_URL, headless=False, name=None, auto_post=False):
    print("=" * 60)
    print("🚀 Launching APUSH Map Quiz Solver...")
    print(f"🔗 Target: {url}")
    print("=" * 60)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless,
            args=["--start-maximized", "--no-default-browser-check"]
        )
        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        print("⏳ Loading map quiz...")
        page.goto(url, wait_until="networkidle")

        # Wait for map marks to be created
        page.wait_for_selector("#marks > g.badge")
        print("🎯 Map markers detected. Solving quiz...")

        result = page.evaluate(SOLVER_JS)

        if not result.get("success"):
            print(f"❌ Error: {result.get('error')}")
            browser.close()
            return

        print(f"✅ Successfully filled {result['filledCount']}/23 answers!")
        print(f"🏆 {result['score']}")

        # Handle name entry if specified
        if name:
            page.wait_for_selector("#fName")
            page.fill("#fName", name)
            print(f"📝 Entered username: {name}")

            if auto_post:
                page.click("#fPost")
                print("📤 Posted score to leaderboard!")
                time.sleep(2)

        if not headless:
            print("\n✨ Browser is open! You can enter your name on the page to post your score.")
            print("👉 Press Ctrl+C in this terminal when you are finished to close the browser.\n")
            try:
                # Keep open until user closes the window or presses Ctrl+C
                while len(context.pages) > 0 and not page.is_closed():
                    time.sleep(0.5)
            except KeyboardInterrupt:
                print("\n👋 Closing browser. Goodbye!")
            except Exception:
                pass
        
        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="APUSH Map Quiz Auto-Solver")
    parser.add_argument("--url", default=QUIZ_URL, help="Target quiz URL")
    parser.add_argument("--headless", action="store_true", help="Run in background headless mode")
    parser.add_argument("--name", default=None, help="Optional username to enter into the finish form")
    parser.add_argument("--post", action="store_true", help="Automatically submit name to the leaderboard")
    args = parser.parse_args()

    solve_quiz(url=args.url, headless=args.headless, name=args.name, auto_post=args.post)
