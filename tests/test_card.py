import pytest




from arc.def_cards import card_date
from arc.def_cards import date_rus
from arc.def_cards import number
from arc.def_cards import get_data
from arc.settings import DATA_PATH

def test_get_data():
    assert isinstance(get_data(DATA_PATH), list)
    with pytest.raises(FileNotFoundError):
        get_data('hkjlh')

def test_card_date(valid_data, i_data):
    assert len(card_date(valid_data)) == 9
    assert card_date(i_data) == ['2019-08-26T10:50:58.294041',
 '2018-06-30T02:08:58.425572',
 '2018-03-23T10:45:06.972075',
 '2019-04-04T23:20:05.206878',
 '2019-03-23T01:09:46.296404',
 '2018-12-20T16:43:26.929246',
 '2019-07-12T20:41:47.882230',
 '2018-08-19T04:27:37.904916',
 '2018-07-11T02:26:18.671407',
 '2019-08-26T10:50:58.294041']


def test_date_rus():
    assert date_rus('2019-11-22') == '22-11-2019'

def test_number(valid_data):
    assert number('from', valid_data[0]) == 'Maestro 5968 78** **** 5199'
    assert number('to', valid_data[0]) == 'Счет **9589'
    assert number('from', valid_data[1]) == 'MasterCard 1583 07** **** 6758'
    assert number('from', valid_data[8]) == 'Visa Classic 8319 24** **** 7658'
    assert number('to', valid_data[8]) == 'Visa Platinum 9909 21** **** 5229'
