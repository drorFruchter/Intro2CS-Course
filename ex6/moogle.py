from typing import List, Dict
from sys import argv
from data_miner import main_data_miner
import pickle


# works
def crawl(base_url: str, index_file: str, out_file: str):
    main_data_miner(base_url, index_file, out_file)


"""
- Read index_list pickle
- Create a dict of all index_list with value 1
- Create a new dict of 0's to input all the new values.
for every Iteration:
    - Create a new dict of 0's to input all the new values.
    for every index:
        - share points (by the formula)
- Save pickle
"""
# works
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

# Double coded - also in data_miner.py
def save_dict(dict, out_file: str):
    with open(out_file, 'wb') as f:
        pickle.dump(dict, f)


def page_rank(iterations: int, dict_file: str, out_file: str):
    dict_list: Dict[str: Dict[str: int]] = read_pickle(dict_file)
    # dict_list = {"Hogwarts": {"Harry Potter": 1}, "Harry Potter": {"Hermione Granger": 1, "Draco Malfoy": 1}, "Hermione Granger": {"Harry Potter": 1}, "Draco Malfoy": {}}
    ranks_dict: Dict[str: float] = {val:1 for val in dict_list}
    for _ in range(iterations):
        ranks_dict = iterate_page_rank(dict_list, ranks_dict)
    save_dict(ranks_dict, out_file)



if __name__ == "__main__":
    base_url = "https://www.cs.huji.ac.il/~intro2cs1/ex6/wiki/"
    index_file = "small_index.txt"
    out_file = "out.pickle"
    page_rank(2, "out.pickle", "page_rank.pickle")


