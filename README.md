# 도쿄 여행 일정 (2026.10.21–10.24)

휴대폰에서 보는 여행 일정 페이지. 결과물은 `index.html` 한 파일이고, GitHub Pages로 배포한다.

## 구조

```
index.html          ← 빌드 결과 (이 파일만 배포하면 됨)
src/
  build.py          ← 모든 데이터를 합쳐 index.html을 만든다
  app_template.html ← 화면(HTML·CSS·JS). __COORDS__, __DATA__ 자리에 데이터가 들어간다
  coords.json       ← 장소 좌표
  existing_reviews.py ← 원본 장소들의 구글·타베로그 리뷰 요약, 주의사항(warn)
  rec_data.py / rec_data2.py / rec_data3.py ← "추천" 장소 (1차, 2차, 초밥)
  attrs.py          ← 요일별 영업시간(OH), 결제(PAY), 면세(TAX), 비 오는 날(RAIN)
  ohparse.py        ← 영업시간 문자열 → 요일별 시간 자동 변환
  price.py          ← 타베로그 1인 예산 → 2인 가격대
  menu.py           ← data/menu.json의 대표 메뉴를 장소에 붙인다
  tips.py           ← data/tips.json의 최신 리뷰 팁을 장소에 붙인다
data/               ← 조사 결과 원본 (JSON)
  res_*.json, res2_*.json   ← Retty·핫페퍼·Trip.com·한국어 후기, 신규 추천 타베로그
  payres_*.json             ← 결제·면세·우천 조사
  budgetres_*.json          ← 타베로그 예산
  menu.json                 ← 맛집 대표 메뉴 (menu · src 출처 · note), 출처 없는 곳은 null
  tips.json                 ← 장소 키별 최신 리뷰 팁 (kind · tip · src · site · date · quote 원문 인용), 상세 창 "최신 리뷰 팁" 버튼
                              2026-10-20 구글 최신순 리뷰·네이버 블로그(2025-07 이후) 수집 → 원문 인용 대조 독립 검증을 통과한 것만
tests/              ← Playwright 클릭 테스트 (지도는 lstub.js 가짜로 대체)
```

## 빌드

```bash
cd src && python3 build.py        # → ../index.html
```

Windows에서는 `PYTHONUTF8=1`을 붙여야 한다 (기본 인코딩이 cp949라 JSON을 못 읽음).

## 자주 하는 수정

- **일정 바꾸기**: `src/build.py`의 `days = [...]` 안 `S("시간", "제목", "장소키", "메모", ...)` 줄을 고친다.
  - 식사·장소 후보 칸은 `meal=dict(area=..., orig=[원본 장소들], groups=[dict(label=..., keys=[...])])`
  - 장소 묶음은 `kind="place"`, 추천 동선은 `route=[...]`, 이유는 `rnote="..."`
- **장소 추가**: `src/build.py`의 `P("키", "이름", "food|cafe|shop|sight", "지역", "지역이름", jp="주소", jpname="일본어 이름", hours="...")`
  - 추천 장소는 `rec_data*.py`에 `pid`(구글 place id), `ll`(좌표), `g`(구글 평점)와 함께 추가
- **영업시간이 자동 해석과 다르면**: `src/attrs.py`의 `OH`에 요일별로 직접 적는다 (월~일 순서, `[]`=휴무)
- **결제·면세 태그**: `attrs.py`의 `PAY`(cash/card/cashless/mixed/free/nocard), `TAX`(yes/no/mixed)
- **대표 메뉴**: `data/menu.json`에 `"키": {"menu": ..., "src": 출처 URL, "note": ...}` (출처 없으면 안 보임)
- **바뀐 점 기록**: `build.py`의 `changes = [...]` (준비 탭 "원본 일정과 달라진 점")

## 원칙 (지금까지 지켜 온 것)

- 데이터는 확인한 출처만 넣는다. 출처끼리 다르면 둘 다 적는다 (`warn`, `ohn`).
- 원본 메모에 있던 곳은 "원본에 있던 곳"으로 맨 위, 리뷰 기반 추천은 `추천` 태그로 구분한다.
- 원본에 없던 곳을 일정에 끼워 넣지 않는다 (근처·추천 칸에만).
- 영업 상태·필터 기준 시각은 일본 시간(UTC+9).

## 지도

Leaflet(cdnjs) + 타일 서버. 웹 주소(GitHub Pages, 미리보기)로 열면 오픈스트리트맵,
파일을 직접 열면(file://) 오픈스트리트맵이 403을 내므로 CARTO를 먼저 쓴다. 실패하면 다음 서버로 넘어간다.

## 날씨

일본 기상청(JMA) 데이터를 페이지가 열릴 때 브라우저에서 직접 불러온다(10분마다 갱신, 실패하면 숨김).
지금 기온은 아메다스 도쿄 관측소(44132), 날짜별 날씨는 도쿄 지방(130010) 단기·주간 예보.
일정 칸에는 그날 지역의 지금 기온(23구는 도쿄 관측소 하나뿐, 나리타는 成田 45121)과 카메탄(cametan.com) 시·구별 라이브카메라 링크가 붙는다. 지역 → 코드는 `app_template.html`의 `AREA`.

## 테스트

```bash
pip install playwright && python3 -m playwright install chromium
tests/run.sh
```
