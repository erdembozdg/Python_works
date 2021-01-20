
from bs4 import BeautifulSoup
import urllib3

def get_counter(text):
    return [item for item in text.split()]

def web_resource(url):
    http = urllib3.PoolManager()
    r = http.request("GET", url)
    bs = BeautifulSoup(r.data, 'lxml')
    return get_counter(bs.text)

if __name__ == '__main__':

    total_words = list()
    unique_words = set()

    for word in web_resource('https://www.globalrelay.com'):
        if word not in unique_words:
            unique_words.add(word)
        total_words.append(word)
    print("Number of total words: {}".format(len(unique_words)))
    print("Number of total words: {}".format(len(total_words)))

