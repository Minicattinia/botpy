import threading, cloudscraper, time, re, string, os, random, sys
from sty import fg, bg, ef, rs
from bs4 import BeautifulSoup
from config import *


class NekoAutoClaim(threading.Thread):
    def __init__(self, site, cookie, delay):
        threading.Thread.__init__(self)
        self.site = site
        self.cookie = cookie
        self.delay = delay
        
    def run(self):
        headers = {
        'cookie': self.cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        }       
        scraper = cloudscraper.Session()
        while True:
            r = scraper.get(self.site, headers=headers)
            soup = BeautifulSoup(r.text, "html.parser")
            succ = soup.find("div", {"class": "alert alert-success"})
            a = random.randint(77, 167)
            if soup.find("div", {"class": "alert alert-success"}) is not None:
                print(fg(a) + succ.text)
            else:
                print(fg(a) + soup.title.text+ "  Success Claim :D")
            time.sleep(self.delay)

def text_search(search_text):
    frequency = {}
    document_text = open('config.py', 'r')
    text_string = document_text.read().lower()
    match_pattern = re.findall(search_text, text_string)
    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()

    for words in frequency_list:
        #print(words, frequency[words])
        return frequency[words]
        
if __name__ == '__main__':
    def logo():
        os.system("cls||clear")
        x = random.randint(16, 224)
        print("\033[1;0H")
        print(fg(x) +  "███▄▄▄▄      ▄████████    ▄█   ▄█▄  ▄██████▄  ████████▄   ▄██████▄   ▄█        ▄█      "+ fg.rs)
        print(fg(x+1) +"███▀▀▀██▄   ███    ███   ███ ▄███▀ ███    ███ ███   ▀███ ███    ███ ███       ███       "+ fg.rs)
        print(fg(x+1) +"███   ███   ███    █▀    ███▐██▀   ███    ███ ███    ███ ███    ███ ███       ███       "+ fg.rs)
        print(fg(x+2) +"███   ███  ▄███▄▄▄      ▄█████▀    ███    ███ ███    ███ ███    ███ ███       ███       "+ fg.rs)
        print(fg(x+3) +"███   ███ ▀▀███▀▀▀     ▀▀█████▄    ███    ███ ███    ███ ███    ███ ███       ███       "+ fg.rs)
        print(fg(x+4) +"███   ███   ███    █▄    ███▐██▄   ███    ███ ███    ███ ███    ███ ███       ███       "+ fg.rs)
        print(fg(x+5) +"███   ███   ███    ███   ███ ▀███▄ ███    ███ ███   ▄███ ███    ███ ███▌    ▄ ███▌    ▄ "+ fg.rs)
        print(fg(x+4) +" ▀█   █▀    ██████████   ███   ▀█▀  ▀██████▀  ████████▀   ▀██████▀  █████▄▄██ █████▄▄██ "+ fg.rs)
        print("")
        print(fg(x + 2) + 'Express Crypto autoclaim create by Nekodoll ' + fg.rs)
        print(fg(x + 1) + '-' * 90 + fg.rs)

    def rest_time():
        for i in range(50, 0, -1):
            x = random.randint(16, 224)
            sys.stdout.write(fg(x) + "\rrest for {} seconds ".format(i))
            time.sleep(1)
            sys.stdout.flush()
            
    
    for x in range(text_search('url') ):
        #print(locals()["Url" + str(x)])
        NekoAutoClaim(locals()["Url" + str(x+1)],locals()["Cookie" + str(x+1)],locals()["Delay" + str(x+1)]).start()
    while True:
        logo()
        time.sleep(10)
        rest_time()
    
