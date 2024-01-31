"Demonstrates while loops by finding low value in string"

card: str = "5235"

Card_indx: int = 0
low_card: int = int(card[0])
#look at each number in the string
while Card_indx < 4:
    # check if current card is less than low card
    current_card: int = int(card[Card_indx])
    if (current_card < low_card):
    #update the low card to be the value of our current card
        low_card = current_card
    Card_indx = Card_indx + 1
print(low_card)