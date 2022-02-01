from gettext import Catalog
import pytest
import json
from catalogue import Catalogue

import requests

BASE_URL = "http://main_app:5000"


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
def test_checkout_valid(item_ids, expected):
    """
    cases: calculate_final_price(item_ids: list)
    - list empty
    - list with one valid item
    - list with different valid items (no discount)
    - list with different valid items (1 discount)
    - list with different valid items (multiple same discounts)
    - list with different valid items (multiple different discounts)
    """
    checkout_url = f"{BASE_URL}/checkout"

    response = requests.post(checkout_url, json=item_ids)
    resp = response.json()
    assert response.status_code == 200

    catalogue = Catalogue()
    assert resp.get("price") == expected


@pytest.mark.parametrize("item_ids", [(["123", "001", "001"])])
def test_calculate_final_price_invalid(item_ids):
    """
    cases: calculate_final_price(item_ids: list)
    - list with invalid id in list
    """
    checkout_url = f"{BASE_URL}/checkout"

    response = requests.post(checkout_url, json=item_ids)
    assert response.status_code == 400

    catalogue = Catalogue()
    assert "'Id 123 does not exist'" == response.text  # FIXME

