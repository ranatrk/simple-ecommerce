[![codecov](https://codecov.io/gh/ranatrk/simple-ecommerce/branch/main/graph/badge.svg?token=LM0ZEC6H3G)](https://codecov.io/gh/ranatrk/simple-ecommerce)

# simple-ecommerce

A simple e-commerce flask application with a single endpoint that performs a checkout action including discounted items

## Contents

- [Components](#components)
- [Running](#running)
  - [Build image and run container](#build-image-and-run-container)
- [Tests](#tests)
  - [Manual testing](#manual-testing)
  - [Unit functional tests](#unit-functional-tests)
  - [Automatic test run](#automatic-test-run)
- [Coverage](#coverage)
- [Improvements](#improvements)

## Components

- **ecommerce_app**:

  - A simple flask application where the API endpoints are defined
  - routes:
        `/checkout` calculate and return total price of items given their ids-> POST request, JSON body: list of Item IDs

- **catalogue data**:
  - JSON file with details about the ecommerce app's items including their ids, prices, and possible discount options when multiple items of the same id are found.
  - example

    ```json
    {
        "001": 
        {"name": "Rolex", "price": 100, "discount": [3, 200]}, 
        "002": 
        {"name": "Michael Kors", "price": 80, "discount": [2, 120]},
        "003": 
        {"name": "Swatch", "price": 50, "discount": []},
        "004": 
        {"name": "Casio", "price": 30, "discount": []}
    }
    ```

- **catalogue**:
  - Python module to handle any processing regaring the ecommerce app and catalgoue details
  - Loads the catalogue json into a python dict to be used
  - Functions:
    - `calculate_discount(self, id, count)` : calculates possible discounted price(if exists) for a number of items with the given id
    - `calculate_final_price(self, item_ids: list)`: calculates total final price of a given list of item ids including any posible discounts

## Running

- Prerequisites to be installed:
  - docker, docker-compose
  - python3, pytest (to run tests manually)

### Build image and run container

using docker-compose

## Tests

### Manual testing

- To manually test a specific endpoint after the server is up using a curl command the following can be used

  ```bash
  curl -d '<LIST_OF_IDS>' -H "Content-Type: application/json" -X POST http://172.29.0.2:5000/checkout
  ```
  
  where

  - *LIST_OF_IDS*: list of string ids of items. e.g `["001","001","001"]`

### Unit/functional tests

- Test cases:

  - **test_catalogue**: covers unit tests for catalogue module functionalities and scenarios
  - **test_app**: covers unit tests for the flask application endpoint scenarios
- Running the tests from repo home

    ```bash
    pytest -s ecommerce_app/tests/
    ```

### Automatic test run

- Github actions workflow added to run the unit tests with every push to github and can be run manually from github actions tab in the repo

### Coverage

- [code-cov](https://app.codecov.io/) is used to output code coverage reports whenever github action flow is triggered.

## Improvements

- Add database for larger catalogue (preferebly relational for fast data retrieval)
- Improve data retrieval from catalogue(if no database) e.g load from csv file
