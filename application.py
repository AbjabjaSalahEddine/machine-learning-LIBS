import tkinter as tk
import numpy as np
import sklearn
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LinearRegression
from tkinter import filedialog, Text
import os
import predictor
import modelsreader

########## LES CONSTANTES
root = tk.Tk()
root.geometry("700x500")
root.title("GUI du programe")
root.resizable(0, 0)

file_path=tk.StringVar()
C={}
LR=LinearRegression()
test=tk.StringVar()

############################# LES FONCTIONS 
def initialisation():
    file_path=tk.StringVar()
    C={}
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    for widget in frame21.winfo_children():
        widget.destroy()
    for widget in frame22.winfo_children():
        widget.destroy()
    openFile = tk.Button(frame2, text="Importer le fichier contenant le spectre", padx=25,
                     pady=8, fg='white', bg="#15a328", command=readfile)
    openFile.pack(side="top", expand="yes")


def readmodels():
    LR=modelsreader.make_model()
    label = tk.Label(frame, text="PARFAIT" , bg="white" )
    label.pack()
    


def readfile():
    
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("excel csv", "*.csv"),("all files", "*.*")))
    file_path.set(filename)
    
    if file_path.get()!="":
        for widget in frame2.winfo_children():
            widget.destroy()
        buttonvisible()

    

def buttonvisible():
    label = tk.Label(frame2, text="le path du fichier : "+file_path.get()+"", bg="#b3ffd6" )
    label.pack()
    runApps = tk.Button(frame2, text="Lancer la prediction !",
                    pady=10, fg='white', bg="#15a328" , command=predict )
    runApps.pack()
    

def predict():
    for widget in frame2.winfo_children():
        if isinstance(widget, tk.Button):
            widget.destroy()
    pred=predictor.prediction(file_path.get(),modelsreader.make_model())
    C["P"]=pred[0][0]
    C["Mg"]=pred[0][1]
    C["N"]=pred[0][2]
    C["K"]=pred[0][3]
    C["Cu"]=pred[0][4]
    s = "Resultats de la prediction :\n \n"
    for V in C.keys() :
    	s+="["+V+"] = "+"%.2f" % C[V]+"\n"
    label = tk.Label(frame21, text=s , bg="#b3ffd6" , font=("", 12) )
    label.pack()
    fig= plt.Figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(111).plot(predictor.spectre(file_path.get())[1],predictor.spectre(file_path.get())[0])
    graph = FigureCanvasTkAgg(fig, frame22 ) 
    graph.get_tk_widget().pack()

################# LE CODE

canvas = tk.Canvas(root, height=500, width=700, bg="#15a328")
canvas.pack()

frame = tk.Frame(root, bg="#15a328" )
frame.place(relx=0.05, rely=0.02, relwidth=0.88, relheight=0.7)

prepare = tk.Button(frame, text="preparer l'envirenement", padx=25,
                     pady=10, fg='black', bg="#b3ffd6", command=readmodels )
prepare.pack()


frame1 = tk.Frame(root, bg="#b3ffd6" )
frame1.place(relx=0.05, rely=0.145, relwidth=0.9, relheight=0.08)

cons="consignes :\n le fichier importé doit etre sous le format .csv obigatoirement.\n"
label = tk.Label(frame1, text=cons,bg="#b3ffd6" ,font=("", 9) ,fg="red" )
label.pack()

frame2 = tk.Frame(root, bg="#b3ffd6")
frame2.place(relx=0.05, rely=0.239, relwidth=0.9, relheight=0.14)
frame21 = tk.Frame(root, bg="#b3ffd6")
frame21.place(relx=0.05, rely=0.39, relwidth=0.27, relheight=0.46)
frame22 = tk.Frame(root, bg="#b3ffd6")
frame22.place(relx=0.32, rely=0.39, relwidth=0.63, relheight=0.46)

openFile = tk.Button(frame2, text="Importer le fichier contenant le spectre", padx=25,
                     pady=10, fg='white', bg="#15a328", command=readfile)
openFile.pack(side="top", expand="yes")



frame3 = tk.Frame(root, bg="#15a328" )
frame3.place(relx=0.1, rely=0.86, relwidth=0.8, relheight=0.13)
init = tk.Button(frame3, text="REINITIALISER", padx=25,
                     pady=10, fg='white', bg="#15a328", command=initialisation )
init.pack(side="top", expand="yes")

root.mainloop()


