from typing import List, Dict
from sys import argv
from data_miner import main_data_miner
import pickle
import urllib.parse
import requests
import bs4


def read_index_file(index_file: str):
    with open(index_file) as reader:
        indexes = reader.readlines()
    for index in range(len(indexes)):
        if indexes[index].endswith('\n'):
            indexes[index] = indexes[index].replace('\n', '')
    return indexes


def save_dict(dict, out_file: str):
    with open(out_file, 'wb') as f:
        pickle.dump(dict, f)


def get_html(base_url: str, name):
    full_url = urllib.parse.urljoin(base_url, name)
    response = requests.get(full_url)
    html = response.text
    return html


def collect_data_of_index(name: str,
                          base_url: str,
                          traffic_dict: Dict[str, Dict[str, int]],
                          index_list: List[str]):
    html = get_html(base_url, name)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    traffic_dict[name] = {}
    for p in soup.find_all("p"):
        for link in p.find_all("a"):
            target = link.get("href")
            if target in traffic_dict[name] and target in index_list:
                traffic_dict[name][target] += 1
            elif target in index_list:
                traffic_dict[name][target] = 1


def collect_all_data(base_url: str, index_file: str):
    index_list = read_index_file(index_file)
    traffic_dict: Dict[str, Dict[str, int]] = {}
    for index in index_list:
        collect_data_of_index(index, base_url, traffic_dict, index_list)
    return traffic_dict


def crawl(base_url: str, index_file: str, out_file: str):
    traffic_dict = collect_all_data(base_url, index_file)
    print(traffic_dict)
    save_dict(traffic_dict, out_file)


def read_pickle(dict_file: str):
    with open(dict_file, "rb") as f:
        d = pickle.load(f)
    return d


def iterate_page_rank(dict_list, ranks_dict: Dict):
    new_ranks: Dict[str: float] = {val:0 for val in ranks_dict}
    for i in dict_list:
        total_pointers = sum(dict_list[i].values())
        for pointer in dict_list[i]:
            new_ranks[pointer] += ranks_dict[i] * (dict_list[i][pointer] / total_pointers)
    return new_ranks


def page_rank(iterations: int, dict_file: str, out_file: str):
    dict_list: Dict[str: Dict[str: int]] = read_pickle(dict_file)
    # dict_list = {"Hogwarts": {"Harry Potter": 1}, "Harry Potter": {"Hermione Granger": 1, "Draco Malfoy": 1}, "Hermione Granger": {"Harry Potter": 1}, "Draco Malfoy": {}}
    ranks_dict: Dict[str: float] = {val:1 for val in dict_list}
    for _ in range(iterations):
        ranks_dict = iterate_page_rank(dict_list, ranks_dict)
    save_dict(ranks_dict, out_file)


def get_words_index(base_url: str, index: str, word_dict):
    html = get_html(base_url, index)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for p in soup.find_all("p"):
        content = p.text.split(' ')
        words = ["".join(e for e in words if e.isalpha()) for words in content]
        words = [word for word in words if word != '']
        for word in words:
            if word in word_dict:
                if index in word_dict[word]:
                    word_dict[word][index] += 1
                else:
                    word_dict[word][index] = 1
            else:
                word_dict[word] = {}
                word_dict[word][index] = 1
    return word_dict


def word_dict(base_url: str, index_file: str, out_file: str):
    word_dict = {}
    index_list = read_index_file(index_file)
    for index in index_list:
        get_words_index(base_url, index, word_dict)
    save_dict(word_dict, out_file)


if __name__ == "__main__":
    base_url = "https://www.cs.huji.ac.il/~intro2cs1/ex6/wiki/"
    index_file = "small_index.txt"
    out_file = "out.pickle"
    # page_rank(2, "out.pickle", "page_rank.pickle")
    # crawl(base_url, index_file, out_file)
    # get_words_index(base_url, 'Draco_Malfoy.html', {}
    print(word_dict(base_url, index_file, "word_dict.pickle"))


