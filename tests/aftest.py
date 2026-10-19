import pathlib
from playwright.sync_api import sync_playwright
d=pathlib.Path(".").resolve()
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":390,"height":844}, device_scale_factor=2)
    errs=[]; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.route("**/*", lambda r: r.continue_() if r.request.url.startswith("file:") else r.abort())
    pg.goto("file://"+str(d/"test.html")); pg.wait_for_timeout(400)
    # set time 10/22 19:30 via plan bar
    bar="#planaf "
    pg.click(bar+'.chip[data-af="pick"]'); pg.wait_for_timeout(100)
    pg.fill(bar+'.aftime input', "19:30"); pg.click(bar+'[data-afd="2026-10-22"]'); pg.wait_for_timeout(200)
    print("when:", pg.inner_text(bar+'.chip[data-af="pick"]'))
    pg.click('#daypick button[data-d="d2"]'); pg.wait_for_timeout(200)
    for e in pg.query_selector_all("#dayview button.stop"):
        tx=e.inner_text().replace("\n"," | ")
        if "후보" in tx: print("STEP:", tx[:150])
    pg.screenshot(path=str(d/"af_plan.png"))
    ak=[e for e in pg.query_selector_all("#dayview button.stop") if "둘러볼" in e.inner_text() and "아키하바라" in e.inner_text()][0]
    ak.click(); pg.wait_for_timeout(400); pg.screenshot(path=str(d/"af_sheet.png"))
    pg.click('#sheet .chip[data-af="open"]'); pg.wait_for_timeout(200)
    vis=[c.get_attribute("data-k") for c in pg.query_selector_all("#sheet .card") if "af-hide" not in (c.get_attribute("class") or "")]
    print("open at 19:30 akiba:", vis)
    pg.screenshot(path=str(d/"af_sheet_open.png"))
    pg.click('#sheet .chip[data-af="open"]'); pg.evaluate("document.querySelector('#sheet .x').click()")
    pg.click(".tab[data-v=food]"); pg.wait_for_timeout(200)
    pg.click('#v-food .chip[data-af="cash"]'); pg.wait_for_timeout(200)
    vis=[c.get_attribute("data-k") for c in pg.query_selector_all("#v-food .card") if c.is_visible()]
    print("cash only:", vis)
    pg.screenshot(path=str(d/"af_food_cash.png"))
    pg.click('#v-food .chip[data-af="cash"]'); pg.click(".tab[data-v=place]"); pg.wait_for_timeout(200)
    pg.click('#v-place .chip[data-af="tax"]'); pg.wait_for_timeout(200)
    print("tax:", [c.get_attribute("data-k") for c in pg.query_selector_all("#v-place .card") if c.is_visible()])
    pg.screenshot(path=str(d/"af_place_tax.png"))
    print("errors", errs); b.close()
