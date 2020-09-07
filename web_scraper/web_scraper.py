import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):

    page = requests.get(url)

    soup = BeautifulSoup(page.content,'html.parser')

    result = soup.find('div', id = 'bodyContent')

    all_citations = result.find_all('p')
    text = []
    for i in all_citations:
        try:
            val = i.find_all('sup',class_= 'noprint Inline-Template Template-Fact')
            if val:
                for j in val:
                    text.append(j)
        except AttributeError as e:
            continue

    return len(text)

print(get_citations_needed_count('https://en.wikipedia.org/wiki/Petra'))



def get_citations_needed_report(url):

    page = requests.get(url)

    soup = BeautifulSoup(page.content,'html.parser')

    result = soup.find('div', id = 'bodyContent')
    all_citations = result.find_all('p')

    para_lst = []
    for i in all_citations:
        try:
            axz = i.find_all('span',string = lambda text: 'citation needed' in text.lower())
            if axz:
                for j in axz:
                    para_lst.append(i.text)
                    pos = i.text.index('citation')
                    qut = i.text[:pos-1]
                    stop = qut.split('. ')
                    para_lst.append(stop[-1])
        except AttributeError as e:
            continue

    
    for i in para_lst:
        print(i)

    return para_lst


get_citations_needed_report('https://en.wikipedia.org/wiki/Petra')