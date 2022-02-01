from collections import defaultdict


class Catalogue:
    def __init__(self):
        self._data = None

    @property
    def data(self):
        if not self._data:
            self._data = self._load_data()
        return self._data

    def _load_data(self) -> dict:
        # TODO read data catalogue.json into catalogue
        loaded_data = {
            "001": {"name": "Rolex", "price": 100, "discount": (3, 200)},
            "002": {"name": "Michael Kors", "price": 80, "discount": (2, 120)},
        }
        return loaded_data

    def calculate_discount(self, id, count) -> int:
        watch_info = self.data.get(id, {})
        if not watch_info:
            raise KeyError(f"Id {id} does not exist")

        if watch_info["discount"] and count == watch_info["discount"][0]:
            return watch_info["discount"][1]

        return 0

    def calculate_final_price(self, item_ids: list) -> int:
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
