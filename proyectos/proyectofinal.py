from random import randrange
def print_board():
    for i in range(13):
            if i%4==0:
                print("+",end="")
                for i in range(3):
                    print("-------+",end="")
                print()
            else:
                for i in range(3):
                    print("|       ",end="")
                print("|")

def print_fill_board(board):
    k=-1
    for i in range(13):
            if i%4==0:
                print("+",end="")
                for i in range(3):
                    print("-------+",end="")
                print()
                k+=1
            else:
                l=0
                if i%2==0 and i%4!=0:
                    for i in range(3):
                        print("|  ",board[k][l],"  ",end="")
                        l+=1
                    print("|")
                else:
                    for i in range(3):
                        print("|       ",end="")
                    print("|")

def alter_board(board,n):
    for i in range(3):
        for j in range(3):
            if n==board[i][j]:
                board[i][j]="O"
                return True
    return False

def continuo(board):
    if board[0][0]==board[1][1]==board[2][2]:
        if board[0][0]=="O":
            return [False, "O"]
        else:
            return [False, "X"]
    if board[0][2]==board[1][1]==board[2][0]:
        if board[0][2]=="O":
            return [False, "O"]
        else:
            return [False, "X"]
    if board[0][0]==board[0][1]==board[0][2]:
        if board[0][0]=="O":
            return [False, "O"]
        else:
            return [False, "X"]
    if board[1][0]==board[1][1]==board[1][2]:
        if board[1][0]=="O":
            return [False, "O"]
        else:
            return [False, "X"]
    if board[2][0]==board[2][1]==board[2][2]:
        if board[2][0]=="O":
            return [False, "O"]
        else:
            return [False, "X"]
    if board[0][0]==board[1][0]==board[2][0]:
        if board[0][0]=="O":
            return [False, "O"]
        else:
            return [False, "X"]
    if board[0][1]==board[1][1]==board[2][1]:
        if board[0][1]=="O":
            return [False, "O"]
        else:
            return [False, "X"]
    if board[0][2]==board[1][2]==board[2][2]:
        if board[0][2]=="O":
            return [False, "O"]
        else:
            return [False, "X"]
    return [True, None]

def juega_maquina(board):
    existe=False
    while not existe:
        celda=randrange(1,10)
        for i in range(3):
            for j in range(3):
                if celda==board[i][j]:
                    board[i][j] = "X"
                    existe=True

def juega_jugador(board):
    error=True
    while error:
        try:
            n=int(input("Ingresa tu movimiento: "))
            if n>=0 and n<=10:
                error=False
                if not alter_board(board,n):
                    error=True
                    print("Lo sentimos pero la casilla ya está ocupada")
                
            else: print("Lo sentimos pero el número ha de estar entre 0 y 10")
        except ValueError:
            print("Lo sentimos pero el valor ha de ser un entero mayor que 0 y menor que 10")


board=[[1,2,3],[4,5,6],[7,8,9]]
print("Comienza el juego!")
board[1][1] = "X"
print_fill_board(board)
while continuo(board)[0]:
    juega_jugador(board)
    print_fill_board(board)
    if(continuo(board)[1]=="O"): 
        print("Enhorabuena, has ganado!")
        break
    juega_maquina(board)
    print_fill_board(board)
    if(continuo(board)[1]=="X"): 
        print("Lo sentimos, has perdido")

    
    

    