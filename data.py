from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
import pyautogui

path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

#Localiza na tela o campo Vencimento
# Criando objeto com data atual adcionando 1 mes.
dataatual = datetime.now() + relativedelta(months=2)
# Convertendo no formato desejado DDMMYY.
data1mes = int(dataatual.strftime('%d%m%y'))

#Localiza na tela o campo Vencimento
if pyautogui.locateOnScreen(rf"{path}\campo_vencto_ped_compra.png", confidence=0.9):
    camp_vencto = pyautogui.locateOnScreen(rf"{path}\campo_vencto_ped_compra.png", confidence=0.9)
    time.sleep(2)
    pyautogui.click(camp_vencto)
    #Cola o Nº do Pedido no txt
    time.sleep(2)
    pyautogui.write(str(data1mes))
    