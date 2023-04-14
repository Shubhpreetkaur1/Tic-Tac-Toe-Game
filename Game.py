from tkinter import *
import random

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == playersname[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = playersname[1]
                name.config(text=(playersname[1]+" turn"))

            elif check_winner() is True:
                name.config(text=(playersname[0]+" wins"))

            elif check_winner() == "Tie":
                name.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = playersname[0]
                name.config(text=(playersname[0]+" turn"))

            elif check_winner() is True:
                name.config(text=(playersname[1]+" wins"))

            elif check_winner() == "Tie":
                name.config(text="Tie!")

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="blue")
            buttons[row][1].config(bg="blue")
            buttons[row][2].config(bg="blue")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="blue")
            buttons[1][column].config(bg="blue")
            buttons[2][column].config(bg="blue")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="blue")
        buttons[1][1].config(bg="blue")
        buttons[2][2].config(bg="blue")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="blue")
        buttons[1][1].config(bg="blue")
        buttons[2][0].config(bg="blue")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player

    player = random.choice(playersname)

    name.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

# setup GUI for game
window = Tk()
window.title("Tic-Tac-Toe")
playersname = ["x","o"]
player = random.choice(playersname)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

name = Label(text=player + " turn", font=('consolas',20))
name.pack(side="top")

restart = Button(text="restart", font=('consolas',20), command=new_game)
restart.pack(side="bottom")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=4, height=1,
        command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()
