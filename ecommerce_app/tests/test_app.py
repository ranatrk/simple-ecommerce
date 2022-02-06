import pytest

from .conftest import app_client


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
def test_checkout_valid(item_ids, expected, app_client):
    """
    cases: calculate_final_price(item_ids: list)
    - list empty
    - list with one valid item
    - list with different valid items (no discount)
    - list with different valid items (1 discount)
    - list with different valid items (multiple same discounts)
    - list with different valid items (multiple different discounts)
    """

    response = app_client.post("/checkout", json=item_ids, content_type="application/json")
    resp = response.get_json()
    assert response.status_code == 200

    assert resp.get("price") == expected


@pytest.mark.parametrize("item_ids", [(["123", "001", "001"])])
def test_calculate_final_price_invalid(item_ids, app_client):
    """
    cases: calculate_final_price(item_ids: list)
    - list with invalid id in list
    """
    response = app_client.post("/checkout", json=item_ids)
    assert response.status_code == 400

    assert "'Id 123 does not exist'" == response.data.decode()  # FIXME

