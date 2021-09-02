#!/usr/bin/env python
# coding: utf-8

# In[1]:


#imports libraries required for gui
from tkinter import *
from tkinter import messagebox as mb
 
#Global variables used in the game
x=[]
counter=1
player='X'
color='lightgreen'
list1=[['1', '2', '3'],['4', '5', '6'],['7', '8', '9']]      #The cells in the board 
b1,b2,b3,b4,b5,b6,b7,b8,b9=True,True,True,True,True,True,True,True,True  #checks whether the buttons are clicked or not
 
# Exit Game Button fn 
def exit():
    root.destroy()
#function to check if a player won 
def is_win():
    global counter,list1,player
    win=True
    if(counter>5):
        #row win
        for i in [0,1,2]:
            if(list1[i][0]==list1[i][1]==list1[i][2]=='X'):
                mb.showinfo('Winner', 'player 1 wins')
                end()
            if(list1[i][0]==list1[i][1]==list1[i][2]=='O'):
                mb.showinfo('Winner', 'player 2 wins')

 
        #column win
        for i in [0,1,2]:
            if(list1[0][i]==list1[1][i]==list1[2][i]=='X'):
                mb.showinfo('Winner', 'player 1 wins')
                end()
 
            if(list1[0][i]==list1[1][i]==list1[2][i]=='O'):
                mb.showinfo('Winner', 'player 2 wins')
                end()
 
 
        #diagonal win
        if(list1[0][0]==list1[1][1]==list1[2][2]=='X'):
            mb.showinfo('Winner', 'player 1 wins')
            end()
 
        if(list1[0][0]==list1[1][1]==list1[2][2]=='O'):
            mb.showinfo('Winner', 'player 1 wins')
            end()
 
 
        if(list1[0][2]==list1[1][1]==list1[2][0]=='X'):
            mb.showinfo('Winner', 'player 1 wins')
            end()
 
        if(list1[0][2]==list1[1][1]==list1[2][0]=='O'):
            mb.showinfo('Winner', 'player 2 wins')
            end()
 
    if(counter>9):
        mb.showinfo('Tie', 'TIE')
        end()
 # end function is executed after the game ends
def end():
    global list1,counter,b1,b2,b3,b4,b5,b6,b7,b8,b9
    list1=[['1', '2', '3'],['4', '5', '6'],['7', '8', '9']]
    counter=1
    player_ch()
    b1,b2,b3,b4,b5,b6,b7,b8,b9=True,True,True,True,True,True,True,True,True
    but11.config(relief=RAISED,text="   ",bg="skyblue")
    but12.config(relief=RAISED,text="   ",bg="skyblue")
    but13.config(relief=RAISED,text="   ",bg="skyblue")
    but14.config(relief=RAISED,text="   ",bg="skyblue")
    but15.config(relief=RAISED,text="   ",bg="skyblue")
    but16.config(relief=RAISED,text="   ",bg="skyblue")
    but17.config(relief=RAISED,text="   ",bg="skyblue")
    but18.config(relief=RAISED,text="   ",bg="skyblue")
    but19.config(relief=RAISED,text="   ",bg="skyblue")
 # change the player
def player_ch():
    global player, color
    if counter%2==0:
        player='O'
        color='yellow'
    else:
        player='X'
        color='lightgreen'
 # open the game's frame
def to_frame2():
    frame2.pack()
    frame1.forget()
# open the home frame
def to_frame1():
    frame1.pack()
    frame2.forget()
     
 # 9 functions for each button when it's clicked
def but11():
    global counter,list1,b1
    if(b1):
        but11.config(text=player,bg=color)
        but11.config(relief=SUNKEN)
        counter +=1
        list1[0][0]=player
        player_ch()
        b1=False
        is_win()
    else:
        mb.showinfo('Wrong', 'Is pressed before')
 
 
def but12():
    global counter,list1,b2
    if(b2):    
        but12.config(text=player,bg=color)
        but12.config(relief=SUNKEN)
        counter +=1
        list1[0][1]=player
        player_ch()
        b2=False
        is_win()
    else:
        mb.showinfo('Wrong', 'Is pressed before')
def but13():
    global counter,list1,b3
    if(b3):    
        but13.config(text=player,bg=color)
        but13.config(relief=SUNKEN)
        counter +=1
        list1[0][2]=player
        player_ch()
        b3=False
        is_win()
    else:
        mb.showinfo('Wrong', 'Is pressed before')
def but14():
    global counter,list1,b4
    if(b4):    
        but14.config(text=player,bg=color)
        but14.config(relief=SUNKEN)
        counter +=1
        list1[1][0]=player
        player_ch()
        b4=False
        is_win()
    else:
        mb.showinfo('Wrong', 'Is pressed before')
def but15():
    global counter,list1,b5
    if(b5):    
        but15.config(text=player,bg=color)
        but15.config(relief=SUNKEN)
        counter +=1
        list1[1][1]=player
        player_ch()
        b5=False
        is_win()
    else:
        mb.showinfo('Wrong', 'Is pressed before')
def but16():
    global counter,list1,b6
    if(b6):    
        but16.config(text=player,bg=color)
        but16.config(relief=SUNKEN)
        counter +=1
        list1[1][2]=player
        player_ch()
        b6=False
        is_win()
    else:
        mb.showinfo('Wrong', 'Is pressed before')
def but17():
    global counter,list1,b7
    if(b7):
        but17.config(text=player,bg=color)
        but17.config(relief=SUNKEN)
        counter +=1
        list1[2][0]=player
        player_ch()
        b7=False
        is_win()
    else:
        mb.showinfo('Wrong', 'Is pressed before')
def but18():
    global counter,list1,b8
    if(b8):    
        but18.config(text=player,bg=color)
        but18.config(relief=SUNKEN)
        counter +=1
        list1[2][1]=player
        player_ch()
        b8=False
        is_win()
    else:
        mb.showinfo('Wrong', 'Is pressed before')
def but19():
    global counter,list1,b9
    if(b9):
        but19.config(text=player,bg=color)
        but19.config(relief=SUNKEN)
        counter +=1
        list1[2][2]=player
        player_ch()
        b9=False
        is_win()
    else:
        mb.showinfo('Wrong', 'Is pressed before')
 # open the game window
root = Tk()
root.geometry("510x600")
root.title("Tic Tac Toe")
 
# Home Frame
frame1=Frame(root)
frame1.pack()
 
topframe1=Frame(frame1)
topframe1.pack()
bottomframe1 = Frame(frame1)
bottomframe1.pack( side = BOTTOM )
lab01=Label(topframe1,text="X O",font=("Arial",40),fg="Red",pady=100)
but01=Button(bottomframe1,text="START",pady=50,padx=112,border=5,bg='#fff',command=to_frame2)
but02=Button(bottomframe1,text="EXIT",pady=50,padx=114,border=5,bg='#fff',command=exit)
lab02=Label(bottomframe1,text="   ",pady=10)
lab01.pack()
but01.pack()
but02.pack()
lab02.pack()
 
# Game Frame
frame2 = Frame(root)
 
# Creates the 9 buttons for the 9 cells
but11=Button(frame2,text="   ", width=22,height=10,border=5,bg="skyblue",command=but11)
but12=Button(frame2,text="   ", width=22,height=10,border=5,bg="skyblue",command=but12)
but13=Button(frame2,text="   ", width=22,height=10,border=5,bg="skyblue",command=but13)
but14=Button(frame2,text="   ", width=22,height=10,border=5,bg="skyblue",command=but14)
but15=Button(frame2,text="   ", width=22,height=10,border=5,bg="skyblue",command=but15)
but16=Button(frame2,text="   ", width=22,height=10,border=5,bg="skyblue",command=but16)
but17=Button(frame2,text="   ", width=22,height=10,border=5,bg="skyblue",command=but17)
but18=Button(frame2,text="   ", width=22,height=10,border=5,bg="skyblue",command=but18)
but19=Button(frame2,text="   ", width=22,height=10,border=5,bg="skyblue",command=but19)
 
but_bk=Button(frame2,text="Back",width=10,bg='#fff',command=to_frame1)
but_clr=Button(frame2,text="Clear",width=10,bg='#fff',command=end)
# Shows the 9 buttons in the board 
but11.grid(row=1,column=1)
but12.grid(row=1,column=2)
but13.grid(row=1,column=3)
but14.grid(row=2,column=1)
but15.grid(row=2,column=2)
but16.grid(row=2,column=3)
but17.grid(row=3,column=1)
but18.grid(row=3,column=2)
but19.grid(row=3,column=3)
but_bk.grid(row=4,column=3)
but_clr.grid(rows=5,column=3)
 
root.mainloop()


# In[ ]:




