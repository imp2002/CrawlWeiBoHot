from requests_html import HTMLSession
import time

session = HTMLSession()
pa = session.get('https://s.weibo.com/top/summary')

def crawlWeiBoHot(i):
    phi = '#pl_top_realtimehot > table > tbody > tr:nth-child('+str(i)+') > td.td-02 > a'
    contain = pa.html.find(str(phi), first = True)
    with open(f"WbHot-{time.strftime('%Y-%m-%d')}.txt", "a+") as wb :
        wb.write(str(i)+'   '+contain.text+'\n')

for i in range(1, 51):
    crawlWeiBoHot(i)