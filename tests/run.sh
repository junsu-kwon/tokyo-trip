#!/usr/bin/env bash
# 지도 라이브러리 대신 가짜(lstub.js)를 넣은 test.html을 만들고 클릭 테스트를 돌린다.
set -e
cd "$(dirname "$0")"
sed 's#<script src="https://cdnjs[^"]*leaflet[^"]*"[^>]*></script>#<script src="lstub.js"></script>#' ../index.html > test.html
python3 aftest.py
python3 ftest.py
