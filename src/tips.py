# -*- coding: utf-8 -*-
# 장소별 최신 리뷰 팁 (data/tips.json, 2026-10-20 조사: 네이버 블로그·구글·타베로그·공식 등). 상세 창 "최신 리뷰 팁"에 나온다.
import json, os
def apply(places):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "tips.json")
    for k, ts in json.load(open(path, encoding="utf-8")).items():
        if k in places:
            places[k]["tips"] = ts
