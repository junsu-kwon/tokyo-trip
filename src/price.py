# -*- coding: utf-8 -*-
# 타베로그 1인 예산(口コミ集計) → 2인 기준 가격대
import json, os, glob, re
def _rng(s):
    if not s: return None
    nums = [int(x.replace(",", "")) for x in re.findall(r'[\d,]+', s)]
    if not nums: return None
    if re.match(r'\s*[～~]', s): return (0, nums[0])          # ～¥999
    if re.search(r'[～~]\s*$', s): return (nums[0], None)      # ¥30,000～
    return (nums[0], nums[1] if len(nums) > 1 else nums[0])
def _fmt(n):
    if n >= 10000:
        v = n / 10000
        return (f"{v:.1f}".rstrip("0").rstrip(".")) + "만"
    return f"{round(n/1000)*1000:,}" if n >= 1000 else f"{round(n/100)*100:,}"
def two(s):
    r = _rng(s)
    if not r: return ""
    lo, hi = r
    lo2 = lo * 2; hi2 = (hi + 1) * 2 if hi else None
    if lo2 == 0: return f"{_fmt(hi2)}엔 이하"
    if hi2 is None: return f"{_fmt(lo2)}엔 이상"
    return f"{_fmt(lo2)}~{_fmt(hi2)}엔"
MANUAL = {  # 타베로그 페이지가 없는 곳
 "hanamaru": dict(l="2,000~3,000엔", d="2,000~3,000엔", src="구글 후기 (소고기 우동 780엔 + 튀김 1~2개 기준)"),
 "yokocho": dict(d="가게마다 달라요", src=""),
 "nonbei": dict(d="가게마다 달라요 · 자릿세 1인 500~1,000엔 별도", src=""),
}
def load():
    base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
    out = {}
    for f in glob.glob(os.path.join(base, "budgetres_*.json")):
        for o in json.load(open(f)):
            l = two(o.get("lunch") or o.get("shop_lunch")); d = two(o.get("dinner") or o.get("shop_dinner"))
            ch = o.get("charge") or ""
            for a, b in [("サービス料", "서비스료"), ("チャージ", "자릿세"), ("お通し", "기본 안주(오토시)"), ("なし", "없음"), ("無し", "없음"), ("円", "엔"), ("夜のみ", "저녁만"), ("ディナー", "저녁"), ("ランチ", "점심"), ("あり", "있음")]:
                ch = ch.replace(a, b)
            if re.fullmatch(r"\s*(없음|-|－)?\s*", ch): ch = ""
            out[o["key"]] = dict(l=l, d=d, ch=ch, src="타베로그 이용자 예산 ×2")
    CH = {"r_hibiki": "저녁엔 자릿세 1인 1,000엔", "r_matsue": "저녁엔 서비스료 10%", "n_itamae": "술 주문 시 기본 안주 1인 550엔"}
    for k, c in CH.items():
        if k in out: out[k]["ch"] = c
    for k in ("n_maimon", "renoir_ginza"):  # 점심·저녁 구분이 안 된 값
        if k in out and out[k].get("d") and not out[k].get("l"): out[k]["l"] = out[k]["d"]
    for k, v in out.items():
        if v.get("ch") and re.search(r"없음|無し|なし", v["ch"]) and not re.search(r"\d", v["ch"]): v["ch"] = ""
    out.update(MANUAL)
    return out
def apply(places):
    data = load()
    for k, v in data.items():
        if k in places and (v.get("l") or v.get("d")): places[k]["p2"] = v
if __name__ == "__main__":
    for s in ["¥1,000～¥1,999", "～¥999", "¥10,000～¥14,999", "¥30,000～", "¥3,000～¥3,999"]: print(s, "→", two(s))
