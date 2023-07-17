import json

cards_date = []

def get_data(path:str) -> list[dict]:
    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data



def card_date(data):
    for item in data:
        if item == {}:
            del item
        elif item["state"] != "EXECUTED":
            del item
        else:
            cards_date.append(item["date"])
    return cards_date


def date_rus(card_new):
    return card_new[8:10] + "-" + card_new[5:7] + "-" + card_new[0:4] + card_new[10:]

def number(key:str, card_:dict):
    list_ = card_[key].split(" ")
    list_len = len(list_[len(list_) - 1])
    if list_len == 20:
        card_number = card_[key][0:len(card_[key]) - list_len] + "**" + card_[key][len(card_[key]) - 4:]
    else:
        card_number = card_[key][0:len(card_[key]) - list_len] + card_[key][len(card_[key]) - 15:len(card_[key]) - 11] \
                      + " " + card_[key][len(card_[key]) - 10:len(card_[key]) - 8] + "** **** " + card_[key][len(card_[key]) - 4:len(card_[key])]

    return card_number


