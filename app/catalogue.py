from collections import defaultdict
import json

DATA_PATH = "./data/catalogue.json"


class Catalogue:
    def __init__(self):
        self._data = None

    @property
    def data(self):
        if not self._data:
            self._load_data()
        return self._data

    def _load_data(self):
        """
        load/reload catalogue data into self._data by loading json in DATA_PATH
        """
        loaded_data = json.load(open(DATA_PATH))
        self._data = loaded_data or {}

    def calculate_discount(self, id, count) -> int:
        """
        Calculate discount for an item with id given a total number that item
        :param id: id of item
        :type id: str
        :param count: repetitions of given id to calculate discount based on if exists
        :type count: int
        :return: discounted price for items
        :type return: int
        """
        watch_info = self.data.get(id, {})
        if not watch_info:
            raise KeyError(f"Id {id} does not exist")

        if watch_info.get("discount", 0) and count == watch_info["discount"][0]:
            return watch_info["discount"][1]

        return 0

    def calculate_final_price(self, item_ids: list) -> int:
        """
        Calculate total final price of items including discounts if available given list of ids
        :param id: id of item
        :type id: str
        :return: total price
        :type return: int
        """
        final_price = 0
        watches_count = defaultdict(int)
        for id in item_ids:
            if id in self.data:  # TODO validate in a better way
                watches_count[id] += 1

                discounted_price = self.calculate_discount(id, watches_count[id])
                if discounted_price:
                    watches_count[id] = 0
                    final_price += discounted_price

        if watches_count:
            for id in watches_count:
                final_price += self.data[id]["price"] * watches_count[id]

        return final_price
