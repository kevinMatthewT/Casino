import random

Cards=['1','2','3','4','5','6','7','8','9','10','A','J','Q','K']
winner='None'

def deal_cards(deal):
    dealer=[]
    hand=[]
    i=0
    while i<deal:
        dealer.append(random.choice(Cards))
        hand.append(random.choice(Cards))
        i+=1
    return dealer, hand


def calculate_amount(dealer, hand):
    face_card=['J','Q','K']
    dealer_value=0
    hand_value=0
    aces={'dealer':0,'hand':0}
    for card in dealer:
        if card in face_card:
            dealer_value+=10
        elif card=='A':
            aces['dealer']+=1
        else:
            dealer_value+= int(card)
    
    for card in hand:
        if card in face_card:
            hand_value+=10
        elif card=='A':
            aces['hand']+=1
        else:
            hand_value+= int(card)
    
    for i in range(aces['dealer']):
        if (dealer_value+11)>21:
            dealer_value+=1
        else:
            dealer_value+=11
    
    for i in range(aces['hand']):
        if (hand_value+11)>21:
            hand_value+=1
        else:
            hand_value+=11
    
    return dealer_value,hand_value
            
            

def dealer_action():
    print('hello')

def action(action, dealer, hand):
    dealer_value=0
    hand_value=0
    global winner
    match action:
        case 'hit':
            hand.append(random.choice(Cards))
            dealer_value,hand_value=calculate_amount(dealer,hand)
            if(hand_value>21):
                winner= 'dealer'
            if(hand_value==21):
                winner='you'

        case 'stand':
            dealer_value,hand_value=calculate_amount(dealer,hand)
            while dealer_value<17:
                dealer.append(random.choice(Cards))
                dealer_value,hand_value=calculate_amount(dealer,hand)
            if dealer_value==21 and dealer_value==hand_value:
                winner='draw'
            else:
                winner='you'



def show_hand(dealer, hand):
    print(dealer)
    print('\n'*4)
    print(hand)

def check_blackjack(dealer_value, hand_value):
    global winner
    if hand_value == dealer_value and hand_value== 21:
        winner='draw'
    if hand_value==21:
        winner='you'
    if dealer_value==21:
        winner='dealer'
            

def blackjack(money,bet):
    global winner
    winner='None'
    while bet>money:
        bet=int(input("please input amount that is less or equal to your money"))
    
    dealer , hand=deal_cards(2)

    dealer_value,hand_value=calculate_amount(dealer,hand)

    show_hand(dealer,hand)

    check_blackjack(dealer_value,hand_value)

    while winner=='None':
        action(input('Enter Action'), dealer, hand)
        show_hand(dealer, hand)
    
    if winner=='dealer':
        return money-bet
    if winner=='you':
        return money+bet
    if winner=='draw':
        return money
        
