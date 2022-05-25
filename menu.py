# Impotação das bibliotecas necessarias para criar o arquivo de LOG
import logging
from datetime import datetime

# Salvar a data de hoje em uma variavel
today = datetime.now()
#formatação da data e hora
logdt = today.strftime(" %d.%b.%Y - %H-%M-%S")

#Tentar executar essa ação
try:
    #Importação da bibliotecas necessarias para execução do programa
    import tkinter as tk
    from tkinter import *
    from PIL import Image, ImageTk
    import time
    import pyautogui
    import os
    import logging
    from datetime import datetime
    from tkinter import Tk
    from tkinter import messagebox
    from tkinter import filedialog
    #from cadastro_empresa import *
    #from cadastro_produto import *
    #from cadastro_orcamento import *
    #from cadastro_pedido_venda import *
    #from cadastro_pedido_venda_simples import *
    #from cadastro_venda_saida import *
    #from maximiza_fecha import *
    #from editar_orcamento import *
    #from editar_pedido_venda import *
    #from editar_pedido_venda_simples import *
    #from editar_pedido_venda_simples import *
    #from cancela_venda_saida import *
    #from pedido_venda_baseado import *
    #from importa_orcamento_pedido_venda import *

    #Caminho para imagens do Servidor
    path = (rf"\\vm-srvfile01\Testes\Projeto-automacao\Teste Automatizado OuroWeb\bin\project\tests\img")

    #Função para fechar telas do ouroweb e ouronet
    def clsouro():
        #localiza icone do ouroweb na tela
        ouroweb = pyautogui.locateOnScreen(rf"{path}\barra_app_ouroweb.png", confidence=0.9)
        #clica na imagem do ouroweb
        pyautogui.click(ouroweb)
        time.sleep(2)
        #Verifica se mensagem aparece na tela
        if pyautogui.locateOnScreen(rf"{path}\atencao_compromissos.png", confidence=0.9):
            atencao_compromissos = pyautogui.locateOnScreen(rf"{path}\atencao_compromissos.png", confidence=0.9)
            #Tecla para selecionara a opção "Não" da mensagem
            pyautogui.press("n")
            time.sleep(2)
        #Fechar telas do OuroWeb
        pyautogui.hotkey('ctrl', 'f8')
        pyautogui.hotkey('ctrl', 'f8')
        pyautogui.hotkey('ctrl', 'f8')
        pyautogui.hotkey('ctrl', 'f8')
        pyautogui.hotkey('ctrl', 'f8')
        time.sleep(1)
        #Abrir Menu Principal do OuroWeb
        pyautogui.hotkey('ctrl', '1')
        time.sleep(2)
        time.sleep(1)
        #Verificar se há janelas do OuroNet aberto com icone laranja
        if pyautogui.locateOnScreen(rf"{path}\app_ouronet_laranja.png", confidence=0.9):
            clsouronet = pyautogui.locateOnScreen(rf"{path}\app_ouronet_laranja.png", confidence=0.9)
            #Clicar no icone do OuroNet com botão direito
            pyautogui.click(clsouronet, button='right')
            time.sleep(1)
            #Caso seja mais de uma janela a mensagem para fechar será "Fechar todas as Janelas"
            if pyautogui.locateOnScreen(rf"{path}\cls_all_win.png", confidence=0.9):
                close = pyautogui.locateOnScreen(rf"{path}\cls_all_win.png", confidence=0.9)
            #Caso seja uma janela a mensagem para fechar será "Fechar Janela"
            elif pyautogui.locateOnScreen(rf"{path}\cls_one_win.png", confidence=0.9):
                close = pyautogui.locateOnScreen(rf"{path}\cls_one_win.png", confidence=0.9)
            time.sleep(1)
            #Clicar na mensagem
            pyautogui.click(close)
        #Verificar se há janelas do OuroNet aberto com icone normal
        elif pyautogui.locateOnScreen(rf"{path}\app_ouronet.png", confidence=0.9):
            clsouronet = pyautogui.locateOnScreen(rf"{path}\app_ouronet.png", confidence=0.9)
            #Clicar no icone do OuroNet com botão direito
            pyautogui.click(clsouronet, button='right')
            time.sleep(1)
            #Caso seja mais de uma janela a mensagem para fechar será "Fechar todas as Janelas"
            if pyautogui.locateOnScreen(rf"{path}\cls_all_win.png", confidence=0.9):
                close = pyautogui.locateOnScreen(rf"{path}\cls_all_win.png", confidence=0.9)
            #Caso seja uma janela a mensagem para fechar será "Fechar Janela"
            elif pyautogui.locateOnScreen(rf"{path}\cls_one_win.png", confidence=0.9):
                close = pyautogui.locateOnScreen(rf"{path}\cls_one_win.png", confidence=0.9)
            time.sleep(1)
            #Clicar na mensagem
            pyautogui.click(close)

    #================================================ Criação do Tooltip ================================================#

    try:
        # for Python2
        import Tkinter as tk
    except ImportError:
        # for Python3
        import tkinter as tk

    class CreateToolTip(object):
        """
        create a tooltip for a given widget
        """
        def __init__(self, widget, text='widget info'):
            self.waittime = 500     #miliseconds
            self.wraplength = 180   #pixels
            self.widget = widget
            self.text = text
            self.widget.bind("<Enter>", self.enter)
            self.widget.bind("<Leave>", self.leave)
            self.widget.bind("<ButtonPress>", self.leave)
            self.id = None
            self.tw = None

        def enter(self, event=None):
            self.schedule()

        def leave(self, event=None):
            self.unschedule()
            self.hidetip()

        def schedule(self):
            self.unschedule()
            self.id = self.widget.after(self.waittime, self.showtip)

        def unschedule(self):
            id = self.id
            self.id = None
            if id:
                self.widget.after_cancel(id)

        def showtip(self, event=None):
            x = y = 0
            x, y, cx, cy = self.widget.bbox("insert")
            x += self.widget.winfo_rootx() + 25
            y += self.widget.winfo_rooty() + 20
            # creates a toplevel window
            self.tw = tk.Toplevel(self.widget)
            # Leaves only the label and removes the app window
            self.tw.wm_overrideredirect(True)
            self.tw.wm_geometry("+%d+%d" % (x, y))
            label = tk.Label(self.tw, text=self.text, justify='left',
                           background="#feffeb", relief='solid', borderwidth=1,
                           wraplength = self.wraplength)
            label.pack(ipadx=1)

        def hidetip(self):
            tw = self.tw
            self.tw= None
            if tw:
                tw.destroy()

    #================================================== Janela Padrão ==================================================#
    
    window = Tk()
    #Titulo da janela
    window.title('Automação de Testes')
    #Bloquear ajuste de tamanho da janela
    window.resizable(width=False, height=False)
    #Menor tamanho possivel da janela
    window.minsize(430, 250)
    #Tamanho Inicial da Janela
    window.geometry('430x250')
    #Posição Inicial da Janela
    window.eval('tk::PlaceWindow . center')

    #======================================== Novos Testes serão inseridos aqui ========================================#

    #Declarar variaveis dos teste (Exemplo: varXXXXXXX = tk.IntVar)
            
    varcadastroEmpresas = tk.IntVar()
    varcadastroProd = tk.IntVar()
    varcadastroOrc = tk.IntVar()
    varcadastroPedVenda = tk.IntVar()
    varcadastroPedVendaSimples = tk.IntVar()
    varcadastroVendaSaida = tk.IntVar()

    #Checkboxes dos testes

    #Criação do checkbox
    cadastroEmpresaschkbx = tk.Checkbutton(window, text='Cadastro Empresas',variable=varcadastroEmpresas, onvalue=1, offvalue=0)
    cadastroEmpresaschkbx.pack()
    #Criação do Tooltip
    cadastroEmpresas_ttp = CreateToolTip(cadastroEmpresaschkbx, \
    "Os metódos a serem executados são respectivamente: \n "
    "-cadastroEmpresas() \n ")
    #Posição do checkbox
    cadastroEmpresaschkbx.place(x=10, y=10)

    #Criação do checkbox
    cadastroProdchkbx = tk.Checkbutton(window, text='Cadastro Produto',variable=varcadastroProd, onvalue=1, offvalue=0)
    cadastroProdchkbx.pack()
    #Criação do Tooltip
    cadastroProd_ttp = CreateToolTip(cadastroProdchkbx, \
    "Os metódos a serem executados são respectivamente: \n "
    "-cadastroProd() \n "
    "-alterarProd() \n "
    "-duplicarProd(). \n ")
    #Posição do checkbox
    cadastroProdchkbx.place(x=10, y=30)

    #Criação do checkbox
    cadastroOrcchkbx = tk.Checkbutton(window, text='Cadastro Orçamento',variable=varcadastroOrc, onvalue=1, offvalue=0)
    cadastroOrcchkbx.pack()
    #Criação do Tooltip
    cadastroOrc_ttp = CreateToolTip(cadastroOrcchkbx, \
    "Os metódos a serem executados são respectivamente: \n "
    "-cadastroOrc() \n "
    "-editaOrc(). \n ")
    #Posição do checkbox
    cadastroOrcchkbx.place(x=10, y=50)

    #Criação do checkbox
    cadastroPedVendachkbx = tk.Checkbutton(window, text='Cadastro Pedido de Venda',variable=varcadastroPedVenda, onvalue=1, offvalue=0)
    cadastroPedVendachkbx.pack()
    #Criação do Tooltip
    cadastroPedVenda_ttp = CreateToolTip(cadastroPedVendachkbx, \
    "Os metódos a serem executados são respectivamente: \n "
    "-cadastroPedVenda() \n "
    "-editaPedVend() \n "
    "-pedVendBaseado() \n "
    "-importaOrcPedVend(). \n ")
    #Posição do checkbox
    cadastroPedVendachkbx.place(x=10, y=70)

    #Criação do checkbox
    cadastroPedVendaSimpleschkbx = tk.Checkbutton(window, text='Cadastro Pedido de Venda Simples',variable=varcadastroPedVendaSimples, onvalue=1, offvalue=0)
    cadastroPedVendaSimpleschkbx.pack()
    #Criação do Tooltip
    cadastroPedVendaSimples_ttp = CreateToolTip(cadastroPedVendaSimpleschkbx, \
    "Os metódos a serem executados são respectivamente: \n "
    "-cadastroPedVendaSimples() \n "
    "-editaPedVendSimp() \n ")
    #Posição do checkbox
    cadastroPedVendaSimpleschkbx.place(x=10, y=90)

    #Criação do checkbox
    cadastroVendaSaidachkbx = tk.Checkbutton(window, text='Cadastro de Venda/Saida',variable=varcadastroVendaSaida, onvalue=1, offvalue=0)
    cadastroVendaSaidachkbx.pack()
    #Criação do Tooltip
    cadastroVendaSaida_ttp = CreateToolTip(cadastroVendaSaidachkbx, \
    "Os metódos a serem executados são respectivamente: \n "
    "-cadastroVendaSaida() \n "
    "-cancelaVendSaid() \n ")
    #Posição do checkbox
    cadastroVendaSaidachkbx.place(x=10, y=110)

    #Função chamada pelo botão

    def login():
        global y
        y = 5
        if pyautogui.locateOnScreen(rf"{path}\scr_login.png", confidence=0.9):
            time.sleep(y)
            pyautogui.getWindowsWithTitle("Ouro Web ®")[0].maximize()
            pyautogui.write('custom')
            pyautogui.press('tab')
            pyautogui.write('2wsx@dr5')
            pyautogui.press('Enter')
            if pyautogui.locateOnScreen(rf"{path}\atencao_usu_sem_perm.png", confidence=0.9):
                time.sleep(5)
                pyautogui.press('enter')
                pyautogui.write("cd")
                pyautogui.press('tab')
                pyautogui.write("2wsx@dr5")
                pyautogui.press('enter')
        else:
            time.sleep(y)
            y+=10
            login()
        time.sleep(15)

    #Encontra Base aberta
    def openouro():

        hoje = datetime.now()
        datalog = hoje.strftime(" %d.%b.%Y - %H-%M-%S")

        try:
            if pyautogui.locateOnScreen(rf"{path}\barra_app_ouroweb.png", confidence=0.9):
                pyautogui.alert("Os testes irão começar, por favor não mexa no TECLADO ou MOUSE durante os testes. Clique em OK para iniciar.")
                time.sleep(5)
                clsouro()
                time.sleep(5)
                tst_func()
            else:
                pyautogui.alert(text='Não foi encontrada uma base aberta, favor selecione a base de uma empresa', title='Base não encontrada', button='OK')
                browseFiles()
        except Exception as error:
            logging.basicConfig(filename = rf'./Log/Logging{datalog}.log', level = logging.INFO)
            logging.exception(str(error))

    #busca de arquivo, para iniciar base, caso não haja base aberta
    def browseFiles():
        filename = filedialog.askopenfilename(initialdir = "/",
                                                title = "Selecione o Arquivo",
                                                filetypes = (("Atalhos", "*.lnk*"), ("Todos Arquivos", "*.*")))
        if (filename == ""):
            pyautogui.alert(text='Selecione um Local Valido', title='Local Invalido', button='OK')
        else:
            pyautogui.alert("Os testes irão começar, por favor não mexa no TECLADO ou MOUSE durante os testes. Clique em OK para iniciar.")
            if (varcadastroEmpresas.get() == 0) and (varcadastroProd.get() == 0) and (varcadastroOrc.get() == 0) and  (varcadastroPedVenda.get() == 0) and (varcadastroPedVendaSimples.get() == 0) and (varcadastroVendaSaida.get() == 0):
                pyautogui.alert("Não foi selecionado nenhum módulo para testar, o sistema irá apenas iniciar o OuroWeb.")
            pyautogui.hotkey('win', 'd')
            time.sleep(1)
            os.startfile (rf"{filename}")
            login()
            time.sleep(15)
            clsouro()
            time.sleep(5)
            tst_func()

    #Execução baseada nos checkboxes
    def tst_func():
        ouroweb = pyautogui.locateOnScreen(rf"{path}\barra_app_ouroweb.png", confidence=0.9)
        print('Inicio das funções')
        if (varcadastroEmpresas.get() == 1):
            pyautogui.click(ouroweb)
            pyautogui.getWindowsWithTitle("Ouro Web ®")[0].maximize()
            time.sleep(2)
            cadastroEmpresas()
            time.sleep(2)
            clsouro()
            time.sleep(5)
        if (varcadastroProd.get() == 1):
            pyautogui.click(ouroweb)
            pyautogui.getWindowsWithTitle("Ouro Web ®")[0].maximize()
            time.sleep(2)
            cadastroProd()
            time.sleep(2)
            alterarProd()
            time.sleep(2)
            duplicarProd()
            time.sleep(2)
            clsouro()
            time.sleep(5)
        if (varcadastroOrc.get() == 1):
            pyautogui.click(ouroweb)
            pyautogui.getWindowsWithTitle("Ouro Web ®")[0].maximize()
            time.sleep(2)
            cadastroOrc()
            time.sleep(2)
            editaOrc()
            time.sleep(2)
            clsouro()
            time.sleep(5)
        if (varcadastroPedVenda.get() == 1):
            pyautogui.click(ouroweb)
            pyautogui.getWindowsWithTitle("Ouro Web ®")[0].maximize()
            time.sleep(2)
            cadastroPedVenda()
            time.sleep(2)
            editaPedVend()
            time.sleep(2)
            #pedVendBaseado()
            #time.sleep(2)
            #importaOrcPedVend()
            #time.sleep(2)
            clsouro()
            time.sleep(5)
        if (varcadastroPedVendaSimples.get() == 1):
            pyautogui.click(ouroweb)
            pyautogui.getWindowsWithTitle("Ouro Web ®")[0].maximize()
            time.sleep(2)
            cadastroPedVendaSimples()
            time.sleep(2)
            editaPedVendSimp()
            time.sleep(2)
            clsouro()
            time.sleep(5)
        if (varcadastroVendaSaida.get() == 1):
            pyautogui.click(ouroweb)
            pyautogui.getWindowsWithTitle("Ouro Web ®")[0].maximize()
            time.sleep(2)
            cadastroVendaSaida()
            time.sleep(2)
            cancelaVendSaid()
            time.sleep(2)
            clsouro()
            time.sleep(5)
        if (varcadastroEmpresas.get() == 0) and (varcadastroProd.get() == 0) and (varcadastroOrc.get() == 0) and  (varcadastroPedVenda.get() == 0) and (varcadastroPedVendaSimples.get() == 0) and (varcadastroVendaSaida.get() == 0):
            pyautogui.alert("O Sistema foi inicializado, recomenda-se iniciar um teste padrão, caso contrario, favor fechar o aplicativo de Automação")

    #===================================================================================================================#

    # Create a photoimage object of the image in the path
    image1 = Image.open("setor-de-testes-branco1.png")
    test = ImageTk.PhotoImage(image1)

    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(rely=0, relx=1, x=-10, y=10, anchor=NE)

    botao = Button(window, text='Testa Ouro', command=openouro)
    botao.pack()
    botao.place(rely=1, relx=1, x=-10, y=-10, anchor=SE)
    lbl_ver = Label(window, text='Versão 1.0.0')
    lbl_ver.place(rely=1, relx=0, x=5, y=-5, anchor=SW)
    window.mainloop()

except Exception as e:
    logging.basicConfig(filename = rf'{path}/Log/Logging{logdt}.log', level = logging.DEBUG)
    #logging.debug('Here you have some information for debugging.')
    #logging.info('Everything is normal.')
    #logging.warning('Something unexpected but not important happend.')
    #logging.error('Something unexpected and important happened.')
    #logging.critical('A critical error happend and the code cannot run!')
    logging.exception(str(e))
