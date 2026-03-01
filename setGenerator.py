#Hello, if you're reading this, I'm sorry that my code is probably suboptimal. I made it quickly over 2 days to try and get it working so my friends and I could play with it.
#If there are any features that you think would improve this please let me know.
#Please don't distribute this as if you were the one that made it, but please feel free to edit the code to fit what you want.
#Most importantly, please have fun!

from tkinter import *
import pandas as pd
import json
import os.path

pokelist = list(pd.read_csv('pokedex.csv'))
movelist = list(pd.read_csv('moves.csv'))
itemlist = list(pd.read_csv('items.csv'))
abilitylist = list(pd.read_csv('abilities.csv'))
teralist = list(pd.read_csv('teratypes.csv'))

#set all of the varables used to determine whether the program can generate the pokemon is able to be run to false so they can be changed within each function
validpokemon = False
validmove1 = False
validmove2 = False
validmove3 = False
validmove4 = False
validitem = False
validability = False
validtera = False
validfile = False
validlevel = False

#Function to validate the pokemon
def pokemonvalidator():
    global validpokemon
    global pokelist
    if pokemon_entry.get() in pokelist:
        pokevalid_label.config(text = 'Valid',fg = 'green')
        validpokemon = True
    else:
        pokevalid_label.config(text = 'Invalid',fg = 'red')
        validpokemon = False
    return True

#move validators. The program should work just fine if one or more of them are blank.
def move1validator():
    global movelist
    global validmove1
    if move1_entry.get():
        if move1_entry.get() in movelist:
            move1_label.config(text = "Valid",fg='green')
            validmove1 = True
        else:
            move1_label.config(text = 'Invalid',fg='red')
            validmove1 = False
    else:
        move1_label.config(text = 'Invalid',fg='red')
        validmove1 = False
    return True

def move2validator():
    global movelist
    global validmove2
    if move2_entry.get():
        if move2_entry.get() in movelist:
            move2_label.config(text = "Valid",fg='green')
            validmove2 = True
        else:
            move2_label.config(text = 'Invalid',fg='red')
            validmove2 = False
    else:
        move2_label.config(text="Valid",fg = 'green')
        validmove2 = True
    return True

def move3validator():
    global movelist
    global validmove3
    if move3_entry.get():
        if move3_entry.get() in movelist:
            move3_label.config(text = "Valid",fg='green')
            validmove3 = True
        else:
            move3_label.config(text = 'Invalid',fg='red')
            validmove3 = False
    else:
        move3_label.config(text="Valid",fg = 'green')
        validmove3 = True
    return True

def move4validator():
    global movelist
    global validmove4
    if move4_entry.get():
        if move4_entry.get() in movelist:
            move4_label.config(text = "Valid",fg='green')
            validmove4 = True
        else:
            move4_label.config(text = 'Invalid',fg='red')
            validmove4 = False
    else:
        move4_label.config(text="Valid",fg = 'green')
        validmove4 = True
    return True

def itemvalidator():
    global itemlist
    global validitem
    if item_entry.get():
        if item_entry.get() in itemlist:
            itemvalid_label.config(text = "Valid",fg='green')
            validitem = True
        else:
            itemvalid_label.config(text = 'Invalid',fg='red')
            validitem = False
    else:
        itemvalid_label.config(text="invalid",fg = 'red')
        validitem = False
    return True

def abilityvalidator():
    global abilitylist
    global validability
    if ability_entry.get():
        if ability_entry.get() in abilitylist:
            abilityvalid_label.config(text = "Valid",fg='green')
            validability = True
        else:
            abilityvalid_label.config(text = 'Invalid',fg='red')
            validability = False
    else:
        abilityvalid_label.config(text="Invalid",fg = 'red')
        validability = True
    return True

def teravalidator():
    global teralist
    global validtera
    if tera_entry.get():
        if tera_entry.get() in teralist:
            teravalid_label.config(text = 'valid',fg='green')
            validtera = True
        else:
            teravalid_label.config(text = 'invalid',fg='red')
            validtera = False
    else:
        teravalid_label.config(text = 'invalid',fg='red')
        validtera = False
    return True

def filevalidator():
    global validfile
    if outputfile_entry.get():
        if os.path.isfile(outputfile_entry.get()) and outputfile_entry.get().endswith('.json'):
            outputfilevalid_label.config(text = 'Valid',fg='green')
            validfile = True
        else:
            outputfilevalid_label.config(text='Invalid',fg='red')
            validfile = False
    else:
        outputfilevalid_label.config(text='Invalid',fg='red')
        validfile = False
    return True

def levelvalidator():
    global validlevel
    if level_entry.get():
        if level_entry.get().isdigit():
            if int(float(level_entry.get())) > 100 or int(float(level_entry.get())) <= 0:
                levelvalid_label.config(text = 'Invalid',fg='red')
                validlevel = False
            else:
                levelvalid_label.config(text = 'Valid',fg ='green')
                validlevel = True
        else:
            levelvalid_label.config(text = 'Invalid',fg='red')
            validlevel = False
    else:
        levelvalid_label.config(text = 'Valid',fg ='green')
        validlevel = True
    return True


#validation button in order to do the thing that I need it to do
def validatebutton():
    pokemonvalidator()
    move1validator()
    move2validator()
    move3validator()
    move4validator()
    itemvalidator()
    abilityvalidator()
    teravalidator()
    filevalidator()
    levelvalidator()


def modifyjson():
    #Start by grabbing all the information and store them in the variables we will use later
    pokemonname = pokemon_entry.get()
    move1 = move1_entry.get()
    move2 = move2_entry.get()
    move3 = move3_entry.get()
    move4 = move4_entry.get()
    item = item_entry.get()
    ability = ability_entry.get()
    tera = tera_entry.get()
    outputfile = outputfile_entry.get()

    #now lets open the json file
    with open(outputfile,'r+') as f:
        outputjson = json.load(f)

    #Next, lets create the array for the moves. Because you can leave some of the moves blank, I need to do some weird stuff here
    #initialize array to just be 0 so that I can easily work with it
    movearr = [move1]
    if move2_entry.get():
        movearr.append(move2)
    if move3_entry.get():
        movearr.append(move3)
    if move4_entry.get():
        movearr.append(move4)
    #now I've created movearr, this will be used later when generating the json file

    #technically, tera and ability are also arrays, so lets make those arrays
    teraarr = [tera]
    abilityarr = [ability]

    #Perfect, now we should have everything to make the json file
    set2addjson = {"sets":{"role":item,
                            "movepool":movearr,
                            "abilities":abilityarr,
                            "teraTypes":teraarr
    }
    }
    #We've made the json, now I need to check if the pokemon isn't in the system. If not in system, I have to add it using this weird work around
    keys = outputjson.keys()
    if pokemonname not in keys:
        #From here I'm copying the code that I've already written elsewhere and adapting it for here
        if not level_entry.get():
            addpokemon_label.config(text = 'Not in system, add level.',fg='red')
            return
        levelnum = int(float(level_entry.get()))
        #Have the level, now I want to create the json that adds the pokemon to the system
        newpokemonjson = {
            pokemonname:{"level":levelnum,"sets":[]}
        }
        #Made the json, now I convert it into a string
        newpokemonstr = str(newpokemonjson)
        #also need to turn the original file into a string
        outputstr = str(outputjson)
        outputstr = outputstr[:-1]
        newpokemonstr = newpokemonstr[1:]
        concatstr = outputstr+","+newpokemonstr
        outputjson = eval(concatstr)
    #Ok, that should create the the json file that contains the new pokemon
    #Now let's go ahead and add the set. First I need to check if there's a set alerady, otherwise I need to do some dumb cleanup stuff
    if len(outputjson[pokemonname]["sets"]) == 0:
        outputjson[pokemonname]["sets"] = ["placeholder"]
        outputjson["sets"] = outputjson[pokemonname]["sets"].append(set2addjson["sets"])
        outputjson[pokemonname]["sets"] = outputjson[pokemonname]["sets"][1:]
    else:
        outputjson["sets"] = outputjson[pokemonname]["sets"].append(set2addjson["sets"])
    #and now, after all of this, I should have the json file edited, and ready to save.
    with open(outputfile,'w') as g:
        json.dump(outputjson,g)
    addpokemon_label.config(text='Success',fg='green')





    

def addpokemon():
    validatebutton()
    if validpokemon and validmove1 and validmove2 and validmove3 and validmove4 and validitem and validability and validtera and validfile and validlevel:
        modifyjson()

    else:
        addpokemon_label.config(text = 'Error',fg = 'red')

    

root = Tk()
root.title('Pokemon Set Generator')
root.geometry('750x500')
root.iconbitmap('pokeball.ico')

title_label = Label(root,text = "Pokemon Set Generator",font=("Times New Roman",28),anchor='n')
title_label.place(x=200,y=0)

#throwing in a validation button because this stupid thing sucks and can't just work normally for 2 seconds.
validation_button = Button(root,text='Validate',command=validatebutton,font=("Times New Roman",16))
validation_button.place(x=330,y=60)

#All the information for creating the pokemon name validator.
pokemon_label = Label(root,text = "Pokemon:")
pokemon_label.place(x=10, y=110)

pokemon_entry = Entry(root,validate = 'focusout',validatecommand=pokemonvalidator)
pokemon_entry.place(x=75,y=112)

pokevalid_label = Label(root,text = "")
pokevalid_label.place(x=200,y=110)

#Moves for the pokemon
moves_label = Label(root,text="Moves:")
moves_label.place(x=10,y = 150)

move1_entry = Entry(root,validate = 'focusout',validatecommand=move1validator)
move1_entry.place(x=60,y=152)
#text box approximately 124 in size
move2_entry = Entry(root,validate = 'focusout',validatecommand=move2validator)
move2_entry.place(x=204,y=152)

move3_entry = Entry(root,validate = 'focusout',validatecommand=move3validator)
move3_entry.place(x=348,y=152)

move4_entry = Entry(root,validate = 'focusout',validatecommand=move4validator)
move4_entry.place(x=492,y=152)

#offset by 37
move1_label = Label(root,text="")
move1_label.place(x=97,y=172)

move2_label = Label(root,text = "")
move2_label.place(x=241,y=172)

move3_label = Label(root,text = "")
move3_label.place(x=385,y=172)

move4_label = Label(root,text = "")
move4_label.place(x=529,y=172)

#this is where the item goes
item_label = Label(root,text = 'Item:')
item_label.place(x=10,y=205)

item_entry = Entry(root,validate = 'focusout',validatecommand=itemvalidator)
item_entry.place(x=50,y=207)

itemvalid_label = Label(root,text = "")
itemvalid_label.place(x=180,y=205)

#for the ability
ability_label = Label(root,text = "Ability:")
ability_label.place(x=10,y= 245)

ability_entry = Entry(root,validate = 'focusout',validatecommand=abilityvalidator)
ability_entry.place(x=60,y=247)

abilityvalid_label=Label(root,text='')
abilityvalid_label.place(x=190,y=245)

#for tera
tera_label = Label(root,text = 'Tera Type:')
tera_label.place(x=10,y=285)

tera_entry = Entry(root,validate='focusout',validatecommand = teravalidator)
tera_entry.place(x=75,y=287)

teravalid_label = Label(root,text = '')
teravalid_label.place(x=205,y=285)

#for output file

outputfile_label = Label(root,text ='Output File:')
outputfile_label.place(x=10,y=325)

outputfile_entry = Entry(root,validate='focusout',validatecommand = filevalidator)
outputfile_entry.place(x=85,y=327)

outputfilevalid_label = Label(root,text = '')
outputfilevalid_label.place(x=215,y=325)

addpokemon_button = Button(text='Add Pokemon!',command=addpokemon,font=('Times New Roman',36))
addpokemon_button.place(x=275,y=225)

addpokemon_label = Label(root,text = '',font=("Times New Roman",18))
addpokemon_label.place(x=415,y=325)

level_label = Label(root,text = 'Level:')
level_label.place(x=10,y=360)

level_entry = Entry(root, validate='focusout',validatecommand = levelvalidator)
level_entry.place(x=55,y=362)

levelvalid_label = Label(root,text = '')
levelvalid_label.place(x=185,y=360)

root.mainloop()