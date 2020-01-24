import random as rdom
deck = []
print("one", deck)
for i in range(1, 11):
    deck.append(i)
deck[0] = 1000
#print("two", deck)
#deck.reverse()
#print("three", deck)
#hand= (deck.pop(),deck.pop())
#print("four", deck)
#hand= (deck.pop(),deck.pop())
#print("five", deck)
#print(hand)
#print(hand)
#print(deck)
rdom.shuffle(deck)
#indexofone = deck.index(1)
#print(deck[indexofone])
#deck[indexofone] = "A"
#print(deck)
print("press enter to begin game")
spade= u"\u2660"

mscore=0
ascore= 0
input()
for i in range (1, 6):
    hand= [deck.pop(), deck.pop()]
    if hand[0]>hand[1]:
        mscore=mscore+1
    else:
        ascore=ascore+1
    if hand[0] == 1000:
        hand[0] ="A"
    if hand[1] == 1000:
        hand[1] = "A"
    print(str(hand[0]) + spade, " , ", str(hand[1]) + spade)
    input()
print(deck)
print("mohadesa =", mscore, ", ahsan =", ascore)
spade= u"\u2660"
print(spade)







