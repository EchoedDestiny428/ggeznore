# APUSH Map Quiz Automated Solver 🎯

An automated bot and browser tool for solving the [US Physical Geography — Label Practice Quiz](https://apush-mapquiz.vercel.app/) with 100% accuracy.

---

## Method 1: Python Playwright Bot (`bot.py`)

### Requirements
- Python 3.x
- `playwright` (`pip install playwright` & `playwright install`)

### Usage

1. **Solve and keep browser open for manual name entry**:
   ```bash
   py bot.py
   ```
   This will:
   - Launch Chromium and open the quiz.
   - Automatically detect and map all 23 randomized geographic markers.
   - Instantly fill in all 23 answers and check them.
   - Leave the browser open at the "Put your name on the board" screen so you can type your name and post your score manually.

2. **Optional Flags**:
   - `--name "YourName"` : Pre-fills your username on the submission card.
   - `--post` : Automatically clicks "Post time" after filling.
   - `--headless` : Runs the bot invisibly in the background.

   *Example with name pre-fill:*
   ```bash
   py bot.py --name "Asriel"
   ```

---

## Method 2: Browser Console / Bookmarklet (`solver.js`)

If you are already on the site in Chrome / Firefox / Edge:

### DevTools Console
1. Press `F12` on the quiz page.
2. Click the **Console** tab.
3. Paste the contents of [`solver.js`](solver.js) and press `Enter`.

### Bookmarklet (1-Click)
Create a new browser bookmark with the following URL:
```javascript
javascript:(()=>{const F=[{n:"Pacific Ocean",x:55,y:470},{n:"Atlantic Ocean",x:1150,y:430},{n:"Gulf of Mexico",x:745,y:700},{n:"Lake Superior",x:780,y:130},{n:"Lake Michigan",x:797,y:235},{n:"Lake Huron",x:874,y:186},{n:"Lake Erie",x:917,y:258},{n:"Lake Ontario",x:985,y:210},{n:"Hudson River",x:1056,y:227},{n:"Chesapeake Bay",x:1050,y:320},{n:"Appalachian Mountains",x:918,y:420},{n:"Mississippi River",x:727,y:537},{n:"Great Plains",x:525,y:285},{n:"Missouri River",x:516,y:143},{n:"Rocky Mountains",x:396,y:368},{n:"Great Basin",x:172,y:333},{n:"Great Salt Lake",x:263,y:292},{n:"Rio Grande",x:499,y:631},{n:"Cascade Mountains",x:112,y:170},{n:"Colorado River",x:262,y:423},{n:"Sierra Nevada Mountains",x:135,y:388},{n:"Mexico",x:429,y:703},{n:"Canada",x:330,y:30}];document.querySelectorAll("#marks > g.badge").forEach((b,s)=>{const d=b.querySelector(".dot");if(!d)return;const x=+d.getAttribute("cx"),y=+d.getAttribute("cy"),m=F.find(f=>Math.abs(f.x-x)<2&&Math.abs(f.y-y)<2);if(m){const i=document.getElementById("in"+s);if(i)i.value=m.n;}});document.getElementById("check")?.click();})();
```
Click the bookmark at any time to instantly solve the quiz!
