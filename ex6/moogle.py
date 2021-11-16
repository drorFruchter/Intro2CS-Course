from typing import List, Dict
from sys import argv
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


# ------- Part 2 ---------


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


# ------- Part 3 ---------


def get_words_index(base_url: str, index: str, word_dict):
    html = get_html(base_url, index)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for p in soup.find_all("p"):
        words = p.text.split(' ')
        # words = ["".join(e for e in words if e.isalpha()) for words in content]
        # words = [word for word in words if word != '']
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


# ------- Part 4 ---------


def sort_dict(ranking_dict):
    sorted_dict: Dict[str: float] = {}
    values = list(ranking_dict.values())
    values.sort()
    values.reverse()
    for i in values:
        sorted_dict[list(ranking_dict.keys())\
                    [list(ranking_dict.values()).index(i)]] = i
    return sorted_dict


def write_result(results_dict):
    txt = ""
    for word in results_dict:
        txt += word + " " + str(results_dict[word]) + "\n"
    txt += "*" * 10 + "\n"
    with open('results.txt', 'a') as f:
        f.write(txt)


def search(query: str,
           ranking_dict_file: str,
           words_dict_file: str,
           max_results: int):
    ranking_dict = read_pickle(ranking_dict_file)
    words_dict = read_pickle(words_dict_file)
    sorted_ranking_dict = sort_dict(ranking_dict)
    result_counter = 0
    result_dict = {}
    query = query.split(" ")
    for index in sorted_ranking_dict:
        occurence_list = []
        for word in query:
            if word in words_dict:
                if index in words_dict[word]:
                    occurence_list.append(words_dict[word][index])
            else:
                break

        if len(occurence_list) == len(query):
            result_dict[index] = min(occurence_list) * sorted_ranking_dict[index]
            result_counter += 1
        if result_counter == max_results:
            break

    result_dict = sort_dict(result_dict)
    write_result(result_dict)


def main():
    if argv[1] == "crawl":
        base_url, index_file, out_file = argv[2:]
        crawl(base_url, index_file, out_file)

    elif argv[1] == "page_rank":
        iterations, dict_file, out_file = argv[2:]
        page_rank(int(iterations), dict_file, out_file)

    elif argv[1] == "words_dict":
        base_url, index_file, out_file = argv[2:]
        word_dict(base_url, index_file, out_file)

    elif argv[1] == "search":
        query, ranking_dict_file, words_dict_file, max_results = argv[2:]
        search(query, ranking_dict_file, words_dict_file, int(max_results))


if __name__ == "__main__":
    # base_url = "https://www.cs.huji.ac.il/~intro2cs1/ex6/wiki/"
    # index_file = "small_index.txt"
    # out_file = "out.pickle"
    main()
    # page_rank(2, "out.pickle", "page_rank.pickle")
    # crawl(base_url, index_file, out_file)
    # get_words_index(base_url, 'Draco_Malfoy.html', {}
    # print(word_dict(base_url, index_file, "word_dict.pickle"))
    # search("scar", "page_rank.pickle", "word_dict.pickle", 5)
