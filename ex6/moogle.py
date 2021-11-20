#################################################################
# FILE : moogle.py
# WRITER : eyal , eyalmutzary , 206910432
# EXERCISE : intro2cs ex6 2021
# DESCRIPTION: moogle search engine
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED: W3School
# NOTES: ...
#################################################################

from typing import List, Dict
from sys import argv
import pickle
import urllib.parse
import requests
import bs4
from collections import OrderedDict


def read_index_file(index_file: str):
    """
        reads the index file
        :param index_file - the name of the file to read
        :return a list of indexes
    """
    with open(index_file) as reader:
        indexes = reader.readlines()
    for index in range(len(indexes)):
        if indexes[index].endswith('\n'):
            indexes[index] = indexes[index].replace('\n', '')
    return indexes


def save_dict(dict, out_file: str):
    """
        Saves a dict to an out_file
        :param dict - the dict to save
        :param out_file - the directory to save
    """
    with open(out_file, 'wb') as f:
        pickle.dump(dict, f)


def get_html(base_url: str, name):
    """
        Sends a request to a website, and get its html
        :param base_url - the base url of the site
        :param name - the index in the site
        :return the HTML of the page
    """
    full_url = urllib.parse.urljoin(base_url, name)
    response = requests.get(full_url)
    html = response.text
    return html


def collect_data_of_index(name: str,
                          base_url: str,
                          traffic_dict: Dict[str, Dict[str, int]],
                          index_list: List[str]):
    """
        Collects the traffic dictionary of an index
        :param base_url - the base url of the site
        :param name - the index in the site
        :param traffic_dict - a dictionary of all the traffic of the indexes
        :param index_list - the list of the indexes
        :return a traffic dictionary of a single index in the list
    """
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
    """
        Collects the traffic dictionary of all the indexes
        :param base_url - the base url of the site
        :param index_file - filename of the index file
        :return a traffic dictionary of all the indexes in the list
    """
    index_list = read_index_file(index_file)
    traffic_dict: Dict[str, Dict[str, int]] = {}
    for index in index_list:
        collect_data_of_index(index, base_url, traffic_dict, index_list)
    return traffic_dict



def crawl(base_url: str, index_file: str, out_file: str):
    """
       Activates the crawl algorithm
       :param base_url - the base url of the site
       :param index_file - filename of the index file
       :param out_file - the output filename
   """
    traffic_dict = collect_all_data(base_url, index_file)
    save_dict(traffic_dict, out_file)


# ------- Part 2 ---------


def read_pickle(dict_file: str):
    """
       Reads a pickle
       :param dict_file - pickle filename
       :return The pickle content
   """
    with open(dict_file, "rb") as f:
        d = pickle.load(f)
    return d


def iterate_page_rank(dict_list, ranks_dict: Dict):
    """
        Goes through a single iteration for page ranking
        :param dict_list - dict list
        :param ranks_dict - a dictionary of all the rankings
        :return an updated ranking dictionary
   """
    new_ranks: Dict[str: float] = {val:0 for val in ranks_dict}
    for i in dict_list:
        total_pointers = sum(dict_list[i].values())
        for pointer in dict_list[i]:
            new_ranks[pointer] += ranks_dict[i] * (dict_list[i][pointer] / total_pointers)
    return new_ranks


def page_rank(iterations: int, dict_file: str, out_file: str):
    """
       Goes through the page rank algorithm
       :param iterations - the amount of iteration to calculate
       :param dict_file - filename of the dict file
       :param out_file - output filename
   """
    dict_list: Dict[str: Dict[str: int]] = read_pickle(dict_file)
    ranks_dict: Dict[str: float] = {val:1 for val in dict_list}
    for _ in range(iterations):
        ranks_dict = iterate_page_rank(dict_list, ranks_dict)
    save_dict(ranks_dict, out_file)


# ------- Part 3 ---------


def get_words_index(base_url: str, index: str, word_dict):
    """
       Gets all waords from a certain index
       :param base_url - the base url of the site
       :param index - the index of the page
       :param word_dict - a dictionary of all the words from past collections
       :return an updated word_dict
   """
    html = get_html(base_url, index)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for p in soup.find_all("p"):
        words = p.text.split(' ')
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
    """
       Goes throuhg the word_dict algorithm
       :param base_url - the base url of the site
       :param index_file - filename of the index file
       :param out_file - output filename
   """
    word_dict = {}
    index_list = read_index_file(index_file)
    for index in index_list:
        get_words_index(base_url, index, word_dict)
    save_dict(word_dict, out_file)

# ------- Part 4 ---------


def sort_dict(ranking_dict):
    """
        Sorts a dictionary of the type [str: float] - biggest value top
       :param ranking_dict - the ranking dictionary
       :return an updated dictionary
   """
    sorted_dict = [(index, ranking_dict[index]) for index in ranking_dict]
    if len(sorted_dict) <= 1:
        return ranking_dict
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(sorted_dict)-1):
            if sorted_dict[i+1][1] > sorted_dict[i][1]:
                sorted_dict[i+1], sorted_dict[i] = sorted_dict[i], sorted_dict[i+1]
                is_sorted = False
    return dict(sorted_dict)


def write_result(results_dict):
    """
       prints and writes the result to a txt file
       :param results_dict - the search result dictionary
   """
    txt = ""
    for word in results_dict:
        txt += word + " " + str(results_dict[word]) + "\n"
    print(txt, end='')
    txt += "*" * 10 + "\n"
    with open('results.txt', 'a') as f:
        f.write(txt)


def search(query: str,
           ranking_dict_file: str,
           words_dict_file: str,
           max_results: int):
    """
       Goes through the search algorithm and prints it
       :param query - the search query (string)
       :param ranking_dict_file - a dictionary of the ranking of the indexes
       :param words_dict_file - a dictionary of all the words
       :param max_results - the amount of max results to show
   """
    ranking_dict = read_pickle(ranking_dict_file)
    words_dict = read_pickle(words_dict_file)
    sorted_ranking_dict = sort_dict(ranking_dict)
    result_counter = 0
    result_dict = {}
    query = query.split(" ")
    new_query = []
    for word in range(len(query)):
        if query[word] in words_dict:
            new_query.append(query[word])

    for index in sorted_ranking_dict:
        occurence_list = []
        for word in new_query:
            if word in words_dict:
                if index in words_dict[word]:
                    occurence_list.append(words_dict[word][index])
            else:
                break

        if len(occurence_list) == len(new_query):
            result_dict[index] = min(occurence_list) * sorted_ranking_dict[index]
            result_counter += 1
        if result_counter == max_results:
            break

    result_dict = sort_dict(result_dict)
    write_result(result_dict)


def main():
    """
       Handles the terminal inputs
   """
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
    main()
