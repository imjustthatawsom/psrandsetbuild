from tkinter import *
import os.path
import pandas as pd
import json

validfile1 = False
validfile2 = False
validfile3 = False
validfile4 = False

buildjson = {

}


def filevalidator1():
    global validfile1
    if file1_entry.get():
        if os.path.isfile(file1_entry.get()) and file1_entry.get().endswith('.json'):
            file1valid_label.config(text = 'Valid',fg='green')
            validfile1 = True
        else:
            file1valid_label.config(text='Invalid',fg='red')
            validfile1 = False
    else:
        file1valid_label.config(text='Invalid',fg='red')
        validfile1 = False
    return True

def filevalidator2():
    global validfile2
    if file2_entry.get():
        if os.path.isfile(file2_entry.get()) and file2_entry.get().endswith('.json'):
            file2valid_label.config(text = 'Valid',fg='green')
            validfile2 = True
        else:
            file2valid_label.config(text='Invalid',fg='red')
            validfile2 = False
    else:
        file2valid_label.config(text='Invalid',fg='red')
        validfile2 = False
    return True

def filevalidator3():
    global validfile3
    if file3_entry.get():
        if os.path.isfile(file3_entry.get()) and file3_entry.get().endswith('.json'):
            file3valid_label.config(text = 'Valid',fg='green')
            validfile3 = True
        else:
            file3valid_label.config(text = 'Invalid',fg='red')
            validfile3 = False
    else:
        file3valid_label.config(text = 'Valid',fg='green')
        validfile3 = True
    return True

def filevalidator4():
    global validfile4
    if not file4_entry.get():
        file4valid_label.config(text = 'valid',fg='green')
        validfile4 = True
    else:
        if os.path.isfile(file4_entry.get()) and file4_entry.get().endswith('.json'):
            file4valid_label.config(text = 'Valid',fg = 'green')
            validfile4 = True
        else:
            file4valid_label.config(text = 'Invalid',fg='red')
            validfile4 = False
    return True

def combinefiles(file):
    global buildjson
    with open(file,'r+') as g:
        filejson = json.load(g)

    filekeys = list(filejson.keys())
    if 'sets' in filekeys:
        filekeys.remove('sets')
    #I have the keys for the file and buildjson. I will now loop through the keys, compare to buildjson, and see if I need a new line, or if I add to existing
    for i in range(len(filekeys)):
        buildjsonkeys = list(buildjson.keys())
        pokemonname = filekeys[i]
        print(pokemonname)
        #basically, this checks to make sure there is a set present. If there isn't a set, I won't add it. This doubles as nicely cleaning up the json to only contain usable friends.
        setarr = filejson[pokemonname]['sets']
        if len(setarr) > 0:
            #do the adding thing
            if pokemonname in buildjsonkeys:
                #need to append the sets a number of times based on length of the sets array.
                for n in range(len(setarr)):
                    buildjson[pokemonname]['sets'].append(setarr[n]) 
            else:
                pokemonjson = {
                    pokemonname:{'level':filejson[pokemonname]['level'],'sets':[]}
                }
                pokemonjson[pokemonname]['sets'] = filejson[pokemonname]['sets']
                buildjsonstr = str(buildjson)
                pokemonstr = str(pokemonjson)
                buildjsonstr = buildjsonstr[:-1]
                pokemonstr = pokemonstr[1:]
                if len(list(buildjson.keys())) > 0:
                    pokemonstr = ","+pokemonstr
                concatstr = buildjsonstr+pokemonstr
                buildjson = eval(concatstr)
                #Now the pokemon should be added I think
    


            


def startcombination():
    global buildjson
    buildjson = {

    }
    #step 1 is to check if this is a valid action
    filevalidator1()
    filevalidator2()
    filevalidator3()
    filevalidator4()
    if validfile1:
        file1 = file1_entry.get()
        combinefiles(file1)
        if validfile2 and file2_entry.get():
            file2 = file2_entry.get()
        #I have the files, so now let's run the function that will actually start the process
            combinefiles(file2)
        if file3_entry.get() and validfile3:
            file3 = file3_entry.get()
            combinefiles(file3)
        if file4_entry.get() and validfile4:
            file4 = file4_entry.get()
            combinefiles(file4)

        with open('combinedsets.json','w') as test:
            json.dump(buildjson,test)

        combinevalid_label.config(text = 'Combined!',fg='green')
    else:
        combinevalid_label.config(text ='Invalid',fg='red')
    buildjson = {

    }

root = Tk()
root.title('Pokemon Set Combiner')
root.geometry('500x200')
root.iconbitmap('quickball.ico')

#file 1
file1_label = Label(root,text = 'File 1:')
file1_label.place(x=10,y=20)

file1_entry = Entry(root, validate = 'focusout',validatecommand=filevalidator1)
file1_entry.place(x=50,y=22)

file1valid_label = Label(root,text = '')
file1valid_label.place(x=175,y=20)

#file 2
file2_label = Label(root,text = 'File 2:')
file2_label.place(x=10,y=60)

file2_entry = Entry(root, validate = 'focusout',validatecommand=filevalidator2)
file2_entry.place(x=50,y=62)

file2valid_label = Label(root,text = '')
file2valid_label.place(x=175,y=60)

#file 3
file3_label = Label(root,text = 'File 3:')
file3_label.place(x=10,y=100)

file3_entry = Entry(root, validate = 'focusout',validatecommand=filevalidator3)
file3_entry.place(x=50,y=102)

file3valid_label = Label(root,text = '')
file3valid_label.place(x=175,y=100)

#file 4
file4_label = Label(root,text = 'File 4:')
file4_label.place(x=10,y=140)

file4_entry = Entry(root, validate = 'focusout',validatecommand=filevalidator4)
file4_entry.place(x=50,y=142)

file4valid_label = Label(root,text = '')
file4valid_label.place(x=175,y=140)

#big button to combine them!

combine_button = Button(text = 'Combine!',font=('Times New Roman',36),command=startcombination)
combine_button.place(x=225,y=45)

combinevalid_label = Label(text = '')
combinevalid_label.place(x=325,y=150)

root.mainloop()