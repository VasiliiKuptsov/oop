
from def_cards import get_card_date, get_date_rus, get_number, get_data, get_sorting_five
from settings import DATA_PATH


data = get_data(DATA_PATH)

""" Удаление пустых и недействит карточек"""

data = get_card_date(data)

""" Сортировка списка дат"""

data = get_sorting_five(data)
for card_ in data:
    card_["date"] = get_date_rus(card_["date"])

    """ Преобразование счетов с проверкой прихода из вне"""

    if card_["description"] == "Открытие вклада":
        card_["from"] = "               "
    else:
        card_["from"] = get_number("from", card_)
    card_["to"] = get_number("to", card_)

    """    Вывод карт в нужном формате"""

    print(f"{card_['date']}  {card_['description']}")
    print(f'{card_["from"]} -> {card_["to"]}')
    print(f"{card_['operationAmount']['amount']} {card_['operationAmount']['currency']['name']}")
    print()

