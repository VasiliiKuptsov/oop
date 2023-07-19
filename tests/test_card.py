
from arc.def_cards import get_card_date, get_date_rus, get_number, get_data, get_sorting_five
from arc.settings import DATA_PATH


def test_get_sorting_five(valid_data):
    assert len(get_sorting_five(valid_data)) == 5
    assert get_sorting_five(valid_data)[0] == {'id': 441945886, 'state': 'EXECUTED', 'date':
    '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58',
    'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from':
    'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}


def test_get_data():
    assert isinstance(get_data(DATA_PATH), list)


def test_get_card_date(valid_data):
    assert len(get_card_date(valid_data)) == 9
    assert isinstance(get_card_date(valid_data), list)
    assert get_card_date(valid_data)[0]['state'] == 'EXECUTED'
    assert get_card_date(valid_data)[0] == {'id': 441945886, 'state': 'EXECUTED', 'date':
    '2019-08-26T10:50:58.294041',
    'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.',
    'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
    'to': 'Счет 64686473678894779589'}


def test_get_date_rus():
    assert get_date_rus('2019-11-22') == '22-11-2019'


def test_get_number(valid_data):
    assert get_number('from', valid_data[0]) == 'Maestro 1596 83** **** 5199'
    assert get_number('to', valid_data[0]) == 'Счет **9589'
    assert get_number('from', valid_data[1]) == 'MasterCard 7158 30** **** 6758'
    assert get_number('from', valid_data[8]) == 'Visa Classic 6831 98** **** 7658'
    assert get_number('to', valid_data[8]) == 'Visa Platinum 8990 92** **** 5229'
