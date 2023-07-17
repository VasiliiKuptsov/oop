from def_cards import card_date
from def_cards import date_rus
from def_cards import number
from def_cards import get_data
from settings import DATA_PATH
cards_date = []
data = get_data(DATA_PATH)
cards_date = []
""" Удаление пустых и недействит карточек"""
cards_date =card_date(data)

""" Сортировка списка дат"""
cards_date.sort(reverse=True)

for it in range(0,5):
    for card_ in data:
        if cards_date[it] == card_["date"]:

            card_["date"] = date_rus(card_["date"])

            """ Преобразование счетов с проверкой прихода из вне"""

            if card_["description"] == 'Открытие вклада':
                card_["from"] = "               "
            else:
                card_["from"] = number("from", card_)
            card_["to"] = number("to", card_)

            """    Вывод карт в нужном формате"""

            print(f"{card_['date']}  {card_['description']}")
            print(f'{card_["from"]} -> {card_["to"]}')
            print(f"{card_['operationAmount']['amount']} {card_['operationAmount']['currency']['name']}")
            print()
            break
