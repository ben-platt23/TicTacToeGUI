from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe - Ben Platt. X goes first")
root.geometry('400x400')

# game trackers
xturn = True
counter = 0


# disable all buttons
def gameover():
    button1['state'] = DISABLED
    button2['state'] = DISABLED
    button3['state'] = DISABLED
    button4['state'] = DISABLED
    button5['state'] = DISABLED
    button6['state'] = DISABLED
    button7['state'] = DISABLED
    button8['state'] = DISABLED
    button9['state'] = DISABLED


# check for win
def checkwin(button, var):
    global winner
    winner = False
    # check rows
    if button1['text'] == var and button2['text'] == var and button3['text'] == var:
        button1.config(bg='green')
        button2.config(bg='green')
        button3.config(bg='green')
        messagebox.showinfo(title='Winner', message=var+' wins!')
        gameover()
        winner = True
    elif button4['text'] == var and button5['text'] == var and button6['text'] == var:
        button4.config(bg='green')
        button5.config(bg='green')
        button6.config(bg='green')
        messagebox.showinfo(title='Winner', message=var + ' wins!')
        gameover()
        winner = True
    elif button7['text'] == var and button8['text'] == var and button9['text'] == var:
        button7.config(bg='green')
        button8.config(bg='green')
        button9.config(bg='green')
        messagebox.showinfo(title='Winner', message=var + ' wins!')
        gameover()
        winner = True
    # check columns
    elif button1['text'] == var and button4['text'] == var and button7['text'] == var:
        button1.config(bg='green')
        button4.config(bg='green')
        button7.config(bg='green')
        messagebox.showinfo(title='Winner', message=var+' wins!')
        gameover()
        winner = True
    elif button2['text'] == var and button5['text'] == var and button8['text'] == var:
        button2.config(bg='green')
        button5.config(bg='green')
        button8.config(bg='green')
        messagebox.showinfo(title='Winner', message=var+' wins!')
        gameover()
        winner = True
    elif button3['text'] == var and button6['text'] == var and button9['text'] == var:
        button3.config(bg='green')
        button6.config(bg='green')
        button9.config(bg='green')
        messagebox.showinfo(title='Winner', message=var+' wins!')
        gameover()
        winner = True
    # check diagonal
    elif button1['text'] == var and button5['text'] == var and button9['text'] == var:
        button1.config(bg='green')
        button5.config(bg='green')
        button9.config(bg='green')
        messagebox.showinfo(title='Winner', message=var+' wins!')
        gameover()
        winner = True
    # check antidiagonal
    elif button3['text'] == var and button5['text'] == var and button7['text'] == var:
        button3.config(bg='green')
        button5.config(bg='green')
        button7.config(bg='green')
        messagebox.showinfo(title='Winner', message=var+' wins!')
        gameover()
        winner = True


# check for draw
def checkdraw(button, counter):
    if counter == 9:
        button1.config(bg='red')
        button2.config(bg='red')
        button3.config(bg='red')
        button4.config(bg='red')
        button5.config(bg='red')
        button6.config(bg='red')
        button7.config(bg='red')
        button8.config(bg='red')
        button9.config(bg='red')
        messagebox.showinfo(title='Draw!', message='Draw declared!')
        gameover()


# click -> x
def clicked(button):
    global xturn
    global counter
    x = 'X'
    o = 'O'
    if xturn is True and button['text'] == ' ':
        button.config(text='X', padx=46.25)
        xturn = False
        checkwin(button, x)
        counter += 1
        if not winner:
            checkdraw(button, counter)
    elif xturn is False and button['text'] == ' ':
        button.config(text='O', padx=46.25)
        xturn = True
        checkwin(button, o)
        counter += 1
        if not winner:
            checkdraw(button, counter)
    else:
        messagebox.showerror(title='Error', message='That box has already been used')


# buttons
button1 = Button(root, padx=50, pady=50, activebackground='green', text=' ', command=lambda: clicked(button1))  # use lambda: for functions that need to PASS in parameters
button2 = Button(root, padx=50, pady=50, activebackground='green', text=' ', command=lambda: clicked(button2))
button3 = Button(root, padx=50, pady=50, activebackground='green', text=' ', command=lambda: clicked(button3))

button4 = Button(root, padx=50, pady=50, activebackground='green', text=' ', command=lambda: clicked(button4))
button5 = Button(root, padx=50, pady=50, activebackground='green', text=' ', command=lambda: clicked(button5))
button6 = Button(root, padx=50, pady=50, activebackground='green', text=' ', command=lambda: clicked(button6))

button7 = Button(root, padx=50, pady=50, activebackground='green', text=' ', command=lambda: clicked(button7))
button8 = Button(root, padx=50, pady=50, activebackground='green', text=' ', command=lambda: clicked(button8))
button9 = Button(root, padx=50, pady=50, activebackground='green', text=' ', command=lambda: clicked(button9))

# position
button1.grid(row=1, column=1)
button2.grid(row=1, column=2)
button3.grid(row=1, column=3)

button4.grid(row=2, column=1)
button5.grid(row=2, column=2)
button6.grid(row=2, column=3)

button7.grid(row=3, column=1)
button8.grid(row=3, column=2)
button9.grid(row=3, column=3)

# start the program
root.mainloop()
