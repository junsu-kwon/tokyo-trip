# -*- coding: utf-8 -*-
# 맛집 대표 메뉴 (data/menu.json, 2026-10-19 조사). 출처가 없는 항목은 넣지 않는다.
import json, os
def apply(places):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "menu.json")
    for k, v in json.load(open(path, encoding="utf-8")).items():
        if k in places and v.get("menu") and v.get("src"):
            places[k].update(menu=v["menu"], menus=v["src"], menun=v.get("note") or "")
