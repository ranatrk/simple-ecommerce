from gettext import Catalog
import pytest
import json
from catalogue import Catalogue


@pytest.mark.parametrize("path", ["", "test/valid_catalogue.json"])
def test_load_data_valid(path):
    """
    cases: _load_data()
    - load default data
    - load custom valid json
    """
    catalogue = Catalogue()
    if not path:
        catalogue._load_data()
    else:
        catalogue._load_data(path)
    assert catalogue.data


@pytest.mark.parametrize("path,expected", [("test/invalid_catalogue.json", json.JSONDecodeError)])
def test_load_data_invalid(path, expected):
    """
    cases: _load_data()
    - load custom invalid json
    """
    catalogue = Catalogue()
    with pytest.raises(json.JSONDecodeError):
        catalogue._load_data(path)


@pytest.mark.parametrize("id, count, expected", [("001", 2, 0), ("001", 3, 200), ("001", 0, 0)])
def test_calculate_discount_valid(id, count, expected):
    """
    cases: calculate_discount(id, count)
    - id in catalogue and count +ve value - no discount
    - id in catalogue and count +ve value - discount
    - count 0
    """
    catalogue = Catalogue()
    if isinstance(expected, int):
        assert catalogue.calculate_discount(id, count) == expected


@pytest.mark.parametrize("id, count, expected", [("123", 3, KeyError), ("002", -1, RuntimeError)])
def test_calculate_discount_invalid(id, count, expected):
    """
    cases: calculate_discount(id, count)
    - id not in catalogue
    - count -ve 
    """
    catalogue = Catalogue()

    with pytest.raises(expected):
        catalogue.calculate_discount(id, count)


@pytest.mark.parametrize(
    "item_ids,expected",
    [
        ([], 0),
        (["001"], 100),
        (["001", "001"], 200),
        (["001", "001", "001", "002"], 280),
        (["001", "001", "001", "001", "001", "001"], 400),
        (["001", "001", "001", "002", "002"], 320),
    ],
)
def test_calculate_final_price_valid(item_ids, expected):
    """
    cases: calculate_final_price(item_ids: list)
    - list empty
    - list with one valid item
    - list with different valid items (no discount)
    - list with different valid items (1 discount)
    - list with different valid items (multiple same discounts)
    - list with different valid items (multiple different discounts)
    """
    catalogue = Catalogue()
    assert catalogue.calculate_final_price(item_ids) == expected


@pytest.mark.parametrize("item_ids,expected", [(["123", "001", "001"], KeyError)])
def test_calculate_final_price_invalid(item_ids, expected):
    """
    cases: calculate_final_price(item_ids: list)
    - list with invalid id in list
    """
    catalogue = Catalogue()
    with pytest.raises(expected):
        catalogue.calculate_final_price(item_ids)

