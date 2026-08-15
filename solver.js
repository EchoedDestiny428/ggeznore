/**
 * APUSH Map Quiz - Instant Browser Console / Bookmarklet Solver
 * 
 * Usage in Browser:
 * 1. Open https://apush-mapquiz.vercel.app/
 * 2. Press F12 to open Developer Tools, switch to the "Console" tab.
 * 3. Paste the code below and press Enter.
 * 
 * Or save as Bookmarklet:
 * javascript:(()=>{const F=[{n:"Pacific Ocean",x:55,y:470},{n:"Atlantic Ocean",x:1150,y:430},{n:"Gulf of Mexico",x:745,y:700},{n:"Lake Superior",x:780,y:130},{n:"Lake Michigan",x:797,y:235},{n:"Lake Huron",x:874,y:186},{n:"Lake Erie",x:917,y:258},{n:"Lake Ontario",x:985,y:210},{n:"Hudson River",x:1056,y:227},{n:"Chesapeake Bay",x:1050,y:320},{n:"Appalachian Mountains",x:918,y:420},{n:"Mississippi River",x:727,y:537},{n:"Great Plains",x:525,y:285},{n:"Missouri River",x:516,y:143},{n:"Rocky Mountains",x:396,y:368},{n:"Great Basin",x:172,y:333},{n:"Great Salt Lake",x:263,y:292},{n:"Rio Grande",x:499,y:631},{n:"Cascade Mountains",x:112,y:170},{n:"Colorado River",x:262,y:423},{n:"Sierra Nevada Mountains",x:135,y:388},{n:"Mexico",x:429,y:703},{n:"Canada",x:330,y:30}];document.querySelectorAll("#marks > g.badge").forEach((b,s)=>{const d=b.querySelector(".dot");if(!d)return;const x=+d.getAttribute("cx"),y=+d.getAttribute("cy"),m=F.find(f=>Math.abs(f.x-x)<2&&Math.abs(f.y-y)<2);if(m){const i=document.getElementById("in"+s);if(i)i.value=m.n;}});document.getElementById("check")?.click();})();
 */

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
        console.error("No map badges found.");
        return;
    }

    let count = 0;
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
                count++;
            }
        }
    });

    const checkBtn = document.getElementById('check');
    if (checkBtn) {
        checkBtn.click();
    }

    console.log(`%c[APUSH Solver] Successfully solved ${count}/23 features!`, "color: #3fb950; font-weight: bold; font-size: 14px;");
})();
