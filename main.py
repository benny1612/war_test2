def create_card(rank:str, suite:str) -> dict:
    ranks ={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10, "J":11,"Q":12,"K":13,"A":14}
    suits= ["H", "C", "D", "S"]
    card_dict={"rank":rank,"suite":suite}
   
    if rank in ranks and suite in suits:
        card_dict["velue"]=(ranks[rank])
    return card_dict
print(create_card("10","H"))
print(create_card("A","S"))


def compare_card(p1_card:dict, p2_card:dict):
    if p1_card["velue"] > p2_card['velue']:
        return'p1'
    elif p1_card["velue"] < p2_card['velue']:
        return 'p2'
    elif p1_card["velue"] == p2_card['velue']:
        return "WAR"
    # test