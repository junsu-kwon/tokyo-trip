# -*- coding: utf-8 -*-
import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
COORDS = json.load(open(os.path.join(HERE, "coords.json"), encoding="utf-8"))

places = {}
def P(key, name, cat, area, areaName, jp="", q="", hours="", closed="", pay="", note="", tags=None, site="", tel="", brief="", tip=False, **kw):
    d = dict(key=key, name=name, cat=cat, area=area, areaName=areaName, jp=jp, addr=jp, q=q or (jp and (name_jp(kw) or "") + " " + jp) or name,
             hours=hours, closed=closed, pay=pay, note=note, tags=tags or [], site=site, tel=tel, brief=brief, tip=tip)
    d.update({k: v for k, v in kw.items() if k not in ("jpname",)})
    if kw.get("jpname"):
        d["q"] = kw["jpname"] + " " + jp if jp else kw["jpname"]
    places[key] = d
    return key
def name_jp(kw): return kw.get("jpname")

# ----- stations / hubs -----
P("narita", "나리타 공항 (2·3터미널)", "station", "air", "나리타", jpname="成田空港 第3ターミナル", dirq="成田空港 第3ターミナル", nomini=True,
  note="3터미널 ↔ 2터미널(공항 제2빌딩역): 무료 연결버스 약 5분, 또는 연결통로 도보 약 15분(500m)")
P("airport2_st", "공항 제2빌딩역 (스카이라이너 타는 곳)", "station", "air", "나리타", jpname="空港第2ビル駅", dirq="空港第2ビル駅", nomini=True,
  note="2터미널 지하 1층의 게이세이선 역이에요. 3터미널에서 오면 무료 연결버스로 2터미널에 내려서 내려가요. 스카이라이너 예약 QR은 여기 매표소·발권기에서 실물 티켓으로 바꿔요.", site="https://www.keisei.co.jp/keisei/tetudou/skyliner/jp/traffic/skyliner_timetable.php")
P("keisei_ueno", "게이세이우에노역", "station", "ueno", "우에노", jp="東京都台東区上野公園1-60", jpname="京成上野駅",
  note="스카이라이너 발착역. 숙소까지 약 340m", site="https://www.keisei.co.jp/keisei/tetudou/skyliner/jp/traffic/skyliner_timetable.php")
P("hotel", "APA 호텔 우에노 에키마에", "hotel", "ueno", "숙소", jp="東京都台東区東上野2-18-7", jpname="アパホテル〈上野駅前〉",
  note="도쿄메트로 우에노역 3번 출구 1분, JR 우에노역 히로코지 출구 3분. 최상층 대욕장(노천탕)", site="https://yado.knt.co.jp/st/S131006/")
P("jr_ueno_hirokoji", "JR 우에노역 히로코지 출구", "station", "ueno", "우에노", jp="東京都台東区上野7-1", jpname="JR上野駅 広小路口",
  note="야마노테선 「池袋・新宿方面」 승강장으로")
P("ikebukuro_st", "이케부쿠로역 동쪽 출구", "station", "ikebukuro", "이케부쿠로", jpname="池袋駅 東口", jp="東京都豊島区南池袋1-28")
P("shimbashi_st", "신바시역", "station", "ginza", "신바시", jpname="新橋駅", jp="東京都港区新橋2-17", note="긴자선 ↔ 유리카모메 환승")
P("daiba_st", "다이바역 (유리카모메)", "station", "odaiba", "오다이바", jpname="台場駅", jp="東京都港区台場2-6")
P("ginza_st", "긴자역", "station", "ginza", "긴자", jpname="銀座駅", jp="東京都中央区銀座4-1")
P("akiba_st", "아키하바라역", "station", "akiba", "아키하바라", jpname="秋葉原駅 電気街口", jp="東京都千代田区外神田1-17")
P("hamamatsucho_st", "하마마츠초역", "station", "tower", "하마마츠초", jpname="浜松町駅", jp="東京都港区海岸1-3")
P("kamiyacho_st", "카미야초역 (히비야선)", "station", "tower", "도쿄타워", jpname="神谷町駅", jp="東京都港区虎ノ門5-12", note="도쿄타워에서 도보 약 7분")
P("hachiko", "하치코 동상 · 스크램블 교차로", "sight", "shibuya", "시부야", jpname="ハチ公像 渋谷", jp="東京都渋谷区道玄坂2-1")

# ----- Ueno -----
P("unatoto", "나다이 우나토토 우에노점", "food", "ueno", "우에노", jp="東京都台東区上野6-11-15", jpname="名代 宇奈とと 上野店",
  hours="10:00–23:00 (L.O. 30분 전)", pay="예약 불가 · 카드·IC·PayPay 가능", brief="장어덮밥 · 매일 영업", site="https://www.unatoto.com/shop/ueno/")
P("kamotonegi", "카모토네기 오카치마치점", "food", "ueno", "우에노", jp="東京都台東区上野6-4-15", jpname="らーめん 鴨to葱 御徒町店",
  hours="24시간 또는 11:00–21:00", pay="현금만 (카드·전자머니·QR 불가)", note="공식 페이지 안에서도 영업시간이 다르게 적혀 있어요. 이케부쿠로점(LINKS IKEBUKURO 8층, 11:00–23:00)도 있어요.",
  tags=["현금", "확인 필요"], brief="오리 라멘", site="https://www.kamotonegi.com/shoprisuto/okachimachi/")
P("nmwa", "국립서양미술관", "sight", "ueno", "우에노", jp="東京都台東区上野公園7-7", jpname="国立西洋美術館",
  hours="09:30–17:30 (금·토 20:00)", closed="월요일", note="상설전 500엔. 테이트 터너전은 10/24 개막이라 이번엔 못 봐요.", brief="월요일 휴관 · 상설전 500엔", site="https://www.nmwa.go.jp/jp/visit/index.html")
P("shinobazu", "우에노 공원 · 시노바즈 연못", "sight", "ueno", "우에노", jpname="不忍池", hours="상시 개방", brief="2일차 밤 산책 가능")
P("ameyoko", "아메요코", "shop", "ueno", "우에노", jp="東京都台東区上野4-9", jpname="アメ横", hours="대체로 08:00–20:00", note="가게마다 달라요. 20시 이후엔 많이 닫아요.", brief="가게마다 다름")
P("donki_ueno", "돈키호테 우에노점", "shop", "ueno", "우에노", jp="東京都文京区湯島3-38-10", jpname="ドン・キホーテ 上野店", hours="09:00–익일 04:00", brief="오카치마치역 5분")
P("tnm", "도쿄국립박물관", "sight", "ueno", "우에노", jp="東京都台東区上野公園13-9", jpname="東京国立博物館", hours="수 09:30–17:00 (최종 16:30)",
  note="상설전 1,000엔. 특별전 「大徳寺」(10/14–12/6), 「歌川広重」(9/29–12/20). 1일차 점심 뒤 1시간 정도 가능.", brief="특별전 2개 진행 중", tip=True, tags=["추천"])
P("zoo", "우에노 동물원", "sight", "ueno", "우에노", jp="東京都台東区上野公園9-83", jpname="上野動物園", hours="09:30–17:00 (최종 16:00)", closed="월요일", note="성인 600엔", brief="600엔", tip=True, tags=["추천"])
P("aki_oka", "2k540 AKI-OKA ARTISAN", "shop", "ueno", "우에노", jp="東京都台東区上野5-9", jpname="2k540 AKI-OKA ARTISAN", hours="11:00–19:00", closed="수요일",
  note="선로 아래 공방 거리. 1일차(수)는 휴무예요.", brief="선로 아래 공방 거리", tip=True, tags=["추천"])

# ----- Ikebukuro -----
P("sunshine_alpa", "선샤인시티 알파", "shop", "ikebukuro", "이케부쿠로", jp="東京都豊島区東池袋3-1-1", jpname="サンシャインシティ 専門店街アルパ",
  hours="쇼핑 10:00–20:00 · 식당 11:00–22:00", note="역에서 도보 8분. 쇼핑은 20:00에 닫으니 먼저 가세요.", brief="쇼핑 20:00 마감", site="https://sunshinecity.jp/information/opening_hour.html")
P("world_import_mart", "이치방쿠지 공식숍 · 가샤폰의 데파트", "shop", "ikebukuro", "이케부쿠로", jp="東京都豊島区東池袋3-1-3", jpname="一番くじ公式ショップ 池袋サンシャインシティ総本店",
  hours="이치방쿠지·가샤폰 둘 다 10:00–21:00", note="선샤인시티 월드임포트마트 3층에 둘 다 있어요. 가샤폰의 데파트(ガシャポンのデパート)는 공식 페이지 기준 21:00까지예요.", brief="월드임포트마트 3층")
P("animate", "애니메이트 이케부쿠로 본점", "shop", "ikebukuro", "이케부쿠로", jp="東京都豊島区東池袋1-20-7", jpname="アニメイト池袋本店",
  hours="10:00–21:00", note="공식 사이트 기준 매일 같은 시간", brief="매일 21:00까지", site="https://www.animate.co.jp/shop/ikebukuro/")
P("donki_ikebukuro", "돈키호테 이케부쿠로 동쪽출구역앞점", "shop", "ikebukuro", "이케부쿠로", jp="東京都豊島区南池袋1-22-5", jpname="ドン・キホーテ 池袋東口駅前店", hours="24시간", brief="24시간")
P("jiro", "라멘지로 이케부쿠로 동쪽출구점", "food", "ikebukuro", "이케부쿠로", jp="東京都豊島区南池袋2-27-17", jpname="ラーメン二郎 池袋東口店",
  hours="17:00–21:30 (타베로그) · 다른 출처 21:45", closed="화요일", note="타베로그 기준 2026년 7월 22일부터 당분간 저녁만 영업해요. 공식 사이트가 없고 2024년에 임시휴업한 적이 있어서, 가기 전 X 계정(@ikejikabuji) 확인을 권해요.", tags=["주의"], brief="당분간 저녁만", site="https://www.ramen-jiro.com/information.html")
P("kohitei", "皇琲亭 (메모의 커피테이)", "cafe", "ikebukuro", "이케부쿠로", jp="東京都豊島区東池袋1-7-2", jpname="炭火煎珈琲 皇琲亭", hours="11:00–22:00", note="다른 출처는 22:30까지. 금연", brief="금연 · 동쪽 출구")
P("renoir_ikebukuro", "카페 르누아르 선샤인60거리점", "cafe", "ikebukuro", "이케부쿠로", jp="東京都豊島区東池袋1-11-4", jpname="喫茶室ルノアール 池袋サンシャイン60通り店", hours="07:30–22:00", note="흡연석 여부는 확인하지 못했어요.", brief="흡연석 미확인")
P("tenbo", "선샤인60 전망대 텐보파크", "sight", "ikebukuro", "이케부쿠로", jpname="サンシャイン60展望台 てんぼうパーク", hours="최종 입장 20:30", note="평일 성인 700엔. 개장 시각은 공식 페이지끼리 10:00·11:00으로 달라요. 마지막 일정으로 야경 보기 좋아요.", brief="마지막 야경 코스", tip=True, tags=["추천"], site="https://sunshinecity.jp/observatory/")
P("pokemon_mega", "포켓몬센터 메가토쿄", "shop", "ikebukuro", "이케부쿠로", jpname="ポケモンセンターメガトウキョー", hours="10:00–20:00", note="알파 2층. 2026년 8월 재개장 후 당분간 입장 제한이 있어 대기할 수 있어요.", brief="알파 2층 · 입장 제한", tip=True, tags=["추천"])
P("otome", "오토메로드", "shop", "ikebukuro", "이케부쿠로", jpname="乙女ロード 池袋", note="선샤인시티 가는 길. 스루가야 오토메관 10:00–21:00", brief="선샤인시티 가는 길", tip=True, tags=["추천"])

# ----- Odaiba -----
P("divercity", "THE GUNDAM BASE TOKYO", "shop", "odaiba", "오다이바", jp="東京都江東区青海1-1-10 ダイバーシティ東京プラザ7F", jpname="THE GUNDAM BASE TOKYO",
  hours="평일 11:00–20:00", note="입장 무료. 건담 이치방쿠지도 여기서 팔아요. 건프라는 1인 1일 1회 구매, 같은 상품 1개, 최대 10개. 빌드룸 휴업 중. 10/22는 추첨 입장일이 아니지만 붐비면 현장 정리권이 나올 수 있어요. 유니콘 건담 입상은 8/31 전시 종료.",
  tags=["주의"], brief="평일 11:00 개장", site="https://www.gundam-base.net/news/55669.html")
P("hellokitty", "헬로키티 재팬 다이버시티점", "shop", "odaiba", "오다이바", jpname="ハローキティジャパン ダイバーシティ東京プラザ店", hours="몰 기준 평일 11:00–20:00", note="메모의 '오다이바 산리오'", brief="메모의 오다이바 산리오")
P("odaiba_beach", "오다이바 해변공원", "sight", "odaiba", "오다이바", jp="東京都港区台場1-4", jpname="お台場海浜公園", note="레인보우브리지와 자유의 여신상 전망. 건담베이스 개장 전 30분 산책에 맞아요.", brief="건담베이스 개장 전 산책", tip=True, tags=["추천"])

# ----- Ginza -----
P("caretta", "우나기노 나루세 카렛타 시오도메점", "food", "ginza", "신바시", jp="東京都港区東新橋1-8-2 カレッタ汐留B1", jpname="鰻の成瀬 カレッタ汐留店",
  hours="11:00–15:00 · 17:00–20:00", pay="온라인·전화 예약 · 카드·IC·PayPay", tel="050-5487-8912", tags=["예약"], brief="장어덮밥")
P("nishiginza", "산리오 니시긴자점 (구 산리오월드 긴자)", "shop", "ginza", "긴자", jp="東京都中央区銀座4-1 西銀座デパート", jpname="サンリオ 西銀座",
  hours="매일 11:00–20:00", tel="03-3566-4040", note="니시긴자 백화점 2층. 니시긴자 공식 페이지 기준 20:00 마감이고 면세가 안 돼요.", brief="20:00까지 · 면세 안 됨")
P("loft_ginza", "긴자 로프트", "shop", "ginza", "긴자", jp="東京都中央区銀座2-4-6 銀座ベルビア館", jpname="銀座ロフト", hours="11:00–21:00",
  note="마로니에게이트가 아니라 긴자 벨비아관 1–5층. 면세 3층(~20:30)", brief="긴자 벨비아관", site="https://www.loft.co.jp/shop_list/detail.php?shop_id=407")
P("marronnier2", "마로니에게이트 긴자2 (다이소·GU)", "shop", "ginza", "긴자", jp="東京都中央区銀座3-2-1", jpname="マロニエゲート銀座2", hours="11:00–21:00",
  note="6층 다이소·Standard Products·THREEPPY, 5층 GU, 1–4층 유니클로 도쿄", brief="5층 GU · 6층 다이소")
P("hanayama", "고다이메 하나야마우동 긴자점", "food", "ginza", "긴자", jp="東京都中央区銀座3-14-13", jpname="五代目 花山うどん 銀座店",
  hours="평일 11:00–15:30 · 17:30–21:30", pay="예약 불가 · 발권기 순서대로", note="대기 줄이 길어요.", brief="우동 · 예약 불가", site="https://hanayamaudon.co.jp/ginza")
P("hokkaibanya", "홋카이반야 (北海番屋)", "food", "ginza", "쓰키지", jp="東京都中央区築地4-14-16", jpname="北海番屋 築地",
  hours="09:00–15:00 (L.O. 14:00) · 저녁 17:00–21:00 (화·목·금·토)", closed="수요일 (출처마다 매주/셋째 주로 다름)", pay="온라인·전화 예약 · 카드·QR 가능", tel="03-5148-0788",
  note="메모의 08:30 개점은 확인되지 않았어요. 모든 출처가 09:00.", tags=["예약"], brief="카이센동")
P("renoir_ginza", "카페 르누아르 긴자2초메 가스등거리점", "cafe", "ginza", "긴자", jp="東京都中央区銀座2-5-7 B1", jpname="喫茶室ルノアール 銀座2丁目ガス灯通り店", hours="08:00–22:00", note="흡연 부스 있음. 로프트·이토야 근처", brief="흡연 부스 있음")
P("muji_ginza", "무인양품 긴자", "shop", "ginza", "긴자", jp="東京都中央区銀座3-3-5", jpname="無印良品 銀座", hours="11:00–21:00", note="세계 플래그십, 면세 4층. 마로니에게이트 바로 옆", brief="세계 플래그십", tip=True, tags=["추천"])
P("itoya", "긴자 이토야 본점", "shop", "ginza", "긴자", jp="東京都中央区銀座2-7-15", jpname="銀座 伊東屋 本店", hours="평일 10:00–20:00", note="12층 문구 전문점, 12층 카페", brief="12층 문구점", tip=True, tags=["추천"])
P("ginza_six", "긴자 식스 옥상정원", "sight", "ginza", "긴자", jp="東京都中央区銀座6-10-1", jpname="GINZA SIX ガーデン", hours="07:00–23:00 (무료)", note="13층. 쇼핑 중간 휴식", brief="무료 옥상정원", tip=True, tags=["추천"])
P("butter", "BUTTER 미에이 방목낙농장", "food", "tokyo", "도쿄역", jp="東京都千代田区丸の内2-4-1 丸ビルB1", jpname="BUTTER 美瑛放牧酪農場",
  hours="판매 10:00–21:00 · 카페 11:00–19:00 또는 20:00", tel="03-5860-3695", note="카페 마감이 출처마다 달라요. 오전~오후 대기 줄", brief="선택 일정")

# ----- Akihabara -----
P("radiokaikan", "아키하바라 라디오회관", "shop", "akiba", "아키하바라", jp="東京都千代田区外神田1-15-16", jpname="秋葉原ラジオ会館",
  hours="10:00–20:00 (B1층만 평일 22:30)", note="18:30 도착이면 약 1시간 반이에요.", tags=["주의"], brief="20:00 마감")
P("surugaya_plamo", "스루가야 아키하바라 프라모델관", "shop", "akiba", "아키하바라", jp="東京都千代田区外神田4-4-2", jpname="駿河屋 秋葉原プラモデル館", hours="평일 11:00–21:00", note="2–3층", brief="21:00까지")
P("surugaya_honkan", "스루가야 아키하바라 본관", "shop", "akiba", "아키하바라", jp="東京都千代田区外神田3-11-3", jpname="駿河屋 秋葉原本館", hours="평일 11:00–21:00", note="피규어. 1층은 9/14부터 포켓몬 카드 매장. 5–6층 성인 전용", brief="피규어 · 21:00까지")
P("hanamaru", "하나마루 우동 아키하바라", "food", "akiba", "아키하바라", jp="東京都千代田区神田松永町1 宮沢ビル中2F", jpname="はなまるうどん 秋葉原", hours="매일 10:00–22:00", brief="셀프 우동 · 빠르고 저렴")
P("trader", "트레이더 본점 (アキバ トレーダー)", "shop", "akiba", "아키하바라", jp="東京都千代田区外神田4-2-1", jpname="トレーダー 秋葉原本店", hours="매일 11:00–20:00", note="중고 게임·피규어. 면세 안 됨. 2호점(外神田1-4-9)도 근처", brief="중고 게임·피규어 · 20:00까지")
P("donki_akiba", "돈키호테 아키하바라점", "shop", "akiba", "아키하바라", jp="東京都千代田区外神田4-3-3", jpname="ドン・キホーテ 秋葉原店", hours="24시간", note="8층 AKB48 극장", brief="24시간")
P("yodobashi", "요도바시 멀티미디어 Akiba", "shop", "akiba", "아키하바라", jp="東京都千代田区神田花岡町1-1", jpname="ヨドバシAkiba", hours="09:30–22:00", note="6층 하비·가챠. 라디오회관이 닫은 뒤 마무리하기 좋아요.", brief="22:00까지")
P("maach", "마치 에큐트 간다 만세이바시", "shop", "akiba", "아키하바라", jp="東京都千代田区神田須田町1-25-4", jpname="マーチエキュート神田万世橋", hours="11:00–22:00", note="옛 만세이바시역 플랫폼을 쓴 상가. 아키하바라에서 도보권", brief="옛 역 플랫폼 상가", tip=True, tags=["추천"])

# ----- Tokyo Tower -----
P("iwai", "돈카츠 이와이", "food", "tower", "하마마츠초", jp="東京都港区芝公園2-3-7 玉川ビル2F", jpname="とんかつ いわい",
  hours="평일 11:30–14:30 (L.O. 13:45) · 17:30–20:30 (L.O. 19:45)", closed="일요일", pay="현금만 · 예약 불가",
  note="밥이 떨어지면 일찍 닫아요. 두꺼운 로스카츠 정식은 하루 8인분.", tags=["현금"], brief="현금만 · 점심 L.O. 13:45", site="https://tabelog.com/tokyo/A1314/A131401/13170377/")
P("zojoji", "조조지 (증상사)", "sight", "tower", "도쿄타워", jp="東京都港区芝公園4-7-35", jpname="増上寺", hours="경내 09:00–17:00 (무료)", note="보물전시실 평일 11:00–15:00, 700엔. 삼해탈문은 2032년까지 보수 중", brief="경내 무료")
P("tokyo_tower", "도쿄타워", "sight", "tower", "도쿄타워", jp="東京都港区芝公園4-2-8", jpname="東京タワー", hours="09:00–23:00 (최종 22:30)", note="메인덱 1,500엔. 탑덱 투어 온라인 3,300엔·현장 3,500엔", brief="메인덱 1,500엔")
P("shiba_park", "시바공원 4호지 산책로", "sight", "tower", "도쿄타워", jpname="芝公園 4号地", hours="상시 개방", note="도쿄타워를 정면으로 찍는 사진 명소. 19호지 단풍 골짜기도 추천", brief="도쿄타워 사진 명소", tip=True, tags=["추천"])
P("kyushiba", "구 시바리큐 정원", "sight", "tower", "하마마츠초", jp="東京都港区海岸1-4-1", jpname="旧芝離宮恩賜庭園", hours="09:00–17:00 (최종 16:30)", note="150엔. 하마마츠초 북쪽 출구 1분. 돈카츠 대기 전후 짧은 산책", brief="역 앞 정원 · 150엔", tip=True, tags=["추천"])
P("fudanotsuji", "후다노츠지 육교 (메모의 Tokyo Fudanotsuji)", "sight", "tower", "다마치", jpname="札の辻歩道橋", jp="東京都港区芝5-29", hours="24시간",
  note="식당이 아니라 도쿄타워 정면 사진 명소예요. 도쿄타워에서 남쪽으로 약 2km라 이번 동선엔 우회가 필요해요.", tags=["주의"], brief="도쿄타워에서 약 2km")

# ----- Shibuya -----
P("parco", "시부야 파르코", "shop", "shibuya", "시부야", jp="東京都渋谷区宇田川町15-1", jpname="渋谷PARCO", hours="11:00–21:00 · 6층 10:00–21:00",
  note="6층 닌텐도 도쿄·포켓몬센터 시부야. 닌텐도는 붐비는 날 정리권", brief="6층 닌텐도·포켓몬", site="https://shibuya.parco.jp/info/access/")
P("mega_donki", "MEGA 돈키호테 시부야 본점", "shop", "shibuya", "시부야", jp="東京都渋谷区宇田川町28-6", jpname="MEGAドン・キホーテ渋谷本店", hours="24시간", brief="24시간")
P("shibuya109", "SHIBUYA109", "shop", "shibuya", "시부야", jp="東京都渋谷区道玄坂2-29-1", jpname="SHIBUYA109渋谷店", hours="10:00–21:00", brief="21:00까지")
P("tsutaya", "스타벅스 시부야 츠타야 2층", "cafe", "shibuya", "시부야", jp="東京都渋谷区宇田川町21-6", jpname="スターバックス SHIBUYA TSUTAYA", hours="07:00–22:30", note="스크램블 교차로를 내려다보는 자리", brief="교차로 뷰")
P("loft_shibuya", "시부야 로프트", "shop", "shibuya", "시부야", jp="東京都渋谷区宇田川町18-2", jpname="渋谷ロフト", hours="11:00–21:00", note="면세 20:30까지", brief="21:00까지")
P("tokyu_plaza", "도큐플라자 시부야", "shop", "shibuya", "시부야", jp="東京都渋谷区道玄坂1-2-3", jpname="東急プラザ渋谷", hours="11:00–20:00", note="옥상 17층도 20:00까지 (2024년 정보)", brief="옥상 17층")
P("bleubleuet", "블루블루에 시부야 지하가점", "shop", "shibuya", "시부야", jp="東京都渋谷区道玄坂2-2-1 渋谷地下街B1", jpname="Bleu Bleuet 渋谷地下街店", hours="10:00–21:00", note="손수건·잡화 브랜드", brief="손수건·잡화")
P("gu_shibuya", "GU 시부야점", "shop", "shibuya", "시부야", jp="東京都渋谷区宇田川町32-13", jpname="GU 渋谷店", hours="매일 11:00–22:00 (구글)", brief="센터가 쪽 · 22:00까지")
P("qpot", "Q-pot CAFE. 오모테산도 본점", "cafe", "shibuya", "오모테산도", jp="東京都渋谷区神宮前3-4-8", jpname="Q-pot CAFE. 表参道本店", hours="11:00–19:00 (L.O. 18:30)",
  note="시부야역 근처엔 없어요. 오모테산도역 A2 출구 도보 6~7분. 코난 콜라보(10/16–11/15)는 사전 예약. 캐스키드슨 카페는 현재 없어요.", tags=["주의"], brief="시부야가 아니라 오모테산도", site="https://www.q-pot.jp/cafe/")
P("yurinan", "YURINAN 유린안 (메모의 URINAN 도라야키)", "food", "shibuya", "하라주쿠", jp="東京都渋谷区神宮前1-7-5", jpname="YURINAN ゆうりんあん", hours="11:00–19:00", note="시부야가 아니라 하라주쿠 다케시타도리", tags=["주의"], brief="도라야키 · 하라주쿠")
P("maasan", "마상 본점 (구 마상의 집)", "food", "shibuya", "시부야", jp="東京都渋谷区道玄坂2-23-11 B1", jpname="まーさん 本店",
  hours="11:30–15:00 (L.O. 14:30) · 17:00–21:00 (L.O. 20:30)", closed="월요일", pay="카드·Suica·PayPay 가능", note="시부야 스카이(19:00) 뒤엔 L.O.에 걸려요. 17:00 이른 저녁 추천", brief="함박 · L.O. 20:30")
P("hikiniku", "히키니쿠토코메 시부야", "food", "shibuya", "시부야", jp="東京都渋谷区道玄坂2-28-1 3F", jpname="挽肉と米 渋谷",
  hours="11:00–15:00 · 17:00–21:00", closed="첫째·셋째 수요일", pay="완전 캐시리스 · TableCheck 예약 (7일 전 오전 9시쯤 오픈)", note="좁은 계단 3층. 10분 이상 늦으면 취소돼요.",
  tags=["예약"], brief="함박 · 캐시리스", site="https://www.tablecheck.com/shops/hikinikutocome/reserve")
P("kuuya", "츠키시마 몬자 쿠우야 시부야", "food", "shibuya", "시부야", jp="東京都渋谷区渋谷1-25-6 1F", jpname="月島もんじゃ くうや 渋谷",
  hours="11:00(평일 12:00)–익일 04:00", pay="예약 가능 · 카드·QR 가능", tel="03-6712-6788", tags=["예약"], brief="몬자야키 · 늦게까지")
P("shirube", "시루베에 (汁べゑ) 시부야점", "food", "shibuya", "시부야", jp="東京都渋谷区神南1-11-5 2F", jpname="汁べゑ 渋谷店",
  hours="17:00–23:00 (L.O. 22:00)", pay="예약 권장(금요일) · 카드 가능", tel="03-3463-1010", tags=["예약"], brief="이자카야")
P("shibuya_sky", "시부야 스카이", "sight", "shibuya", "시부야", jp="東京都渋谷区渋谷2-24-12 渋谷スクランブルスクエア", jpname="SHIBUYA SKY",
  hours="10:00–22:30 (최종 21:20)", note="입구 14층. 큰 짐·모자·삼각대·셀카봉은 46층 사물함에. 강풍·비가 오면 옥상이 닫혀요.", tags=["예매 완료"], brief="입구 14층")
P("nintendo", "닌텐도 도쿄 · 포켓몬센터 시부야", "shop", "shibuya", "시부야", jpname="Nintendo TOKYO 渋谷PARCO", hours="10:00–21:00", note="파르코 6층. 14:30 도착하면 먼저 가세요.", brief="파르코 6층", tip=True, tags=["추천"])
P("miyashita", "미야시타 파크", "sight", "shibuya", "시부야", jp="東京都渋谷区神宮前6-20-10", jpname="MIYASHITA PARK", hours="상점 11:00–21:00", note="옥상 공원", brief="옥상 공원", tip=True, tags=["추천"])
P("yokocho", "시부야 요코초", "food", "shibuya", "시부야", jpname="渋谷横丁", hours="11:00–05:00", note="미야시타 파크 1층. 전국 음식 포장마차 거리. 시부야 스카이 다음에 간단히", brief="스카이 다음 야식", tip=True, tags=["추천"])
P("nonbei", "논베이 요코초", "food", "shibuya", "시부야", jp="東京都渋谷区渋谷1-25-10", jpname="のんべい横丁", hours="18:00 무렵부터", pay="대부분 현금 · 자릿세 500~1,000엔", tags=["현금"], brief="작은 술집 골목", tip=True)
P("tower_records", "타워레코드 시부야", "shop", "shibuya", "시부야", jp="東京都渋谷区神南1-22-14", jpname="タワーレコード渋谷店", hours="11:00–22:00", brief="음반·아이돌 굿즈", tip=True, tags=["추천"])
P("hikarie", "시부야 히카리에 ShinQs", "shop", "shibuya", "시부야", jp="東京都渋谷区渋谷2-21-1", jpname="渋谷ヒカリエ ShinQs", hours="11:00–21:00", note="B2 디저트", brief="B2 디저트", tip=True, tags=["추천"])


# ---------- Google review recommendations ----------
from rec_data import RECS, REC_GROUPS, TABELOG
for r in RECS:
    r = dict(r)
    ll = r.pop("ll"); COORDS[r["key"]] = ll
    tb = TABELOG.get(r["key"], {})
    tags = ["추천"] + r.pop("tags", [])
    P(r.pop("key"), r.pop("name"), r.pop("cat"), r.pop("area"), r.pop("areaName"), jp=r.pop("jp"), jpname=r.pop("jpname"),
      hours=r.pop("hours"), brief=r.pop("brief",""), tags=tags,
      rec=True, pid=r.pop("pid"), g=r.pop("g"), wait=r.pop("wait",""), fit=r.pop("fit",""), rvT=r.pop("rvT",""),
      tb=tb.get("score",""), rvL=tb.get("note",""), closed=tb.get("closed",""), pay=tb.get("pay",""), site=tb.get("url",""))
# ---------- 2nd-round recommendations ----------
from rec_data2 import RECS2, REC_GROUPS2
import json as _json, glob as _glob, os as _os
EXTRA = {}
_base = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "data")
for f in sorted(_glob.glob(_os.path.join(_base, "res_*.json"))):
    for o in _json.load(open(f)):
        EXTRA[o["key"]] = o
for f in sorted(_glob.glob(_os.path.join(_base, "res2_*.json"))):  # 2차: 빈칸만 채움
    for o in _json.load(open(f)):
        cur = EXTRA.setdefault(o["key"], {"key": o["key"]})
        for src in ("retty", "hotpepper", "tripcom", "ko", "jp"):
            _h = lambda v: bool(v and any(v.get(x) for x in ("pct", "rating", "gist", "note")))
            if _h(o.get(src)) and not _h(cur.get(src)): cur[src] = o[src]
for r in RECS2:
    r = dict(r)
    ll = r.pop("ll"); COORDS[r["key"]] = ll
    tb = (EXTRA.get(r["key"]) or {}).get("tabelog") or {}
    P(r.pop("key"), r.pop("name"), r.pop("cat"), r.pop("area"), r.pop("areaName"), jp=r.pop("jp"), jpname=r.pop("jpname"),
      hours=r.pop("hours"), brief=r.pop("brief",""), tags=["추천"],
      rec=True, pid=r.pop("pid"), g=r.pop("g"), wait=r.pop("wait",""), fit=r.pop("fit",""), rvT=r.pop("rvT",""), warn=r.pop("warn",""),
      tb=str(tb.get("score") or ""), tbn=tb.get("n"), closed=tb.get("closed") or "", pay=tb.get("pay") or "", site=tb.get("url") or "")
from rec_data3 import RECS3, MEAL_ADD, REC_GROUPS3
for r in RECS3:
    r = dict(r)
    ll = r.pop("ll"); COORDS[r["key"]] = ll
    tb = (EXTRA.get(r["key"]) or {}).get("tabelog") or {}
    P(r.pop("key"), r.pop("name"), r.pop("cat"), r.pop("area"), r.pop("areaName"), jp=r.pop("jp"), jpname=r.pop("jpname"),
      hours=r.pop("hours"), brief=r.pop("brief",""), tags=["추천"],
      rec=True, pid=r.pop("pid"), g=r.pop("g"), wait=r.pop("wait",""), fit=r.pop("fit",""), rvT=r.pop("rvT",""), warn=r.pop("warn",""),
      tb=str(tb.get("score") or ""), tbn=tb.get("n"), rvL=tb.get("gist") or "", closed=tb.get("closed") or "", pay=" · ".join(x for x in [tb.get("pay"), ("예약 "+tb["reserve"]) if tb.get("reserve") else ""] if x), site=tb.get("url") or "")
for gid, ks in REC_GROUPS3.items():
    REC_GROUPS["food"].setdefault(gid, []).extend(ks)
for side in ("food", "place"):
    for gid, ks in REC_GROUPS2[side].items():
        REC_GROUPS[side].setdefault(gid, []).extend(ks)

# existing tip labels: "추천" -> "근처" so new recommendations stand apart
for k, v in places.items():
    if not v.get("rec") and "추천" in v["tags"]:
        v["tags"] = ["근처" if t == "추천" else t for t in v["tags"]]

# ---------- review analysis for existing places (no "추천" tag) ----------
from existing_reviews import EXIST, TB_EXIST, TB_WARN
for k, e in EXIST.items():
    if k not in places: print("missing", k); continue
    v = places[k]
    v["g"] = dict(r=e["g"][0], n=e["g"][1]); v["pid"] = e["pid"]
    for f in ("gh", "rvT", "wait"):
        if e.get(f): v[f] = e[f]
    w = [x for x in (e.get("warn"), TB_WARN.get(k)) if x]
    if w: v["warn"] = " ".join(w)
for k, t in TB_EXIST.items():
    v = places[k]; v["tb"] = t[0]; v["rvL"] = t[2]
    if t[1]: v["tbn"] = t[1]
from existing_reviews import NO_GOOGLE
for k, msg in NO_GOOGLE.items():
    if k in places: places[k]["gnone"] = msg
def _num(x):
    try: return float(str(x).replace(",","").replace("%",""))
    except Exception: return None
for k, o in EXTRA.items():
    if k not in places: continue
    ex = {}
    for src in ("retty", "hotpepper", "tripcom", "ko", "jp"):
        v = o.get(src)
        if src == "tripcom" and v and (_num(v.get("n")) or 0) < 3: v = dict(v, rating=None, n=None)  # 리뷰 1–2개짜리 점수는 숨김
        if v and any(v.get(f) for f in ("pct", "rating", "gist", "note")):
            ex[src] = {kk: vv for kk, vv in v.items() if vv not in (None, "")}
    if ex: places[k]["ex"] = ex
# every place gets an explicit Tabelog status
for k, v in places.items():
    if v["cat"] in ("station", "hotel"): continue
    if not v.get("tb"):
        v["tbna"] = "음식점만 다루는 사이트라 해당 없음" if v["cat"] not in ("food", "cafe") else "등록 정보 없음"
if "hanamaru" in places: places["hanamaru"]["tbna"] = "이 지점 페이지를 찾지 못했어요 (전국 체인 우동집)"

COORDS.setdefault("hanamaru", [35.6990522, 139.7751523]); COORDS.setdefault("trader", [35.7001624, 139.7716489])
# fix coords keys aliasing
alias = {"tenbo": None, "pokemon_mega": "sunshine_alpa", "nintendo": "parco", "hellokitty": "divercity", "yokocho": "miyashita"}
for k, v in alias.items():
    if v and k not in COORDS: COORDS[k] = COORDS[v]

# ---------- Street View viewpoints ----------
import math
def _bearing(a, b):
    y = math.sin(math.radians(b[1]-a[1]))*math.cos(math.radians(b[0]))
    x = math.cos(math.radians(a[0]))*math.sin(math.radians(b[0]))-math.sin(math.radians(a[0]))*math.cos(math.radians(b[0]))*math.cos(math.radians(b[1]-a[1]))
    return round((math.degrees(math.atan2(y, x))+360) % 360)
TOWER = (35.658649, 139.745468)
SV = {  # photo spots: stand here, face the landmark
 "fudanotsuji": ((35.6436811, 139.7443006), TOWER, "도쿄타워 쪽을 바라보는 방향으로 열려요"),
 "zojoji": ((35.65745, 139.74905), TOWER, "본당 너머 도쿄타워가 보이는 방향으로 열려요"),
 "shiba_park": ((35.65893, 139.75140), TOWER, "도쿄타워 쪽을 바라보는 방향으로 열려요"),
 "hachiko": ((35.6590552, 139.7006288), (35.65952, 139.70055), "스크램블 교차로 쪽으로 열려요"),
}
for k, v in places.items():
    if v.get("nomap") or v["cat"] == "station" and k == "narita": continue
    if k in SV:
        at, to, hint = SV[k]; v["sv"] = [at[0], at[1], _bearing(at, to)]; v["svh"] = hint
    elif k == "tenbo" and "sunshine_alpa" in COORDS:
        v["sv"] = list(COORDS["sunshine_alpa"]); v["svh"] = "선샤인시티 건물 외관을 보는 용도예요"
    elif k in COORDS:
        v["sv"] = [COORDS[k][0], COORDS[k][1]]
        if v["cat"] in ("shop", "food", "cafe"): v["svh"] = "건물 외관·입구를 미리 확인하는 용도예요"

# ---------- days ----------
def S(time, title, k=None, note="", tags=None, move=False, major=False, minor=False, nomap=False, hs=None, meal=None):
    d = dict(time=time, title=title, note=note, move=move, major=major, minor=minor, nomap=nomap)
    if meal: d["meal"] = meal
    if hs: d["hs"] = hs
    if k: d["k"] = k
    if tags is not None: d["tags"] = tags
    return d

days = [
 dict(long="10월 21일 수요일", id="d1", date="2026-10-21", short="1일차", when="10/21 수", route=["나리타", "우에노", "이케부쿠로"],
  sub="13:22 스카이라이너 · 16:30 선샤인시티 · 19:00 저녁 (이케부쿠로)",
  callout="<b>선샤인시티 쇼핑은 20:00에 닫아요.</b> 이치방쿠지(21:00)와 애니메이트(21:00)보다 먼저 가세요.",
  steps=[
   S("05:30", "청주공항으로 출발", None, "", hs="출발"),
   S("07:00", "청주공항 도착", None, "주차비 경차 하루 약 5천 원(4일 약 2만 원) · Visit Japan Web 작성"),
   S("09:30", "청주공항 비행기 탑승", None, "", move=True),
   S("11:50", "나리타 3터미널 도착", "narita", "입국 수속 약 1시간. 3→2터미널은 연결버스 약 5분", nomap=True, hs="나리타"),
   S("13:22", "스카이라이너 탑승", "airport2_st", "공항 제2빌딩 13:22 → 게이세이우에노 14:09 (다음 차 13:42 → 14:23)", move=True, nomap=True),
   S("14:09", "게이세이우에노역 도착", "keisei_ueno", "숙소까지 약 340m"),
   S("14:30", "숙소 체크인·짐 맡기기", "hotel", major=True, hs="숙소"),
   S("15:00", "점심", "unatoto", "", meal=dict(area="우에노", orig=["unatoto", "kamotonegi"], groups=[dict(label="추천 (리뷰 기반)", keys=["r_gyukatsu", "r_ichiban"])])),
   S("16:00", "JR 우에노역 → 이케부쿠로", "jr_ueno_hirokoji", "야마노테선 「池袋・新宿方面」 약 16분"),
   S("16:20", "이케부쿠로역 동쪽 출구", "ikebukuro_st", "", move=True, minor=True),
   S("16:30", "둘러볼 곳", "sunshine_alpa", "닫는 시간: 선샤인 20:00 · 이치방쿠지·애니메이트 21:00 · 돈키 24시간", major=True, hs="이케부쿠로",
     meal=dict(kind="place", area="이케부쿠로", route=["sunshine_alpa", "world_import_mart", "animate", "donki_ikebukuro"], rnote="가장 먼저 닫는 선샤인(20:00)부터 보고, 같은 쪽 이치방쿠지를 거쳐 역 방향으로 돌아오며 애니메이트·돈키. 저녁 라멘지로도 역 동쪽이라 끝나고 바로 가요.", orig=["animate", "world_import_mart", "sunshine_alpa", "donki_ikebukuro"],
               groups=[dict(label="근처", keys=["tenbo", "pokemon_mega", "otome"]), dict(label="추천 (리뷰 기반)", keys=["r_lashinbang"])])),
   S("19:00", "저녁", "jiro", "", major=True, hs="저녁", meal=dict(area="이케부쿠로", orig=["jiro"], groups=[dict(label="추천 (리뷰 기반)", keys=["r_mutekiya", "n_ikkoku"])])),
   S("귀가", "야마노테선 → 우에노", "hotel", "「上野・東京方面」 환승 없음", move=True),
  ]),
 dict(long="10월 22일 목요일", id="d2", date="2026-10-22", short="2일차", when="10/22 목", route=["오다이바", "긴자", "아키하바라"],
  sub="11:00 건담베이스 · 14:00 긴자 (짧게) · 16:00 아키하바라",
  callout="<b>건담베이스는 평일 11:00에 열어요.</b> 긴자는 1시간 반 정도만 보고 16시쯤 아키하바라로 가요. 아키하바라는 대부분 <b>20:00에 닫아서</b> 저녁은 그 뒤에 먹는 게 쇼핑 시간을 아껴요.",
  steps=[
   S("10:00", "숙소 출발", "hotel", "메트로 3번 출구 → 긴자선 신바시행 약 16분", hs="숙소"),
   S("", "신바시역 환승", "shimbashi_st", "긴자선 → 유리카모메 약 15분", move=True, minor=True),
   S("", "다이바역", "daiba_st", "", move=True, minor=True),
   S("11:00", "둘러볼 곳", "divercity", "건담베이스 평일 11:00 개장 · 다이버시티 7층", tags=["주의"], major=True, hs="오다이바",
     meal=dict(kind="place", area="오다이바", route=["divercity", "hellokitty"], rnote="둘 다 다이버시티 안이에요(7층 → 2층). 시간 남으면 해변공원은 걸어서 10분.", orig=["divercity", "hellokitty"], groups=[dict(label="근처", keys=["odaiba_beach"])])),
   S("12:30", "점심", "caretta", "유리카모메로 신바시 복귀 후 도보", move=True, hs="시오도메", meal=dict(area="긴자", orig=["caretta", "hanayama", "hokkaibanya"], groups=[dict(label="추천 (리뷰 기반)", keys=["r_hibiki"])])),
   S("14:00", "둘러볼 곳", "nishiginza", "긴자선 1정거장 · 1시간 반 정도만", move=True, hs="긴자",
     meal=dict(kind="place", area="긴자", route=["nishiginza", "marronnier2", "loft_ginza"], rnote="니시긴자 → 마로니에게이트 → 로프트가 긴자역에서 북쪽으로 한 줄이라 걸어서 각각 3–5분이에요. 로프트에서 JR 유라쿠초역이 가까워서 바로 아키하바라로 넘어가기 좋아요.", orig=["nishiginza", "marronnier2", "loft_ginza"],
               groups=[dict(label="근처", keys=["muji_ginza", "itoya", "ginza_six"]), dict(label="추천 (리뷰 기반)", keys=["n_caretta_sky", "n_kitte"])])),
   S("15:30", "긴자 → 아키하바라", "akiba_st", "JR 유라쿠초 → 아키하바라 (야마노테·게이힌토호쿠선) 또는 히비야선 긴자 → 아키하바라 약 12분", move=True, minor=True),
   S("16:00", "둘러볼 곳", "radiokaikan", "닫는 시간: 라디오회관·트레이더·가샤폰 회관 20:00 · 스루가야 21:00 · 돈키 24시간", tags=["주의"], major=True, hs="아키하바라",
     meal=dict(kind="place", area="아키하바라", route=["radiokaikan", "trader", "surugaya_plamo", "donki_akiba"], rnote="20:00에 닫는 라디오회관·트레이더를 먼저, 21:00 스루가야, 마지막에 24시간 돈키. 넷 다 역에서 걸어서 5분 안이에요. 4시간쯤 있으니 근처·추천 가게도 섞어 보세요.", orig=["radiokaikan", "surugaya_plamo", "trader", "donki_akiba"],
               groups=[dict(label="근처", keys=["surugaya_honkan", "yodobashi", "maach"]), dict(label="추천 (리뷰 기반)", keys=["r_amiami", "r_kotobukiya", "n_gachapon", "n_superpotato", "n_hey"])])),
   S("20:00", "저녁", "hanamaru", "가게들이 20시에 닫은 뒤 먹으면 쇼핑 시간을 아껴요. 마루고는 마지막 주문이 20:00이라 먹으려면 19시 전에 가세요.", meal=dict(area="아키하바라", orig=["hanamaru"], groups=[dict(label="추천 (리뷰 기반)", keys=["n_ichinisan", "r_tsujita", "n_marugo"])])),
   S("귀가", "히비야선 → 우에노", "hotel", "2정거장, 3번 출구 = 숙소", move=True),
   S("", "우에노 돈키호테", "donki_ueno", "숙소 근처 · 새벽 4시까지"),
  ]),
 dict(long="10월 23일 금요일", id="d3", date="2026-10-23", short="3일차", when="10/23 금", route=["도쿄타워", "시부야"],
  sub="11:30 점심 (하마마츠초) · 14:30 시부야 · 19:00 시부야 스카이",
  callout="점심·저녁은 정해 두지 않았어요. 일정의 <b>점심 후보 · 저녁 후보</b>를 누르면 그 지역 후보가 나와요. 저녁은 시부야 스카이(19:00) 전인 17:00쯤이 좋아요.",
  steps=[
   S("10:50", "숙소 출발", "hotel", "JR 우에노 → 「品川方面」 하마마츠초 (환승 없음)", hs="숙소"),
   S("11:20", "하마마츠초역", "hamamatsucho_st", "", move=True, minor=True),
   S("11:30", "점심", "iwai", "", major=True, hs="점심", meal=dict(area="하마마츠초", orig=["iwai"], groups=[dict(label="시오도메 쪽 (걸어서 10–15분)", keys=["caretta", "r_hibiki"])])),
   S("12:45", "둘러볼 곳", "shiba_park", "시바공원 4호지가 사진 명소", major=True, hs="도쿄타워",
     meal=dict(kind="place", area="도쿄타워", route=["shiba_park", "tokyo_tower"], rnote="이와이에서 시바공원 4호지(사진 명소)를 지나 도쿄타워로. 후다노츠지는 남쪽으로 약 2km라 시간이 남을 때만 가세요.", orig=["tokyo_tower", "shiba_park", "fudanotsuji"], groups=[dict(label="근처", keys=["zojoji", "kyushiba"])])),
   S("14:00", "카미야초역 → 시부야", "kamiyacho_st", "히비야선 에비스 → JR 1정거장"),
   S("14:30", "둘러볼 곳", "hachiko", "하치코 출구로 나오기 · 닫는 시간: 109·파르코 21:00 · 돈키 24시간", move=True, major=True, hs="시부야",
     meal=dict(kind="place", area="시부야", route=["hachiko", "tsutaya", "shibuya109", "mega_donki", "parco"], rnote="하치코 → 교차로 건너 스타벅스 2층 → 109 → 메가돈키 → 파르코 6층으로 한 바퀴 도는 순서예요. 원본 순서(메가돈키 → 파르코 → 109)로 가도 거리 차이는 크지 않아요.", orig=["hachiko", "tsutaya", "mega_donki", "parco", "shibuya109"],
               groups=[dict(label="원본 · 여유 되면", keys=["gu_shibuya", "loft_shibuya", "qpot", "yurinan", "tokyu_plaza", "bleubleuet"], orig=True),
                       dict(label="근처", keys=["nintendo", "miyashita", "tower_records", "hikarie"]),
                       dict(label="추천 (리뷰 기반)", keys=["r_linefriends", "r_mandarake", "r_hikarie_sky"])])),
   S("17:00", "저녁", "maasan", "", meal=dict(area="시부야", orig=["maasan", "kuuya", "hikiniku", "shirube"], groups=[dict(label="추천 (리뷰 기반)", keys=["r_matsue", "r_uogashi"]), dict(label="근처 골목 술집 (원본에 없음)", keys=["yokocho", "nonbei"])])),
   S("19:00", "시부야 스카이", "shibuya_sky", "입구 14층", tags=["예매 완료"], major=True, hs="스카이"),
   S("귀가", "긴자선 → 우에노", "hotel", "직행 약 30분 · 게이세이우에노에서 귀국표 교환", move=True),
  ]),
 dict(long="10월 24일 토요일", id="d4", date="2026-10-24", short="4일차", when="10/24 토", route=["우에노", "나리타", "귀국"],
  sub="09:40 스카이라이너 · 11:00 공항 · 13:05 출국",
  callout="여유를 원하면 <b>09:15발(10:01 도착)</b>, 늦어지면 <b>09:55발(10:41 도착)</b>도 있어요.",
  steps=[
   S("09:20", "체크아웃 · 출발", "hotel", "게이세이우에노역까지 약 340m", hs="숙소"),
   S("09:40", "스카이라이너 25호", "keisei_ueno", "게이세이우에노 09:40 → 공항 제2빌딩 10:21 (토요일 시간표)", major=True, hs="스카이라이너"),
   S("10:25", "2터미널 → 3터미널", "narita", "연결버스 또는 도보 약 15분", move=True, nomap=True),
   S("11:00", "3터미널 체크인", "narita", "", nomap=True, hs="나리타"),
   S("13:05", "출국", None, "", major=True, hs="출국"),
  ]),
]

foodGroups = [
 dict(id="ueno", title="우에노", when="1일차 점심 · 숙소 근처", c="var(--ink)", items=["unatoto", "kamotonegi"]),
 dict(id="ikebukuro", title="이케부쿠로", when="1일차", c="var(--d1)", items=["jiro", "kohitei", "renoir_ikebukuro"]),
 dict(id="ginza", title="신바시 · 긴자 · 쓰키지", when="2일차", c="var(--d2)", items=["caretta", "hanayama", "hokkaibanya", "renoir_ginza", "butter"]),
 dict(id="akiba", title="아키하바라", when="2일차 저녁", c="var(--d2)", items=["hanamaru"]),
 dict(id="tower", title="하마마츠초", when="3일차 점심", c="var(--d3)", items=["iwai"]),
 dict(id="shibuya", title="시부야 · 하라주쿠", when="3일차", c="var(--d3)", items=["maasan", "hikiniku", "kuuya", "shirube", "tsutaya", "qpot", "yurinan"], tips=["yokocho", "nonbei"]),
]
placeGroups = [
 dict(id="ikebukuro", title="이케부쿠로", when="1일차", c="var(--d1)", items=["sunshine_alpa", "world_import_mart", "animate", "donki_ikebukuro"], tips=["tenbo", "pokemon_mega", "otome"]),
 dict(id="odaiba", title="오다이바", when="2일차", c="var(--d2)", items=["divercity", "hellokitty"], tips=["odaiba_beach"]),
 dict(id="ginza", title="긴자", when="2일차", c="var(--d2)", items=["nishiginza", "loft_ginza", "marronnier2"], tips=["muji_ginza", "itoya", "ginza_six"]),
 dict(id="akiba", title="아키하바라", when="2일차 저녁", c="var(--d2)", items=["radiokaikan", "surugaya_plamo", "trader", "donki_akiba"], tips=["surugaya_honkan", "yodobashi", "maach"]),
 dict(id="tower", title="도쿄타워 · 시바", when="3일차", c="var(--d3)", items=["tokyo_tower", "shiba_park", "fudanotsuji"], tips=["zojoji", "kyushiba"]),
 dict(id="shibuya", title="시부야", when="3일차", c="var(--d3)", items=["shibuya_sky", "parco", "mega_donki", "shibuya109", "loft_shibuya", "tokyu_plaza", "bleubleuet", "gu_shibuya"], tips=["nintendo", "miyashita", "tower_records", "hikarie"]),
 dict(id="ueno", title="숙소 주변 우에노", when="언제든", c="var(--ink)", items=["nmwa", "shinobazu", "donki_ueno"], tips=["ameyoko", "tnm", "zoo", "aki_oka"]),
]
alerts = [
 "<b>건담베이스는 평일 11:00 개장</b>이에요. 유니콘 건담 실물 크기 입상은 8/31에 전시가 끝났어요.",
 "메모의 \"이치방쿠지 7층 건담\"은 아키하바라가 아니라 <b>오다이바 건담베이스(다이버시티 7층)</b>예요.",
 "<b>라멘지로 이케부쿠로</b>는 당분간 저녁(17:00–21:30, 타베로그 기준)만 영업하고 화요일에 쉬어요. 1일차 저녁에 간다면 괜찮아요.",
 "<b>돈카츠 이와이</b>는 <b>현금만 받고 예약이 안 돼요</b>. 점심 L.O. 13:45, 일요일 휴무.",
 "<b>라디오회관은 20:00에 닫아요.</b> 그 뒤엔 요도바시(22:00), 스루가야(21:00), 돈키호테(24시간).",
 "<b>마상 L.O.는 20:30</b>, <b>히키니쿠토코메는 완전 캐시리스</b>예요. 3일차 저녁은 17:00쯤이 좋아요.",
 "긴자 로프트는 <b>긴자 벨비아관</b>, GU 긴자는 마로니에게이트 긴자2 5층이에요.",
 "Q-pot 카페는 오모테산도에만 있고, 캐스키드슨 카페는 현재 없어요. \"URINAN 도라야키\"는 하라주쿠 YURINAN으로 보여요.",
]
changes = [
 ("2일차 긴자·아키하바라 배분", "원본: 긴자 오후 → 17시 긴자 저녁 → 18:30 아키하바라 / 지금: 14시 긴자 1시간 반 → 16시 아키하바라 → 20시 아키하바라 저녁", "아키하바라 가게 대부분이 20:00에 닫아서, 원본대로면 1시간 반밖에 못 봐요. 대신 긴자 저녁(하나야마·홋카이반야)은 점심 후보로만 남아요."),
 ("2일차 출발·도착 시간", "원본 09:30 출발 · 10:30 도착 → 10:00 출발 · 11:00 도착", "건담베이스가 평일 11:00에 열어서요. 원본대로 가면 30분 기다려요."),
 ("장소 순서", "지역별 '둘러볼 곳' 후보로 묶음", "순서를 정하지 않았어요. 원본 장소가 맨 위, 닫는 시간을 같이 적어 뒀어요. 이케부쿠로는 선샤인(20:00)이 가장 먼저 닫아요."),
 ("3일차 이동 경로", "원본 '롯폰기 이동' → 하마마츠초역", "돈카츠 이와이·도쿄타워는 롯폰기보다 하마마츠초·카미야초 쪽이 가까워요."),
 ("3일차 시부야 도착", "원본 14:00 → 14:30", "도쿄타워에서 이동 시간(약 30분)을 넣었어요."),
 ("점심·저녁", "가게를 고정하지 않고 후보 목록으로", "원본에 있던 곳이 맨 위, 그 아래가 추천이에요. 원본 3일차 저녁은 마상·쿠우야예요."),
 ("스카이라이너·역 이동 단계", "원본에 없던 시간표·환승 단계 추가", "예약한 스카이라이너 시간과 역 출구를 적어 둔 거예요."),
 ("원본에 없던 곳", "조조지·아메요코·스루가야 본관·요도바시·마치 에큐트 등", "일정에서 빼고 장소 탭의 '근처' 칸에만 두었어요. 리뷰 추천은 '추천' 태그로 따로 표시돼요."),
 ("원본에서 못 찾은 곳", "캐스키드슨 카페", "지금 도쿄에 운영 중인 캐스키드슨 카페가 없어서 넣지 않았어요."),
]
checklist = [
 dict(k="c1", t="스카이라이너 예약", done=True), dict(k="c2", t="시부야 스카이 10/23 입장권 예매", done=True),
 dict(k="c3", t="스카이라이너 QR → 실물 티켓 교환 (공항 제2빌딩역)", done=False),
 dict(k="c4", t="ICOCA 잔액 확인 (충전은 역 발매기)", done=False), dict(k="c5", t="eSIM 등록", done=False),
 dict(k="c6", t="Visit Japan Web 등록, QR 캡처", done=False), dict(k="c7", t="히키니쿠토코메 예약 여부 결정", done=False),
 dict(k="c8", t="현금 준비 (돈카츠 이와이 · 카모토네기 · 논베이 요코초)", done=False), dict(k="c9", t="청주공항 주차 요금 확인", done=False),
 dict(k="c11", t="귀국 스카이라이너 티켓 우에노역에서 미리 교환 (3일차 밤)", done=False),
 dict(k="c12", t="교통카드 어떻게 할지 정하기", done=False),
 dict(k="c13", t="바우처 인쇄 또는 캡처 (스카이라이너 QR · 시부야 스카이 · 숙소 확인서 · 항공 e티켓)", done=False),
 dict(k="c14", t="여권 사본 1장 + 여권 사진 2장 (원본과 따로 보관 · 원본은 늘 휴대, 면세에 필요)", done=False),
]
links = [
 dict(t="스카이라이너 시간표", d="게이세이 공식", u="https://www.keisei.co.jp/keisei/tetudou/skyliner/jp/traffic/skyliner_timetable.php"),
 dict(t="건담베이스 영업안내", d="입장 제한 확인", u="https://www.gundam-base.net/news/55669.html"),
 dict(t="Visit Japan Web", d="입국 수속", u="https://services.digital.go.jp/visit-japan-web/"),
 dict(t="히키니쿠토코메 예약", d="TableCheck", u="https://www.tablecheck.com/shops/hikinikutocome/reserve"),
 dict(t="라멘지로 공지", d="영업시간 변경", u="https://www.ramen-jiro.com/information.html"),
 dict(t="숙소 정보", d="APA 우에노 에키마에", u="https://yado.knt.co.jp/st/S131006/"),
]

# 초밥 후보를 식사 칸의 "추천 (리뷰 기반)"에 합침 (없으면 새로 만듦)
for _d in days:
    for _st in _d["steps"]:
        _m = _st.get("meal")
        if _m and (_d["id"], _st["time"]) in MEAL_ADD:
            _rg = next((g for g in _m["groups"] if g.get("label") == "추천 (리뷰 기반)"), None)
            if _rg is None:
                _rg = dict(label="추천 (리뷰 기반)", keys=[]); _m["groups"].append(_rg)
            _rg["keys"] += MEAL_ADD[(_d["id"], _st["time"])]
for g in foodGroups: g["recs"] = REC_GROUPS["food"].get(g["id"], [])
for g in placeGroups: g["recs"] = REC_GROUPS["place"].get(g["id"], [])
missing = [k for k in places if k not in COORDS]
from attrs import apply as _apply_attrs
_apply_attrs(places)
from price import apply as _apply_price
_apply_price(places)
from menu import apply as _apply_menu
_apply_menu(places)
data = dict(changes=[dict(t=a, d=b, w=c) for a, b, c in changes], places=places, days=days, foodGroups=foodGroups, placeGroups=placeGroups, alerts=alerts, checklist=checklist, links=links)
tpl = open(os.path.join(HERE, "app_template.html"), encoding="utf-8").read()
out = tpl.replace("__COORDS__", json.dumps(COORDS, ensure_ascii=False)).replace("__DATA__", json.dumps(data, ensure_ascii=False))
_out = sys.argv[1] if len(sys.argv) > 1 else os.path.join("..", "index.html")
open(os.path.join(HERE, _out), "w", encoding="utf-8").write(out)
print("built", os.path.normpath(os.path.join(HERE, _out)))
print("no coords:", missing)
