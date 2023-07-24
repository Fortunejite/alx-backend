#!/usr/bin/env python3

"""Simple helper function"""


import csv
import math
from typing import List



class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
      """Return a tuple of size two containing a start index and an end index
      corresponding to the range of indexes to return in a list for those
      particular pagination parameters."""

      start = (page - 1) * page_size
      end = page * page_size
      return (start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset (i.e. the correct
        list of rows). If the input arguments are out of range for the dataset,
        an empty list should be returned."""

        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        range = self.index_range(page, page_size)
        return self.dataset()[range[0]:range[1]]
