import os
from tkinter import *
from tkinter import filedialog
from tkinter import Tk
import pyautogui


#Fernando 29/11/2021
def selecAppOuro():
    #Área de trabalho
    filename = filedialog.askopenfilename(initialdir = "/", title = "Selecione o Arquivo", 
                                        filetypes = (("Atalhos",  "*.lnk*"), ("Todos Arquivos", "*.*")))
    os.startfile (rf"{filename}")
