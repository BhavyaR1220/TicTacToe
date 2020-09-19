block=['1','2','3','4','5','6','7','8','9','choice']
cont=1
turn=1
def display():
    print(f"{block[0]} | {block[1]} | {block[2]}")
    print(f"{block[3]} | {block[4]} | {block[5]}")
    print(f"{block[6]} | {block[7]} | {block[8]}")

def won(a):
    
    global turn
    if a=='O':
        print('Player 1 WON')
    else :
        print('Player 2 WON')    
    ask=input('want to play again ?(Y/N)')
    if ask=='N':
        print('Bye')
        exit()
    else:
        global block
        block=['1','2','3','4','5','6','7','8','9','choice']
        turn=0
        display()
        game()

def check():
    
    global cont
    if block[0]==block[1]==block[2] or block[0]==block[4]==block[8] or block[0]==block[3]==block[6]:
        won(block[0])
    elif block[4]==block[1]==block[7] or block[4]==block[6]==block[2] or block[3]==block[4]==block[5]:
        won(block[4])     
    elif block[8]==block[7]==block[6] or block[8]==block[5]==block[2]:
        won(block[8])   
        
    else :
        print('next turn')    



def game():
    global turn
    global block
    while cont==1:
        pos=int(input('1st player enter position : '))
        if block[pos-1] in range(0,9):
            pass
        else:
            print("already filled")
        block[pos-1]='O'   

        display()

        check()

        if turn==0:
            turn=1
            break

        pos=int(input('2nd player enter position : '))
        block[pos-1]='X'

        check()

        display()

display()
game()        
