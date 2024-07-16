import random
from blackart import logo

def dealCards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calcScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return sum(cards)
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(userScore, compScore):
    if userScore > 21 and compScore > 21:
        return "Both Bust!"
    if userScore == compScore:
        return "Push!"
    elif compScore == 21:
        return "Opponent has Blackjack!"
    elif userScore == 21:
        return "You have Blackjack"
    elif userScore > 21:
        return "Bust!"
    elif compScore > 21:
        return "Opponent bust!"
    elif userScore > compScore:
        return "You win!"
    else:
        return "You lose!"

def game():
    print(logo)
    userCards = []
    compCards = []
    gameOver = False
    
    for card in range(2):
        userCards.append(dealCards())
        compCards.append(dealCards())
    while not gameOver:
        userScore = calcScore(userCards)
        compScore = calcScore(compCards)
        print(f"Your cards are: {userCards}, your score: {userScore}")
        print(f"Opponent's cards are: {compCards}, their score: {compScore}")
        
        if userScore == 21 or compScore == 21 or userScore > 21:
            gameOver = True
        else:
            decis = input("'hit' or 'stand'?").lower()
            if decis == "hit":
                userCards.append(dealCards())
            else:
                gameOver = True
    while compScore != 21 and compScore < 17:
        compCards.append(dealCards())
        compScore = calcScore(compCards)
    print(f"Your final hand: {userScore}, your final score: {userScore}")
    print(f"Opponents final hand: {compScore}, their final score: {compScore}")
    print(compare(userScore, compScore))
while input("Play BlackJack? 'y' or 'n'").lower() == "y":
    game()
    
    
    
    
    
    