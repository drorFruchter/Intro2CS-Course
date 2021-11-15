import urllib.parse
from typing import List, Dict
import requests
import bs4
import pickle


def read_index_file(index_file: str):
    with open(index_file) as reader:
        indexes = reader.readlines()
    for index in range(len(indexes)):
        if indexes[index].endswith('\n'):
            indexes[index] = indexes[index].replace('\n', '')
    return indexes


def collect_data_of_index(name: str, base_url: str, traffic_dict: Dict[str, Dict[str, int]]):
    full_url = urllib.parse.urljoin(base_url, name)
    response = requests.get(full_url)
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    traffic_dict[name] = {}
    for p in soup.find_all("p"):
        for link in p.find_all("a"):
            target = link.get("href")
            if target in traffic_dict[name] and target != '':
                traffic_dict[name][target] += 1
            elif target != '':
                traffic_dict[name][target] = 1


def collect_all_data(base_url: str, index_file: str):
    index_list = read_index_file(index_file)
    # index_list = ["Albus_Dumbledore.html"]
    traffic_dict: Dict[str, Dict[str, int]] = {}
    for index in index_list:
        collect_data_of_index(index, base_url, traffic_dict)
    return traffic_dict


def save_dict(traffic_dict: Dict[str, Dict[str,int]], out_file: str):
    with open(out_file, 'wb') as f:
        pickle.dump(traffic_dict, f)


def main_data_miner(base_url: str, index_file: str, out_file: str):
    traffic_dict = collect_all_data(base_url, index_file)
    save_dict(traffic_dict, out_file)