import json
cards_date = []


def get_data(path: str):
    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_card_date(data):
    for item in data:
        if item == {}:
            del item
        elif item["state"] != "EXECUTED":
            del item
        else:
            cards_date.append(item)
    return cards_date


def get_sorting_five(data: list[dict]):
    return list(sorted(data, key=lambda make: make['date'], reverse=True))[:5]


def get_date_rus(card_new):
    return card_new[8:10] + "-" + card_new[5:7] + "-" + card_new[0:4]


def get_number(key: str, card_: dict):
    list_ = card_[key].split(" ")
    list_len = len(list_[len(list_) - 1])
    if list_len == 20:
        card_number = card_[key][:4] + " **" + card_[key][- 4:]
    else:
        card_number = card_[key][:- 12] + " " + card_[key][- 12:- 10] + "** **** " + card_[key][- 4:]
    return card_number
