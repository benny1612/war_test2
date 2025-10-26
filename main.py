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
    
def create_deck() -> list[dict]:
    ranks ={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10, "J":11,"Q":12,"K":13,"A":14}
    suits_list=["H",'C','D','S']
    list_of_cards=[]

    for rank in ranks:
        for l in suits_list:
            list_of_cards.append(create_card(rank,l))
    
    return list_of_cards
def shuffle(deck:list[dict]):
    list_of_cards=create_deck()
    shuffle_list=[]

    import random
    for i in range(random.randrange(1,1001)):
        list_of_cards[random.randint(1,51)]=list_of_cards[random.randint(1,51)]
        
        shuffle_list=list_of_cards
        
        
                
    return shuffle_list