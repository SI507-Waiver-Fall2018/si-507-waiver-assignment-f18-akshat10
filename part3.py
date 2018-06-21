# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here

michiganDailyUrl = "https://www.michigandaily.com/"
page = requests.get(michiganDailyUrl)
html_doc = page.content
soup = BeautifulSoup(html_doc, 'html.parser')

divs = soup.find_all("div","view-most-read")



print("Michigan Daily -- MOST READ")
mostReadDiv = soup.find("div", attrs={'class' : 'view-most-read'}).find("ol").find_all("li")
for item in mostReadDiv:

    print(item.find("a").text.strip())

    try:
        chotaSoup = BeautifulSoup(requests.get(michiganDailyUrl+item.find("a")['href']).content, 'html.parser')
        print("By "+ chotaSoup.find("div", attrs = {"class" : "byline"}).find('div').find('a').text.strip())
    except Exception as e:
        print("No byline author found!")

    # print ("\n")
