# -*- coding: utf-8 -*-
# 영업시간(구조화) · 결제 · 면세 · 우천 정보. 2026-10-19 확인 자료 기준.
import json, os, glob, re
from ohparse import parse
H = lambda a, b: [[int(a[:2])*60+int(a[3:]), (int(b[:2])*60+int(b[3:])) + (1440 if b < a else 0)]]
ALL = lambda r: [r]*7
D24 = [[0, 1440]]
def wk(mon, tue, wed, thu, fri, sat, sun): return [mon, tue, wed, thu, fri, sat, sun]
OH = {  # 월..일. []=휴무, None=정보 없음
 "hachiko": ALL(D24), "odaiba_beach": ALL(D24), "otome": None, "nonbei": None,
 "kamotonegi": ALL(D24),
 "nmwa": wk([], H("09:30","17:30")[0:1], H("09:30","17:30"), H("09:30","17:30"), H("09:30","20:00"), H("09:30","20:00"), H("09:30","17:30")),
 "tnm": wk([], H("09:30","17:00"), H("09:30","17:00"), H("09:30","17:00"), H("09:30","20:00"), H("09:30","20:00"), H("09:30","17:00")),
 "zoo": wk([], H("09:30","17:00"), H("09:30","17:00"), H("09:30","17:00"), H("09:30","17:00"), H("09:30","17:00"), H("09:30","17:00")),
 "sunshine_alpa": ALL(H("10:00","20:00")), "tenbo": ALL(H("11:00","21:00")),
 "divercity": wk(H("11:00","20:00"), H("11:00","20:00"), H("11:00","20:00"), H("11:00","20:00"), H("11:00","20:00"), H("10:00","21:00"), H("10:00","21:00")),
 "hellokitty": wk(H("11:00","20:00"), H("11:00","20:00"), H("11:00","20:00"), H("11:00","20:00"), H("11:00","20:00"), H("10:00","21:00"), H("10:00","21:00")),
 "hokkaibanya": wk(H("09:00","15:00"), H("09:00","15:00")+H("17:00","21:00"), H("09:00","15:00"), H("09:00","15:00")+H("17:00","21:00"), H("09:00","15:00")+H("17:00","21:00"), H("09:00","15:00")+H("17:00","21:00"), H("09:00","15:00")),
 "itoya": wk(*([H("10:00","20:00")]*6), H("10:00","19:00")),
 "butter": ALL(H("10:00","21:00")), "radiokaikan": ALL(H("10:00","20:00")),
 "surugaya_plamo": wk(*([H("11:00","21:00")]*5), H("10:00","21:00"), H("10:00","21:00")),
 "iwai": wk(*([H("11:30","14:30")+H("17:30","20:30")]*5), H("11:30","14:30"), []),
 "parco": ALL(H("11:00","21:00")),
 "kuuya": ALL(H("11:00","04:00")),
 "r_tsujita": wk(*([H("11:00","22:00")]*5), H("11:00","21:30"), H("11:00","21:30")),
 "r_uogashi": wk(*([H("11:00","23:00")]*5), H("11:00","22:00"), H("11:00","21:30")),
 "n_shiseido": wk([], *([H("11:00","21:00")]*5), H("11:00","20:00")),
 "n_tokichi": ALL(H("10:30","19:30")), "n_ichinisan": ALL(H("11:00","21:30")),
 "n_happypancake": wk(*([H("11:00","20:00")]*5), H("10:00","20:30"), H("10:00","20:30")),
 "n_kitte": wk(*([H("11:00","23:00")]*5), H("11:00","22:00"), H("11:00","22:00")),
 "yokocho": wk(*([H("11:00","05:00")]*6), H("11:00","23:00")),
 "zojoji": ALL(H("09:00","17:00")), "shiba_park": ALL(D24), "fudanotsuji": ALL(D24), "shinobazu": ALL(D24),
}
OFF = {"hokkaibanya": ["2026-10-21"], "hikiniku": ["2026-10-07", "2026-10-21"]}
OHNOTE = {"kamotonegi": "출처마다 영업시간이 달라서 24시간 기준으로 표시했어요.", "hikiniku": "타베로그 기준 첫째·셋째 수요일만 쉬어요 (구글은 매주 수요일).",
          "hokkaibanya": "개점 시각은 타베로그 09:00 기준 (구글 08:30).", "n_ichinisan": "구글 21:30 기준 (타베로그 22:00).", "n_tokichi": "구글 19:30 기준 (타베로그 20:30)."}
# 결제: cash=현금만 / card=카드 가능 / cashless=현금 불가 / mixed=가게마다
PAY = {
 "unatoto": "card", "kamotonegi": "cash", "jiro": "cash", "kohitei": "cash", "renoir_ikebukuro": "card", "caretta": "card",
 "hanayama": "card", "hokkaibanya": "card", "renoir_ginza": "card", "butter": "card", "iwai": "cash", "tsutaya": "card",
 "qpot": "card", "yurinan": "card", "maasan": "card", "hikiniku": "cashless", "kuuya": "card", "shirube": "card",
 "yokocho": "mixed", "nonbei": "cash", "r_gyukatsu": "card", "r_ichiban": "cash", "r_mutekiya": "cash", "r_hibiki": "card",
 "r_tsujita": "card", "r_matsue": "card", "r_uogashi": "card", "n_ichinisan": "card", "n_marugo": "cash", "n_ikkoku": "cash",
 "n_lapin": "card", "n_shiseido": "card", "n_tokichi": "card", "n_happypancake": "card",
}
PAYD = {"nonbei": "가게 대부분 현금만", "hikiniku": "현금 불가 (카드·간편결제만)", "yokocho": "가게마다 달라요"}
TAX = {}; TAXD = {}; RAIN = {}
_base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
for f in sorted(glob.glob(os.path.join(_base, "payres_*.json"))):
    for o in json.load(open(f)):
        k = o["key"]; pv = (o.get("pay") or "").lower()
        if pv in ("cash_only", "cash"): PAY[k] = "cash"
        elif pv == "card": PAY[k] = "card"
        elif pv == "mixed": PAY[k] = "mixed"
        elif pv == "free": PAY[k] = "free"
        if o.get("pay_detail"): PAYD.setdefault(k, o["pay_detail"])
        tv = (o.get("taxfree") or "").lower()
        if tv in ("yes", "no", "mixed"): TAX[k] = tv
        if o.get("tax_detail"): TAXD[k] = o["tax_detail"]
        if o.get("rain"): RAIN[k] = o["rain"]

def apply(places):
    for k, v in places.items():
        if v["cat"] in ("station", "hotel"): continue
        oh = OH[k] if k in OH else parse(v.get("hours", ""), v.get("closed", ""))
        if oh is not None: v["oh"] = oh
        if k in OFF: v["off"] = OFF[k]
        if k in OHNOTE: v["ohn"] = OHNOTE[k]
        if k in PAY: v["payk"] = PAY[k]
        elif v.get("pay"):
            pt = v["pay"]
            if re.search(r"현금만|カード不可.*QR不可|카드 불가.*QR 불가", pt): v["payk"] = "cash"
            elif re.search(r"카드 가능|カード可|카드 ?가능|カード：可", pt): v["payk"] = "card"
        if k in PAYD: v["payd"] = PAYD[k]
        if v["cat"] in ("food", "cafe"): v["tax"] = "na"
        elif k in TAX: v["tax"] = TAX[k]
        if k in TAXD: v["taxd"] = TAXD[k]
        if k in RAIN: v["rain"] = RAIN[k]
        # 기존 '현금' 태그는 결제 태그로 대체
        if v.get("tags"): v["tags"] = [t for t in v["tags"] if t != "현금"]

# 구글 후기 근거 보정 (공식 페이지엔 언급 없음)
TAX["trader"] = "no"; TAXD["trader"] = "구글 후기 여러 건: 면세 안 돼요 (공식 페이지엔 언급 없음)"
TAX["surugaya_plamo"] = "yes"; TAXD["surugaya_plamo"] = "구글 후기 기준 · 계산 전에 직접 요청해야 해요"
PAYD["n_gachapon"] = "기계는 동전만 · 지폐 교환기는 천 엔권만"
PAYD["yodobashi"] = PAYD.get("yodobashi", "") ; TAXD["yodobashi"] = "여권 지참 시 면세 (한 출처는 불가로 적혀 있어 계산대에서 확인)"

# 초밥 추천 (구글 요일별 영업시간 기준, 월·화·일은 확인 못 해 수·토와 같게 둠)
OH.update({
 "n_fujiyama": wk(H("16:00","23:00"), H("16:00","23:00"), H("16:00","23:00"), H("11:30","14:00")+H("15:00","23:00"), H("11:30","14:00")+H("15:00","23:00"), H("15:00","23:00"), H("15:00","23:00")),
 "n_midori": wk(*([H("11:00","14:00")+H("17:00","20:30")]*5), H("11:00","20:30"), H("11:00","20:30")),
 "n_ginzo": wk(*([H("11:30","23:00")]*5), H("11:30","22:30"), H("11:30","22:30")),
 "n_utami": wk(*([H("11:30","14:00")+H("17:30","22:00")]*5), [], []),
 "n_houkou": wk(*([H("17:30","22:00")]*6), H("17:30","22:00")),
 "n_tenka": ALL(H("11:00","21:30")), "n_maimon": ALL(H("11:00","22:00")), "n_magurobito": ALL(H("11:30","22:00")),
 "n_itamae": ALL(H("11:30","04:00")),
})
OHNOTE.update({k: "구글 영업시간 기준 (월·화·일은 확인 못 했어요)" for k in ("n_fujiyama", "n_houkou")})

PAY["n_fujiyama"] = "nocard"; PAYD["n_fujiyama"] = "카드 불가 · 교통IC·QR·현금"
PAY["n_houkou"] = "card"
# 초밥 추천 결제·예약 (타베로그 2026-10-19)
PAYTEXT = {
 "n_maimon": "카드·교통IC·QR 가능 · 예약 불가 (전화로 될 때도 있음)",
 "n_magurobito": "카드·교통IC·QR 가능 · 예약 불가",
 "n_tenka": "카드·전자머니·QR 가능 · 예약 불가",
 "n_houkou": "카드·QR(PayPay) 가능, 전자머니 불가 · 완전 예약제",
 "n_itamae": "카드·교통IC 가능 · 예약 가능",
 "n_midori": "카드·교통IC·QR 가능 · 예약 가능",
 "n_fujiyama": "카드 불가 · 교통IC·QR 가능 · 예약 가능",
 "n_ginzo": "카드·교통IC·QR 가능 · 예약 가능",
 "n_utami": "카드 가능(AMEX 표기), 전자머니·QR 불가 · 예약 가능",
}
for _k in PAYTEXT:
    if _k not in PAY: PAY[_k] = "card"
_apply_orig = apply
def apply(places):
    for k, txt in PAYTEXT.items():
        if k in places: places[k]["pay"] = txt
    _apply_orig(places)
