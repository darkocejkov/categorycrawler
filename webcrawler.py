import urllib.request
import requests
from os import path, mkdir
from shutil import rmtree
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
headers = {"user-agent" : USER_AGENT}

ILL_CHARS = ['<', '>', ':', '"', '\\', '|', '?', '*']

count_q = int(input("how many queries? "))
count_r = int(input("how many results? "))
queries = []
for x in range(count_q):
    i = input(f"query {x+1}: ")
    queries.append(i)
print(queries)

if path.exists("./dataset/"):
    rmtree("./dataset/")
mkdir("./dataset/")


for x in range(count_q):
    c = 0
    print(f"query {x+1}")
    query = queries[x]
    mkdir(f'./dataset/{query}')
    query.replace(' ', "+")
    URL  = f"https://google.com/search?q={query}"

    
    resp = requests.get(URL, headers=headers)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")

    #print(soup)
    results = []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            results.append(item)

    next = soup.find(id='pnnext')
    next_link = next['href']
    
    next_page = "https://www.google.com"+next_link
    
    for x in results:
        print(f"{x}")
        url = x.get('link')
        response = requests.get(url, headers=headers)
        if resp.status_code != 200:
            continue

        filen = f"./dataset/{query}/{x.get('title')}.html"
        for ch in ILL_CHARS:
            if ch in filen:
                filen = filen.replace(ch, '')
        #print(filen)
        #urllib.request.urlretrieve(url, filename)
        
        with open(filen, 'wb') as f:
            f.write(response.content)

    resp = requests.get(next_page, headers=headers)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")

    #print(soup)
    results = []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            results.append(item)

    for x in results:
        print(f"{x}")
        url = x.get('link')
        response = requests.get(url, headers=headers)
        if resp.status_code != 200:
            continue

        filen = f"./dataset/{query}/{x.get('title')}.html"
        for ch in ILL_CHARS:
            if ch in filen:
                filen = filen.replace(ch, '')
        #print(filen)
        #urllib.request.urlretrieve(url, filename)
        
        with open(filen, 'wb') as f:
            f.write(response.content)
        # anchor = scrapeAnchor(x.get('link'), headers)
        # filename = f"./dataset/{query}/{x.get('title')}.html"
        # with open(filename, 'wb') as f:
        #     f.write(anchor)
    
