import pyautogui
import time

#Métodos de maximizar e minimizar telas

#Implementado - Renan 10/01/2022
#Método Maximiza tela de movimentos do ouro
def maximizaTela():
    #Aperta CTRL + F7 para selecionar a janela e da um doule click
    pyautogui.hotkey('ctrl','f7')
    time.sleep(10)
    pyautogui.click(clicks=2)


#Método Fecha tela de movimentos do ouro
def fechaTela():
    #Aperta o atalho CTRL + F8 para fechar a tela
    pyautogui.hotkey('ctrl','f8')
    time.sleep(5)