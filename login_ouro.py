import pyautogui
import time
import tkinter



path = (r"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")


def loginOuro():

    #Abrindo o OuroWeb
    time.sleep(10)
    pyautogui.write("custom")
    pyautogui.press('tab')
    pyautogui.write("2wsx@dr5")
    pyautogui.press('enter')
    time.sleep(10)
    if pyautogui.locateOnScreen(rf"{path}\atencao_usu_sem_perm.png", confidence=0.9):
        time.sleep(5)
        pyautogui.press('enter')
        pyautogui.write("cd")
        pyautogui.press('tab')
        pyautogui.write("2wsx@dr5")
        pyautogui.press('enter')
    else:
        time.sleep(1)

    #Minimizar Telas
def fecharCompromissos():
    time.sleep(20)
    if pyautogui.locateOnScreen(rf"{path}\atencao_compromissos.png", confidence=0.9):
        btn_nao = pyautogui.locateOnScreen(rf"{path}\btn_nao.png", confidence=0.9)
        pyautogui.click(btn_nao)
    else:
        time.sleep(5)
    
    #fechar todas as Janelas do OuroNet
def fecharTelasOuroNet():
    time.sleep(40)
    if pyautogui.locateCenterOnScreen(rf"{path}\app_ouronet_laranja.png", confidence=0.9):
        click_ouronet = pyautogui.locateCenterOnScreen(rf"{path}\app_ouronet_laranja.png", confidence=0.9)
        pyautogui.click(click_ouronet, button='right')
        time.sleep(3)
        fech_tod_jan = pyautogui.locateOnScreen(rf"{path}\fech_tod_jan.png", confidence=0.9)
        pyautogui.click(fech_tod_jan)
    else:
        time.sleep(10)

def fecharTelasOuroWeb():
        #Windows + d para minimizar as telas
    pyautogui.hotkey('win','d')
    time.sleep(5)
    #Maximiza a tela do Ouro
    pyautogui.getWindowsWithTitle("Ouro Web ®")[0].maximize()
    #fechar telas OuroWeb
    pyautogui.hotkey('ctrl','f8')
    pyautogui.hotkey('ctrl','f8')
    pyautogui.hotkey('ctrl','f8')
    pyautogui.hotkey('ctrl','f8')
    pyautogui.hotkey('ctrl','f8')                                                                                                                                                                                               
    pyautogui.hotkey('ctrl','f8')
    pyautogui.hotkey('ctrl','f8')
    pyautogui.hotkey('ctrl','f8')
    pyautogui.hotkey('ctrl','f8')
    pyautogui.hotkey('ctrl','f8')
    time.sleep(5)
