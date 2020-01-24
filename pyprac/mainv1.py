import random as rdom
deck=[]
rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J','Q','K','A']
suit = [u"\u2660", u"\u2661", u"\u2662", u"\u2663"]
card = (rank[2],suit[2])
print(rank, suit)
print(card)

# deck.append(
#    (rank[2], suit[0])
# )
for i in rank:
    for k in suit:
        print(i, k)
        card = (i, k)
        deck.append(card)
print(deck)

def printCard(c):
    print("---")
    print(c[0])
    print(" "+c[1])
    print("  "+c[0])
    print("---")

    return

printCard(deck[4])
#print('enter to begin the game')
#spade = u"\u2663"
#player1 = 0
#player2 = 0
#for i in range (1, 6):
 #   hand= [deck.pop(), deck.pop()]
  #  if hand[0]> hand[1]:
   #    player1= player1++






