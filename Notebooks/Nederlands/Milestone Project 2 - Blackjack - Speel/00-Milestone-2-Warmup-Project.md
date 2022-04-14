<center>
    <img src='https://intecbrussel.be/img/logo3.png' width='400px' height='auto'/>
    <br/>
    <em>Python les-materialen</em>
</center>

# Warmup Project Exercise

## Simple War Game

Before we launch in to the OOP Milestone 2 Project, let's walk through together on using OOP for a more robust and complex application, such as a game. We will use Python OOP to simulate a simplified version of the game war. Two players will each start off with half the deck, then they each remove a card, compare which card has the highest value, and the player with the higher card wins both cards. In the event of a time

## Single Card Class

### Creating a Card Class with outside variables

Here we will use some outside variables that we know don't change regardless of the situation, such as a deck of cards. Regardless of what round,match, or game we're playing, we'll still need the same deck of cards.


```python
# We'll use this later
import random 
```


```python
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
```


```python
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
```

Create an example card


```python
suits[0]
```




    'Hearts'




```python
ranks[0]
```




    'Two'




```python
two_hearts = Card(suits[0],ranks[0])
```


```python
two_hearts
```




    <__main__.Card at 0x1dfaff6b898>




```python
print(two_hearts)
```

    Two of Hearts
    


```python
two_hearts.rank
```




    'Two'




```python
two_hearts.value
```




    2




```python
values[two_hearts.rank]
```




    2



## Deck Class

### Using a class within another class

We just created a single card, but how can we create an entire Deck of cards? Let's explore doing this with a class that utilizes the Card class.

A Deck will be made up of multiple Cards. Which mean's we will actually use the Card class within the \_\_init__ of the Deck class.


```python
class Deck:
    
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()        
```

### Create a Deck


```python
mydeck = Deck()
```


```python
len(mydeck.all_cards)
```




    52




```python
mydeck.all_cards[0]
```




    <__main__.Card at 0x1dfaff269e8>




```python
print(mydeck.all_cards[0])
```

    Two of Hearts
    


```python
mydeck.shuffle()
```


```python
print(mydeck.all_cards[0])
```

    Five of Spades
    


```python
my_card = mydeck.deal_one()
```


```python
print(my_card)
```

    King of Clubs
    

# Player Class

Let's create a Player Class, a player should be able to hold instances of Cards, they should also be able to remove and add them from their hand. We want the Player class to be flexible enough to add one card, or many cards so we'll use a simple if check to keep it all in the same method.

We'll keep this all in mind as we create the methods for the Player class.

### Player Class


```python
class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = [] 
        
    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
```


```python
jose = Player("Jose")
```


```python
jose
```




    <__main__.Player at 0x1dfaff8b940>




```python
print(jose)
```

    Player Jose has 0 cards.
    


```python
two_hearts
```




    <__main__.Card at 0x1dfaff6b898>




```python
jose.add_cards(two_hearts)
```


```python
print(jose)
```

    Player Jose has 1 cards.
    


```python
jose.add_cards([two_hearts,two_hearts,two_hearts])
```


```python
print(jose)
```

    Player Jose has 4 cards.
    

## War Game Logic


```python
player_one = Player("One")
```


```python
player_two = Player("Two")
```

## Setup New Game


```python
new_deck = Deck()
```


```python
new_deck.shuffle()
```

### Split the Deck between players


```python
len(new_deck.all_cards)/2
```




    26.0




```python
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
```


```python
len(new_deck.all_cards)
```




    0




```python
len(player_one.all_cards)
```




    26




```python
len(player_two.all_cards)
```




    26



## Play the Game


```python
import pdb
```


```python
game_on = True
```


```python
round_num = 0
while game_on:
    
    round_num += 1
    print(f"Round {round_num}")
    
    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break
    
    # Otherwise, the game is still on!
    
    # Start a new round and reset current cards "on the table"
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True

    while at_war:


        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            
            # No Longer at "war" , time for next round
            at_war = False
        
        # Player Two Has higher Card
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            # No Longer at "war" , time for next round
            at_war = False

        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.
            
            # First check to see if player has enough cards
            
            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
        
```

    Round 1
    Round 2
    Round 3
    Round 4
    Round 5
    Round 6
    Round 7
    Round 8
    Round 9
    Round 10
    Round 11
    Round 12
    Round 13
    Round 14
    Round 15
    Round 16
    Round 17
    Round 18
    Round 19
    Round 20
    Round 21
    Round 22
    Round 23
    Round 24
    Round 25
    Round 26
    Round 27
    Player One out of cards! Game Over
    

## Game Setup in One Cell


```python
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
game_on = True
```


```python
round_num = 0
while game_on:
    
    round_num += 1
    print(f"Round {round_num}")
    
    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break
    
    # Otherwise, the game is still on!
    
    # Start a new round and reset current cards "on the table"
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True

    while at_war:


        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            
            # No Longer at "war" , time for next round
            at_war = False
        
        # Player Two Has higher Card
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            # No Longer at "war" , time for next round
            at_war = False

        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.
            
            # First check to see if player has enough cards
            
            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

        
```

    Round 1
    Round 2
    WAR!
    Round 3
    WAR!
    WAR!
    Round 4
    WAR!
    Round 5
    Round 6
    Round 7
    Round 8
    Round 9
    Round 10
    Round 11
    Round 12
    Round 13
    WAR!
    Round 14
    Round 15
    WAR!
    Round 16
    Round 17
    Round 18
    Round 19
    Round 20
    Round 21
    Round 22
    Round 23
    Round 24
    Round 25
    Round 26
    Round 27
    Round 28
    Round 29
    WAR!
    Round 30
    Round 31
    Round 32
    WAR!
    Round 33
    Round 34
    Round 35
    Round 36
    Round 37
    Round 38
    Round 39
    Round 40
    Round 41
    Round 42
    WAR!
    WAR!
    Round 43
    Round 44
    Round 45
    Round 46
    Round 47
    Round 48
    Round 49
    Round 50
    Round 51
    Round 52
    Round 53
    Round 54
    Round 55
    Round 56
    Round 57
    Round 58
    Round 59
    Round 60
    Round 61
    Round 62
    Round 63
    Round 64
    Round 65
    Round 66
    Round 67
    Round 68
    Round 69
    Round 70
    Round 71
    Round 72
    Round 73
    Round 74
    Round 75
    Round 76
    Round 77
    Round 78
    Round 79
    Round 80
    Round 81
    Round 82
    Round 83
    Round 84
    Round 85
    Round 86
    Round 87
    Round 88
    Round 89
    Round 90
    Round 91
    Round 92
    Round 93
    Round 94
    Round 95
    Round 96
    Round 97
    Round 98
    Round 99
    Round 100
    Round 101
    Round 102
    Round 103
    Round 104
    Round 105
    Round 106
    Round 107
    Round 108
    WAR!
    Round 109
    Round 110
    Round 111
    Round 112
    Round 113
    Round 114
    Round 115
    Round 116
    Round 117
    Round 118
    Round 119
    Round 120
    Round 121
    Round 122
    Round 123
    Round 124
    Round 125
    Round 126
    Round 127
    Round 128
    Round 129
    Round 130
    Round 131
    Round 132
    Round 133
    Round 134
    WAR!
    Round 135
    Round 136
    WAR!
    Round 137
    WAR!
    Round 138
    Round 139
    Round 140
    Round 141
    Round 142
    Round 143
    Round 144
    Round 145
    Round 146
    Round 147
    Round 148
    Round 149
    Round 150
    Round 151
    Round 152
    Round 153
    Round 154
    Round 155
    Round 156
    Round 157
    Round 158
    Round 159
    Round 160
    Round 161
    Round 162
    Round 163
    Round 164
    Round 165
    Round 166
    Round 167
    Round 168
    Round 169
    Round 170
    Round 171
    Round 172
    Round 173
    Round 174
    Round 175
    Round 176
    Round 177
    Round 178
    Round 179
    Round 180
    Round 181
    Round 182
    Round 183
    Round 184
    Round 185
    Round 186
    Round 187
    Round 188
    Round 189
    Round 190
    Round 191
    Round 192
    Round 193
    Round 194
    Round 195
    Round 196
    Round 197
    Round 198
    Round 199
    Round 200
    Round 201
    Round 202
    Round 203
    Round 204
    Round 205
    Round 206
    Round 207
    Round 208
    Round 209
    Round 210
    Round 211
    Round 212
    Round 213
    Round 214
    Round 215
    Round 216
    Round 217
    Round 218
    Round 219
    Round 220
    Round 221
    Round 222
    Round 223
    WAR!
    Round 224
    Round 225
    Round 226
    Round 227
    Round 228
    Round 229
    Round 230
    Round 231
    Round 232
    Round 233
    Round 234
    Round 235
    Round 236
    Round 237
    Round 238
    Round 239
    Round 240
    Round 241
    Round 242
    Round 243
    Round 244
    Round 245
    Round 246
    Round 247
    Round 248
    Round 249
    Round 250
    Round 251
    Round 252
    Round 253
    Round 254
    Round 255
    Round 256
    Round 257
    WAR!
    Round 258
    Round 259
    Round 260
    Round 261
    Round 262
    Round 263
    Round 264
    Round 265
    Round 266
    Round 267
    Round 268
    Round 269
    Round 270
    Round 271
    Round 272
    Round 273
    Round 274
    Round 275
    Round 276
    Round 277
    Round 278
    Round 279
    Round 280
    Round 281
    Round 282
    Round 283
    Round 284
    Round 285
    Round 286
    Round 287
    Round 288
    Round 289
    Round 290
    Round 291
    Round 292
    Round 293
    Round 294
    Round 295
    Round 296
    Round 297
    Round 298
    Round 299
    Round 300
    Round 301
    Round 302
    Round 303
    Round 304
    Round 305
    Round 306
    Round 307
    WAR!
    Round 308
    Round 309
    Round 310
    Round 311
    Round 312
    Round 313
    Round 314
    Round 315
    WAR!
    Round 316
    Round 317
    Round 318
    Round 319
    Round 320
    Round 321
    Round 322
    Round 323
    Round 324
    Round 325
    Round 326
    Round 327
    Round 328
    Round 329
    Round 330
    Round 331
    Round 332
    Round 333
    Round 334
    Round 335
    Round 336
    Round 337
    Round 338
    Round 339
    Round 340
    Round 341
    Round 342
    Round 343
    Round 344
    Round 345
    Round 346
    Round 347
    Round 348
    Round 349
    WAR!
    Round 350
    WAR!
    Player Two unable to play war! Game Over at War
    Player One Wins! Player One Loses!
    


```python
len(player_one.all_cards)
```




    27




```python
len(player_two.all_cards)
```




    25




```python
print(player_one_cards[-1])
```

    Ace of Diamonds
    


```python
print(player_two_cards[-1])
```

    Four of Hearts
    

## Great Work!

Other links that may interest you:
* https://www.reddit.com/r/learnpython/comments/7ay83p/war_card_game/
* https://codereview.stackexchange.com/questions/131174/war-card-game-using-classes
* https://gist.github.com/damianesteban/6896120
* https://lethain.com/war-card-game-in-python/
* https://hectorpefo.github.io/2017-09-13-Card-Wars/
* https://www.wimpyprogrammer.com/the-statistics-of-war-the-card-game
