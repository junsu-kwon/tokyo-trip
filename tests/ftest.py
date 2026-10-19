import pathlib, json
from playwright.sync_api import sync_playwright
d=pathlib.Path(".").resolve()
issues=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    for W in (360,390,430):
        ctx=b.new_context(viewport={"width":W,"height":800}, device_scale_factor=2)
        pg=ctx.new_page(); errs=[]
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: errs.append("console:"+m.text) if m.type=="error" else None)
        pg.route("**/*", lambda r: r.continue_() if r.request.url.startswith("file:") else r.abort())
        pg.goto("file://"+str(d/"test.html")); pg.wait_for_timeout(400)
        def overflow(tag):
            ow=pg.evaluate("Math.max(document.documentElement.scrollWidth, document.body.scrollWidth) - window.innerWidth")
            if ow>1: issues.append(f"{W}px {tag}: horizontal overflow {ow}px")
            wide=pg.evaluate("""[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0 && r.right>window.innerWidth+1 && getComputedStyle(e).position!=='fixed' && !e.closest('.chips,.daypick,#daypick,#mapfilters,.leaflet-container,.tabs-scroll,.fchips')}).slice(0,5).map(e=>e.tagName+'.'+e.className+' '+Math.round(e.getBoundingClientRect().right))""")
            if wide: issues.append(f"{W}px {tag}: elements past edge {wide}")
        n_steps=0; n_cards=0
        for day in ["d1","d2","d3","d4"]:
            pg.click(f'#daypick button[data-d="{day}"]'); pg.wait_for_timeout(150); overflow("plan "+day)
            cnt=len(pg.query_selector_all("#dayview button.stop"))
            for i in range(cnt):
                bt=pg.query_selector_all("#dayview button.stop")[i]
                bt.evaluate("e=>e.click()"); pg.wait_for_timeout(120)
                if not pg.query_selector("#sheet.show"): issues.append(f"{day} step {i} no sheet")
                # click every card inside meal sheet
                cards=pg.query_selector_all("#sheet .card, #sheet .rroute button")
                for j in range(len(cards)):
                    c=pg.query_selector_all("#sheet .card, #sheet .rroute button")[j]
                    c.evaluate("e=>e.click()"); pg.wait_for_timeout(60)
                    if not pg.query_selector("#sheet .sh-back"): issues.append(f"{day} step {i} card {j} no back")
                    else: pg.evaluate("document.querySelector('#sheet .sh-back').click()"); pg.wait_for_timeout(60)
                    n_cards+=1
                if W==390: overflow(f"sheet {day}#{i}")
                pg.evaluate("document.querySelector('#sheet .x').click()"); pg.wait_for_timeout(80)
                n_steps+=1
        for tab in ["map","food","place","prep"]:
            pg.click(f".tab[data-v={tab}]"); pg.wait_for_timeout(200); overflow("tab "+tab)
            if tab in("food","place"):
                cs=pg.query_selector_all(f"#v-{tab} .card")
                for c in cs:
                    c.evaluate("e=>e.click()"); pg.wait_for_timeout(40)
                    if not pg.query_selector("#sheet.show"): issues.append(f"{tab} card {c.get_attribute('data-k')} no sheet")
                    pg.evaluate("document.querySelector('#sheet .x').click()"); pg.wait_for_timeout(30)
                if W==390: print(tab,"cards",len(cs))
            if tab=="map":
                n=len(pg.query_selector_all("#mapfilters .chip"))
                for i in range(n): pg.query_selector_all("#mapfilters .chip")[i].click(); pg.wait_for_timeout(50)
        # checklist persistence
        pg.click(".tab[data-v=prep]"); 
        box=pg.query_selector("#check input"); before=box.is_checked(); box.click()
        pg.reload(); pg.wait_for_timeout(400); pg.click(".tab[data-v=prep]")
        after=pg.query_selector("#check input").is_checked()
        if after==before: issues.append(f"{W}px checklist not persisted")
        if W==390: print("steps",n_steps,"inner cards",n_cards)
        if errs: issues.append(f"{W}px errors: {errs[:5]}")
        ctx.close()
    # dark mode screenshot
    ctx=b.new_context(viewport={"width":390,"height":844}, device_scale_factor=2, color_scheme="dark"); pg=ctx.new_page()
    pg.route("**/*", lambda r: r.continue_() if r.request.url.startswith("file:") else r.abort())
    pg.goto("file://"+str(d/"test.html")); pg.wait_for_timeout(400); pg.screenshot(path=str(d/"dark_plan.png"))
    pg.click('#daypick button[data-d="d2"]'); pg.wait_for_timeout(200)
    [e for e in pg.query_selector_all("button.stop") if "둘러볼" in e.inner_text()][1].click(); pg.wait_for_timeout(400); pg.screenshot(path=str(d/"dark_sheet.png"))
    pg.evaluate("document.querySelector('#sheet .x').click()"); pg.click(".tab[data-v=food]"); pg.wait_for_timeout(300); pg.screenshot(path=str(d/"dark_food.png"))
    ctx.close(); b.close()
print("ISSUES:", len(issues)); print("\n".join(issues[:40]))
