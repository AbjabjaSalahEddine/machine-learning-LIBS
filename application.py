import tkinter as tk
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from tkinter import filedialog, Text
import os
import predictor
import modelsreader


root = tk.Tk()
root.geometry("700x500")
root.title("GUI du programe")
root.resizable(0, 0)

file_path=tk.StringVar()
C={}
LR=LinearRegression()
test=tk.StringVar()

def initialisation():
    file_path=tk.StringVar()
    C={}
    for widget in frame2.winfo_children():
        widget.destroy()


def readmodels():
    LR=modelsreader.make_model()
    label = tk.Label(frame, text="PARFAIT" , bg="white" )
    label.pack()


def readfile():
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("excel csv", "*.csv"), ("all files", "*.*")))
    file_path.set(filename)
    
    if file_path.get()!="":
        
        buttonvisible()

    

def buttonvisible():
    label = tk.Label(frame2, text="le path du fichier : "+file_path.get() , bg="white" )
    label.pack()
    runApps = tk.Button(frame2, text="Lancer la prediction !",
                    pady=10, fg='white', bg="#15a328" , command=predict )
    runApps.pack()
    

def predict():
    pred=predictor.prediction(file_path.get(),modelsreader.make_model())
    C["P"]=pred[0][0]
    C["Mg"]=pred[0][1]
    C["N"]=pred[0][2]
    C["K"]=pred[0][3]
    C["Cu"]=pred[0][4]
    s = "Resultats de la prediction : \n"
    for V in C.keys() :
    	s+="["+V+"] = "+str(C[V])+"\n"
    label = tk.Label(frame2, text=s , bg="white" )
    label.pack()
    



canvas = tk.Canvas(root, height=500, width=700, bg="#15a328")
canvas.pack()

frame = tk.Frame(root, bg="#15a328" )
frame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.8)

prepare = tk.Button(frame, text="preparer l'envirenement", padx=25,
                     pady=10, fg='black', bg="#b3ffd6", command=readmodels )
prepare.pack()


frame1 = tk.Frame(root, bg="#b3ffd6" )
frame1.place(relx=0.1, rely=0.19, relwidth=0.8, relheight=0.2)

cons="consignes :\n le fichier importé doit etre sous le format .csv obigatoirement.\n"
label = tk.Label(frame1, text=cons,bg="#b3ffd6")
label.pack()

frame2 = tk.Frame(root, bg="#b3ffd6")
frame2.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

openFile = tk.Button(frame1, text="Importer le fichier contenant le spectre", padx=25,
                     pady=10, fg='white', bg="#15a328", command=readfile)
openFile.pack()

frame3 = tk.Frame(root, bg="#b3ffd6" )
frame3.place(relx=0.1, rely=0.81, relwidth=0.8, relheight=0.18)
init = tk.Button(frame3, text="REINITIALISER", padx=25,
                     pady=10, fg='white', bg="#15a328", command=initialisation )
init.pack(side="top", expand="yes")


root.mainloop()


