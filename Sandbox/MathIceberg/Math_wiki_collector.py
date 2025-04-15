import pandas as pd
import requests
import time
import wikipedia as wk
from bs4 import BeautifulSoup as BS
from math import log, e, sqrt
from pylatexenc.latex2text import LatexNodes2Text
from selenium import webdriver
from selenium.common import exceptions as sel_exs
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from wikipedia import exceptions as wkex


# print(data['Fact/event'][119:])
def find_articles(file: str):
    ef = pd.read_excel("my_icebergs\Iceberg_math.xlsx", 'Математика')
    data = pd.DataFrame(ef, columns=['Fact/event',
                                     'Известность (в тысячах)',
                                     'Ссылки'])
    
    f = open(file, 'w', encoding='utf-8')
    for fact in data['Fact/event']:
        print(fact, ':', end=' ', file=f)
        
        while True:
            try:
                res = wk.search(fact, 5)
                if not res:
                    print(fact, ':', None)
                    print(None, file=f)
                else:
                    print(*res, sep=', ', file=f)
                    print(fact, ':', res[0])
                
                break
            except (TimeoutError, requests.exceptions.ConnectTimeout,
                    requests.exceptions.ConnectionError):
                continue


# fin = open('math_list.txt', 'r', encoding='utf-8')
# fout = open('math_list_new.txt', 'w', encoding='utf-8')

def get_links(f1, f2):
    with open(f1, 'r', encoding='utf-8') as fin:
        with open(f2, 'a', encoding='utf-8') as fout:
            for line in fin.readlines()[1666:]:
                entry, title = line.split(' : ')
                print(entry, end=' : ')
                
                if title.strip() == 'None':
                    print("None")
                    print(entry, ":", None, file=fout)
                    continue
                
                try:
                    wkpg = wk.page(title=title.strip())
                except (wkex.PageError, wkex.DisambiguationError):
                    print('None')
                    print(entry, ':', None, file=fout)
                    continue
                
                catg = wkpg.categories
                if len(catg) > 8:
                    catg = catg[:8]
                
                print(wkpg.url, ':', end=' ', file=fout)
                print(*catg, sep=', ', file=fout)
                print('success')


def delete_garbage(f1, f2):
    fin = open(f1, 'r', encoding='utf-8')
    fout = open(f2, 'w', encoding='utf-8')
    dellist = ['articles',
               'short description is different from wikidata', 'cs1',
               'all pages needing cleanup', 'introductions',
               'short description matches wikidata',
               'commons category link is on wikidata',
               'webarchive template wayback links', 'page']
    
    for line in fin.readlines():
        link, cats = line.split(' : ')
        cats = cats.strip().lower()
        print(link, ':', end='', file=fout)
        if cats == 'none':
            print(' None', file=fout)
            continue
        
        printed = 0
        for cat in cats.split(', '):
            available_cat = True
            for delitem in dellist:
                if delitem in cat:
                    available_cat = False
                    break
            
            if available_cat:
                printed += 1
                print(' ', cat.title(), sep='', end=',', file=fout)
        
        if printed == 0:
            print(' None', end='', file=fout)
        
        print(file=fout)


def get_querys_results(query):
    query = query.replace(' ', '+')
    USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36")
    URL = f"https://google.com/search?q={query}"
    
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)
    
    alive = True
    while alive:
        if resp.status_code == 200:
            soup = BS(resp.content, "html.parser")
            soup.select("#result-stats")
            for t in soup.select("#result-stats"):
                if 'Результатов' in t.text:
                    tt = t.text.replace(' примерно', '')
                    _, tt = tt.split(":", 1)
                    tt, _ = tt.split('(', 1)
                    tt = tt.replace(' ', '').replace(" ", '')
                    return int(tt)
            
            alive = False


def write_popularity(links_file, names_file):
    f1 = open(links_file, 'r', encoding='utf-8')
    f2 = open(names_file, 'r', encoding='utf-8')
    f3 = open('popty.txt', 'a')
    
    for i, (line1, line2) in enumerate(zip(f1.readlines(),
                                           f2.readlines())):
        line1 = line1.strip()
        line2 = line2.strip()
        q, _ = line1.split(" : ")
        if i >= 0:  # i != 226:
            _, q = q.rsplit("/", 1)
            if '#' in q:
                q, _ = q.split('#')
            
            q = q.replace('_', ' ')
            if ' (' in q:
                _, q = q.rsplit(' (', 1)
                res = get_querys_results(line2 + ' (' + q)
                print(res, file=f3)
                print(res, end='   ')
                print(line2, '(' + q)
            else:
                res = get_querys_results(line2)
                print(res, file=f3)
                print(res, end='   ')
                print(line2)
        else:
            res = get_querys_results(q + " meme")
            print(res, file=f3)
            print(res, end='   ')
            print(q)


all_tags = ['Functions', 'Numbers', 'Large numbers',
            'Probability theory', 'Geometry', 'Linear algebra',
            'Algebra', 'Series', 'Analysis', 'Calculus',
            'Mathematical constants', 'Curves', 'Tensors', 'Surfaces',
            'Paradoxes', 'Applied math', 'Infinity',
            'Unsolved problems', 'Other', 'Area of math',
            'Complex analysis', 'Spaces', 'Plane geometry', 'Topology',
            'Manifolds', 'Fractals', 'Sets', 'Identities', 'Theorems',
            'Graph theory', 'Problems', 'Functional analysis',
            'Conjectures', 'Group theory', 'Differential equations',
            'Chaos theory', 'Combinatorics', 'Mathematical logic',
            'Sequences', 'Discrete math', 'Lemmas', 'Arithmetics',
            'Measure theory', 'Operators', 'History', 'Equations',
            'Operations', 'Visualization', 'Coordinate systems',
            'Solid geometry', 'Inequalities', 'Boolean algebra',
            'Axioms', 'Statistics', 'Polygons',
            'Multi-dimensional geometry', 'Polyhedrons', 'Notation',
            'Transforms', 'Polytopes']


def check_correctness(links_file):
    f1 = open(links_file, 'r', encoding='utf-8')
    
    for i, line in enumerate(f1.readlines()):
        if ' : ' not in line:
            print(i + 1, 'string hasn\'t " : " separate symbols')
            continue
        
        link, cats = line.split(' : ')
        cats = list(map(lambda c: c.strip(), cats.split(', ')))
        
        if len(cats) > 4:
            print(f"Entry at line {i + 1} has excess categories: ",
                  end='')
            print(*cats, sep=', ')
            continue
        
        for cat in cats:
            if cat.endswith(','):
                print(cat, f"line {i + 1} has comma")
                continue
            
            if cat not in all_tags:
                print(cat, ":", i + 1, "line")
                # unique.append(cat)


categories = ['Numbers', 'Geometry', 'Algebra', 'Analysis', 'Other',
              'Applied math', 'Area of math', 'Topology',
              'Mathematical logic', 'Discrete math', 'Visualization',
              'Notation', 'Sets', 'Chaos theory', ]
subcategories = {'Tensors': 'Algebra', 'Large numbers': "Numbers",
                 'Probability theory': 'Applied math',
                 'Linear algebra': 'Algebra', 'Calculus': 'Analysis',
                 'Surfaces': 'Geometry', 'Infinity': "Numbers",
                 'Complex analysis': "Analysis",
                 'Plane geometry': 'Geometry',
                 'Graph theory': "Discrete math",
                 'Functional analysis': "Analysis",
                 'Group theory': "Algebra",
                 'Differential equations': "Analysis",
                 'Combinatorics': "Discrete math",
                 'Arithmetics': "Numbers", 'Measure theory': "Analysis",
                 'Coordinate systems': "Geometry",
                 'Solid geometry': "Geometry", 'Manifolds': "Topology",
                 'Boolean algebra': "Mathematical logic",
                 'Statistics': "Applied math", 'Polygons': "Geometry",
                 'Multi-dimensional geometry': "Geometry",
                 'Polyhedrons': "Geometry", 'Polytopes': "Geometry"}
abs_categories = ['Functions', 'Series', 'Mathematical constants',
                  'Curves', 'Paradoxes', 'Unsolved problems', 'Spaces',
                  'Fractals', 'Identities', 'Theorems', 'Problems',
                  'Conjectures', 'Sequences', 'Operators', 'History',
                  'Equations', 'Operations', 'Inequalities', 'Axioms',
                  'Transforms']


def fill_in_gaps(links_file, new_links_file):
    f1 = open(links_file, 'r', encoding='utf-8')
    f2 = open(new_links_file, 'w', encoding='utf-8')
    
    for i, line in enumerate(f1.readlines()):
        link, cats = line.split(' : ')
        cats = list(map(lambda c: c.strip(), cats.split(', ')))
        tcats = list(filter(lambda c: c not in abs_categories, cats))
        if not (any(c in tcats for c in categories)
                or any(c in tcats for c in subcategories.keys())):
            print("There are only abstract categorise. Line",
                  i + 1, end='\t(')
            print(*cats, sep=', ', end='')
            print(')')
        
        mcats = [c for c in tcats if c in categories]
        if len(mcats) > 1:
            print("There are more then 1 main category. Line",
                  i + 1, end='\t(')
            print(*mcats, sep=', ', end='')
            print(')')
        elif len(mcats) == 0:
            # print("There aren't any main category. Line",
            #       i + 1, end='\t(')
            # print(*cats, sep=', ', end='')
            # print(')')
            scats = list({subcategories[c] for c in cats
                          if c in subcategories.keys()})
            if len(scats) == 1:
                print(link, ':', end=' ', file=f2)
                print(*cats, scats[0], sep=', ', file=f2)
            elif len(scats) > 1:
                print(f"There are {len(scats)} possible main categories"
                      f" for line {i + 1} {link}")
                print(*scats, sep=' | ')
                j = int(input()) - 1
                print(link, ':', end=' ', file=f2)
                print(*cats, scats[j], sep=', ', file=f2)
        else:
            print(link, ':', end=' ', file=f2)
            print(*cats, sep=', ', file=f2)


def write_sorted_links(links_file, new_links_file):
    f1 = open(links_file, 'r', encoding='utf-8')
    f2 = open(new_links_file, 'w', encoding='utf-8')
    
    for i, line in enumerate(f1.readlines()):
        link, cats = line.split(' : ')
        cats = list(map(lambda c: c.strip(), cats.split(', ')))
        
        mcat = [c for c in cats if c in categories][0]
        scats = list(filter(lambda c: c in subcategories.keys(), cats))
        abscats = list(filter(lambda c: c in abs_categories, cats))
        print(link, ":", end=" ", file=f2)
        print(mcat, *scats, *abscats, sep=', ', file=f2)


difclty = {'Numbers': 3, 'Geometry': 5, 'Algebra': 5, 'Analysis': 7,
           'Other': 6, 'Applied math': 8, 'Area of math': 4,
           'Topology': 9, 'Mathematical logic': 7, 'Discrete math': 6,
           'Visualization': 5, 'Notation': 6, 'Sets': 6,
           'Chaos theory': 10,  # Areas of math
           'Tensors': 8, 'Large numbers': 7, 'Probability theory': 7,
           'Linear algebra': 7, 'Calculus': 7, 'Surfaces': 7,
           'Infinity': 8, 'Complex analysis': 9, 'Plane geometry': 4,
           'Graph theory': 6, 'Functional analysis': 7,
           'Group theory': 6, 'Differential equations': 8,
           'Combinatorics': 6, 'Arithmetics': 2, 'Measure theory': 6,
           'Coordinate systems': 4, 'Solid geometry': 5, 'Manifolds': 7,
           'Boolean algebra': 5, 'Statistics': 9, 'Polygons': 4,
           'Multi-dimensional geometry': 9, 'Polyhedrons': 5,
           'Polytopes': 6,  # Subcategories
           'Functions': 5, 'Series': 8, 'Mathematical constants': 4,
           'Curves': 6, 'Paradoxes': 7, 'Unsolved problems': 10,
           'Spaces': 7, 'Fractals': 8, 'Identities': 4, 'Theorems': 7,
           'Problems': 5, 'Conjectures': 7, 'Sequences': 5,
           'Operators': 7, 'History': 5, 'Equations': 5,
           'Operations': 3, 'Inequalities': 6, 'Axioms': 6,
           'Transforms': 8}  # Abstract categories


def diftrans(*args):
    mc = difclty[list(filter(lambda c: c in categories, args))[0]]
    scs = sum(difclty[c]
              for c in filter(lambda c: c not in categories, args))
    if scs == 0:
        print("1=", end=' ')
        return 2 * mc * log(mc, e)
    
    a = log(10, e) / sqrt(30)
    return mc * e ** (a * sqrt(scs))


def complexity_difiner(links_file):
    f1 = open(links_file, 'r', encoding='utf-8')
    f2 = open('difty.txt', 'w')
    
    browser = webdriver.Chrome(".wdm\drivers\\chromedriver\win64\\115.0.5790.173\\chromedriver.exe")
    browser.get("http://www.roadtogrammar.com/textanalysis/")
    
    for line in f1.readlines():
        link, cats = line.split(';')
        if 'wikipedia' not in link:  # обработать отдельно
            print("Ahhhhhh! Oshibka, stop nol, nol, nol, nol, nol!!!")
            print(-1000, file=f2)
            continue
    
        textarea = (WebDriverWait(browser, 10)
                    .until(EC.element_to_be_clickable(
                     (By.CSS_SELECTOR, '#tx'))))
        submit = (WebDriverWait(browser, 10)
                  .until(EC.element_to_be_clickable(
                   (By.CSS_SELECTOR, '#butang1'))))
    
        wkar = requests.get(link)
        hahatml = BS(wkar.content, 'html.parser')
        header = hahatml.select_one('#firstHeading').text
        print(link, end=' => ')
        print(header)
        if '#' not in link:
            summary = wk.page(header, auto_suggest=False).summary
        else:
            _, sec = link.split('#', 1)
            sec = sec.replace('_', ' ')
            summary = (wk.page(header, auto_suggest=False).section(sec))
    
        while '\n ' in summary or '  ' in summary:
            summary = summary.replace('\n ', ' ').replace('  ', ' ')
    
        summary = LatexNodes2Text().latex_to_text(summary)
        if summary.count(' ') > 124:
            summary = ' '.join(summary.split()[:125])
    
        # print(summary)
        try:
            textarea.send_keys(summary)
        except sel_exs.WebDriverException:
            print("Oh no! Oh no! Oh on no no no no!")
            print(-1000, file=f2)
            continue
        
        try:
            submit.click()
        except Exception:
            browser.execute_script("arguments[0].click();", submit)
    
        # Извлекаем нужную информацию
        html = BS(browser.page_source, 'html.parser')
        while html.select_one('#contentArea') is None:
            time.sleep(1)
            html = BS(browser.page_source, 'html.parser')
    
        info = html.select_one('#contentArea').text.split('\n')[-1]
        ioio = info.index('word complexity: ') + 18
        jojo = ioio
        for j in range(ioio, len(info)):
            if info[j].isalpha():
                jojo = j
                break
    
        print(int(info[ioio:jojo]))
        print(int(info[ioio:jojo]), file=f2)
        # input()
        # тыкаем по кнопке для перехода на поле ввода нового текста
        new_text = (WebDriverWait(browser, 10)
                    .until(EC.element_to_be_clickable(
                     (By.CSS_SELECTOR, '#butang3'))))
    
        try:
            new_text.click()
        except Exception:
            browser.execute_script("arguments[0].click();", new_text)
    
    browser.close()
