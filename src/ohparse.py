import re
DAYS="월화수목금토일"
def tm(s):
    h,m=s.split(":"); return int(h)*60+int(m)
def ranges(txt):
    out=[]
    for a,b in re.findall(r'(\d{1,2}:\d{2})\s*[–\-~]\s*(?:익일\s*)?(\d{1,2}:\d{2})', txt):
        o,c=tm(a),tm(b)
        if c<=o: c+=1440
        out.append([o,c])
    return out
def parse(hours, closed=""):
    h=hours or ""
    if not h.strip(): return None
    if re.search(r'24시간|상시 개방', h) and not ranges(h): return [[[0,1440]]]*7
    # weekday-specific "평일 ..." and "토·일 ..." segments
    week=[None]*7
    segs=re.split(r'\s*[/|]\s*|\s·\s(?=(?:토|일|평일|주말|월|화|수|목|금))', h)
    base=ranges(re.sub(r'\(.*?\)','',h.split(" · 저녁")[0])) if False else None
    r=ranges(re.sub(r'L\.?O\.?\s*\d{1,2}:\d{2}','',h))
    # drop L.O. and parenthetical last-entry noise
    clean=re.sub(r'\((?:L\.O\.|최종|입장|주문)[^)]*\)','',h)
    r=ranges(clean)
    if not r: return None
    week=[r]*7
    # closed weekdays
    for i,dch in enumerate(DAYS):
        if re.search(dch+r'요일', closed) or re.search(r'(^|[·,\s])'+dch+r'(?=[·,\s]|$)', closed.replace("휴무","")) and "째" not in closed:
            week[i]=[]
    m=re.search(r'([월화수목금토일](?:·[월화수목금토일])*)\s*휴무', hours+" "+closed)
    if m:
        for dch in m.group(1).split("·"): week[DAYS.index(dch)]=[]
    return week
