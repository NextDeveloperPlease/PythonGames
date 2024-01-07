import numpy as np
from Player import Player
import Settings as st
def roulette(player):
    betting = True
    bet = 0
    while betting:
        bet = int(input("Enter your bet: "))
        if bet > player.get_wallet():
            print("You crook!")
            amount_lost = np.random.randint(1, 20)
            print(f"You lose: {amount_lost}")
            player.spend(amount_lost)
            print(player.get_wallet())
        else:
            betting = False
    
    print("Enter the number associated with your bet type: ")
    user_input = input("1. Straight up\t\t2. Split\n3. Street\t\t4. Corner bet\n5. 0-00-1-2-3 bet\t6. Line\n7. Dozen bet\t\t8. Column bet\n9. Eighteen numbers\t10. Red or black bet\n11. Odd or evene bet")
    tile = []
    match(user_input): #Maybe make a matrix to check if a bet is legal
        case '1':
            tile.append(input("Enter the tile you would like to play on: "))
        case '2':
            tile.append(input("Enter the first tile you would like to play on: "))
            tile.append(input("Enter the second tile you would like to play on: "))
        case '3':
            tile.append(input("Enter the first tile you would like to play on: "))
            tile.append(input("Enter the second tile you would like to play on: "))
            tile.append(input("Enter the third tile you would like to play on: "))
        case '4':
            tile.append(input("Enter the first tile you would like to play on: "))
            tile.append(input("Enter the second tile you would like to play on: "))
            tile.append(input("Enter the third tile you would like to play on: "))
            tile.append(input("Enter the third tile you would like to play on: "))
        case '5':
            tile.append('0')
            tile.append('00')
            tile.append('1')
            tile.append('2')
            tile.append('3')
        case '6':
            tile.append(input("Enter the first tile you would like to play on: "))
            tile.append(input("Enter the second tile you would like to play on: "))
            tile.append(input("Enter the third tile you would like to play on: "))
            tile.append(input("Enter the fourth tile you would like to play on: "))
            tile.append(input("Enter the fifth tile you would like to play on: "))
            tile.append(input("Enter the sixth tile you would like to play on: "))
        case '7':
            tile.append(input("Enter the first tile you would like to play on: "))
            tile.append(input("Enter the second tile you would like to play on: "))
            tile.append(input("Enter the third tile you would like to play on: "))
            tile.append(input("Enter the fourth tile you would like to play on: "))
            tile.append(input("Enter the fifth tile you would like to play on: "))
            tile.append(input("Enter the sixth tile you would like to play on: "))
            tile.append(input("Enter the seventh tile you would like to play on: "))
            tile.append(input("Enter the eighth tile you would like to play on: "))
            tile.append(input("Enter the nineth tile you would like to play on: "))
            tile.append(input("Enter the tenth tile you would like to play on: "))
            tile.append(input("Enter the eleventh tile you would like to play on: "))
            tile.append(input("Enter the twelveth tile you would like to play on: "))
        case '8':
            col = input("Enter the column you would like to play on (1, 2, 3): ")
            match(col):
                case '1':
                    tiles = np.arange(1, 35, 4)
                    tile.append(tiles)
                case '2':
                    tiles = np.arange(2, 36, 4)
                    tile.append(tiles)
                case '3':
                    tiles = np.arange(3, 37, 4)
                    tile.append(tiles)
        case '9':
            col = input("1 to 18 or 19 to 36? (1 or 2)")
            match(col):
                case '1':
                    tiles = np.arange(1, 19)
                    tile.append(tiles)
                case '2':
                    tiles = np.arange(1, 37)
                    tile.append(tiles)
        case '10':
            col = input("Enter the color you would like to play on (red or black): ").lower()
            match(col):
                case 'red':
                    tile.append('red')
                case 'black':
                    tile.append('black')
        case '11':
            col = input("Enter the parity you would like to play on (odd or even): ")
            match(col):
                case 'odd':
                    tiles = np.arange(1, 36, 2)
                    tile.append(tiles)
                case 'even':
                    tiles = np.arange(2, 37, 2)
                    tile.append(tiles)
    #Finish adding the logic of rolling the ball
roulette(Player())