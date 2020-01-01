import requests


def test_login():
    result = requests.get('https://demo.book24.ru/api/v1/sale/order/basket', auth=('selivanov.sa@eksmo.ru', '955098'))
    assert 200 == result.status_code
