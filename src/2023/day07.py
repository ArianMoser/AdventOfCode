import os
import sys
import re

#1'high card'
#2'one pair'
#3'two pair'
#4'three of a kind'
#5'full house'
#6'four of a kind'
#7'five of a kind'
card_map = {'T': 'a', 'J': '1', 'Q': 'c', 'K': 'd', 'A': 'e'}

def convert_cards_to_hex(cards):
    hex_string = ''
    for card in cards:
        if card in card_map.keys(): hex_string += card_map[card]
        else: hex_string += card
    return hex_string

def has_five_of_a_kind(cards):
    card_count = {card: cards.count(card) for card in set(cards) if card != 'J'}
    jacks = cards.count('J')
    try:
        return 5 == max(card_count.values()) + jacks
    except ValueError:
        return 5 == jacks

def has_four_of_a_kind(cards):
    card_count = {card: cards.count(card) for card in set(cards) if card != 'J'}
    jacks = cards.count('J')
    return 4 == max(card_count.values()) + jacks

def has_three_of_a_kind(cards):
    card_count = {card: cards.count(card) for card in set(cards) if card != 'J'}
    jacks = cards.count('J')
    return 3 == max(card_count.values()) + jacks

def has_full_house(cards):
    card_count = {card: cards.count(card) for card in set(cards) if card != 'J'}
    jacks = cards.count('J')
    return (3 in card_count.values() and 2 in card_count.values()) or (has_two_pairs(cards) and jacks == 1)

def has_two_pairs(cards):
    card_count = {card: cards.count(card) for card in set(cards)}
    return list(card_count.values()).count(2) == 2

def has_one_pair(cards):
    card_count = {card: cards.count(card) for card in set(cards) if card != 'J'}
    jacks = cards.count('J')
    return 2 in card_count.values() or jacks == 1

def get_cards_value(poker_round):
    cards = poker_round[0]
    value = convert_cards_to_hex(cards)
    if has_five_of_a_kind(cards): return int('7' + value, 16)
    if has_four_of_a_kind(cards): return int('6' + value, 16)
    if has_full_house(cards): return int('5' + value, 16)
    if has_three_of_a_kind(cards): return int('4' + value, 16)
    if has_two_pairs(cards): return int('3' + value, 16)
    if has_one_pair(cards): return int('2' + value, 16)
    return int('1' + value, 16)

def main(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        f_content = f.read()
    lines = f_content.splitlines()
    cards = []
    for line in lines:
        cards.append(line.split(' '))


    # task 2
    res = 0
    for i, poker_round in enumerate(sorted(cards, key=get_cards_value)):
        print(i, poker_round[0])
    res = sum(int(r[1])*(i+1) for i, r in enumerate(sorted(cards, key=get_cards_value)))
    print(f"Task 2: {res}")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else: 
        input_file = os.path.join(os.path.dirname(__file__), \
                                'inputs', 
                                sys.argv[0].replace("py", "txt"))
        main(input_file)
