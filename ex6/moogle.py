from typing import List, Dict
from sys import argv
from data_miner import main_data_miner



if __name__ == "__main__":
    base_url = "https://www.cs.huji.ac.il/~intro2cs1/ex6/wiki/"
    index_file = "small_index.txt"
    out_file = "out.pickle"
    # main_data_miner(base_url, index_file, out_file)