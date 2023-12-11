from pathlib import Path
import datetime

def f_1() -> int:
    cards = {"A":14,"K":13,"Q":12,"J":11,"T":10}
    hc = []
    pair = []
    pair2 = []
    kind3 = []
    fullhouse = []
    kind4 = []
    kind5 = [] 
    hands = {}
    for line in Path('i.txt').open("r"):
        c_dict = {"A":0,"K":0,"Q":0,"J":0,"T":0,"9":0,"8":0,"7":0,"6":0,"5":0,"4":0,"3":0,"2":0}
        hand = []
        init_hand, bid = line.strip().split(" ")
        for i in init_hand:
            c_dict[i] += 1
            if i.isalpha():
                hand.append(cards[i])
            else:
                hand.append(int(i))
        hands[str(hand)] = int(bid)
        pairs = 0
        kind_3 = 0
        full_house = 0
        kind_4 = 0
        kind_5 = 0
        for i in c_dict:
            if c_dict[i] == 2:
                pairs += 1
            elif c_dict[i] == 3:
                kind_3 += 1
            elif c_dict[i] == 4:
                kind_4 += 1
            elif c_dict[i] == 5:
                kind_5 += 1
            if pairs > 0 and kind_3 > 0:
                full_house += 1

        if kind_5 > 0:
            kind5.append(hand)
        elif kind_4 > 0:
            kind4.append(hand)
        elif full_house > 0:
            fullhouse.append(hand)
        elif kind_3 > 0:
            kind3.append(hand)
        elif pairs == 1:
            pair.append(hand)
        elif pairs == 2:
            pair2.append(hand)
        else:
            hc.append(hand)

    r,v = value(sorted(hc), hands, 0,0,"hc")
    r,v = value(sorted(pair), hands, r,v,"1 pair")
    r,v = value(sorted(pair2), hands, r,v,"2 pair")
    r,v = value(sorted(kind3), hands, r,v,"3 kind")
    r,v = value(sorted(fullhouse), hands, r,v,"full house")
    r,v = value(sorted(kind4), hands, r,v,"4 kind")
    r,v = value(sorted(kind5), hands, r,v,"5 kind")

    print(f"Rank: {r}, Value: {v}")

def f_2() -> int:
    cards = {"A":14,"K":13,"Q":12,"J":1,"T":10}
    hc = []
    pair = []
    pair2 = []
    kind3 = []
    fullhouse = []
    kind4 = []
    kind5 = [] 
    hands = {}
    for line in Path('i.txt').open("r"):
        c_dict = {"A":0,"K":0,"Q":0,"T":0,"9":0,"8":0,"7":0,"6":0,"5":0,"4":0,"3":0,"2":0,"J":0}
        hand = []
        init_hand, bid = line.strip().split(" ")
        for i in init_hand:
            c_dict[i] += 1
            if i.isalpha():
                hand.append(cards[i])
            else:
                hand.append(int(i))
        hands[str(hand)] = int(bid)
        largest_dict_add_jokers(c_dict)
        pairs = 0
        kind_3 = 0
        full_house = 0
        kind_4 = 0
        kind_5 = 0
        for i in c_dict:
            if c_dict[i] == 2:
                pairs += 1
            elif c_dict[i] == 3:
                kind_3 += 1
            elif c_dict[i] == 4:
                kind_4 += 1
            elif c_dict[i] == 5:
                kind_5 += 1
            if pairs > 0 and kind_3 > 0:
                full_house += 1
        
        if kind_5 > 0:
            kind5.append(hand)
        elif kind_4 > 0:
            kind4.append(hand)
        elif full_house > 0:
            fullhouse.append(hand)
        elif kind_3 > 0:
            kind3.append(hand)
        elif pairs == 1:
            pair.append(hand)
        elif pairs == 2:
            pair2.append(hand)
        else:
            hc.append(hand)

    r,v = value(sorted(hc), hands, 0,0,"hc")
    r,v = value(sorted(pair), hands, r,v,"1 pair")
    r,v = value(sorted(pair2), hands, r,v,"2 pair")
    r,v = value(sorted(kind3), hands, r,v,"3 kind")
    r,v = value(sorted(fullhouse), hands, r,v,"full house")
    r,v = value(sorted(kind4), hands, r,v,"4 kind")
    r,v = value(sorted(kind5), hands, r,v,"5 kind")

    print(f"Rank: {r}, Value: {v}")


def largest_dict_add_jokers(dict) -> None:
    largest = 0 
    for i in dict:
        if i != "J":
            if largest == 0 and dict[i] > 0:
                largest = i
            if largest != 0:
                if dict[i] > dict[largest]:
                    largest = i
    if largest != 0:
        dict[largest] += dict["J"]

def value(s, hands_dict, rank, value, vl):
    for i in s:
        rank += 1
        value += hands_dict[str(i)] * rank
    return rank, value

if __name__ == "__main__":
    start = datetime.datetime.now()
    f_1()
    print(f"Time taken: {(datetime.datetime.now() - start).microseconds/1000}ms")
    start = datetime.datetime.now()
    f_2()
    print(f"Time taken: {(datetime.datetime.now() - start).microseconds/1000}ms")
