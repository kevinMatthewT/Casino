import blackjack

money=1000
going=True

while going:
    game=input("what do you want to play?")

    match game:
        case 'blackjack':
            bet=int(input("How much do you want to bet"))
            money=blackjack.blackjack(money,bet)
            print("This is your current balance:" + str(money))