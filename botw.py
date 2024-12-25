import os
import pyautogui as pg
import time as t
from tkinter.messagebox import askyesnocancel

def autom():   
    try:
        os.startfile("c:/Windows/system32/notepad")
        # pg.locateOnWindow(grayscale= True)
        t.sleep(4)
        pg.write(" CARMO MOTOS LTDA    | CONSORCIO | MOTOS | PECAS | SERVICOS\n\n Atendemos toda regiao do norte de Minas     |    CNPJ: 0000000000    | | C   MG: Montes Claros    \n\n Cliente: \n Contato: \n Endereco: \n Motocicleta:                      Chassis:   O                Placa:          \n Km:      \n Servico:  \n\n\n Observaçoes Gerais:   N                                                                      \n\n\n Mao de Obra: R$      S        Peças: R$           Valor total: ORR$         \n\n Assinatura:                                    Data: __/__/__ \n\n * Concordo e estou ciente Ass: _________________________________________\n\n") # interval= 0.1
        pg.press("enter")
        pg.PAUSE = 4
        pg.hotkey("Ctrl","S")
        pg.PAUSE = 4
        pg.write("teste2")
        pg.PAUSE = 4
        pg.screenshot("tela2.png")
        pg.PAUSE = 4
        pg.press("enter")
        pg.PAUSE = 4
        pg.press("left")
        pg.press("enter")
        pg.PAUSE = 1
        pg.press("esc")
        pg.PAUSE = 1
        pg.hotkey("win","d")
        t.sleep(1)
        pg.alert(title= "Confirmaçao", text="O codigo foi finalizado. Voce ja pode utilizar o computador!")
    except KeyboardInterrupt:
        pg.alert("Falha na execuçao!")
        KeyboardInterrupt


def enviar_msg_whats():
    try:   
        pg.press("winleft")
        t.sleep(4)
        pg.write("Google")
        t.sleep(4)
        pg.press("enter")
        t.sleep(4)
        pg.write("https://web.whatsapp.com/")
        t.sleep(3)
        pg.press("enter")
        t.sleep(30)
        pg.moveTo(200,180, duration=2)
        pg.click()
        pg.write("riva")
        t.sleep(5)
        pg.press("enter")
        pg.write("Ola! Feliz Natal")
        pg.press("enter")
        t.sleep(3)
        pg.screenshot("screen.png")
        t.sleep(1)
        pg.click(1365,1)
        pg.confirm(title= "Confirmaçao",text="O código foi finalizado. Você já pode utilizar o computador!")
        pg.press("esc")
    except KeyboardInterrupt:
        pg.alert("Falha na execuçao!")
        KeyboardInterrupt
 
confirmacao = pg.confirm(title= "Automaçao",text="Ola!\n Deseja iniciar o programa?", buttons=["Bot Serviço", "Bot Whatszapp"])
if confirmacao == "Bot Serviço":
    # pg.hotkey('ctrl', 'shift', 'esc')
    # pg.confirm(title= "Automaçao", text= "O codigo vai começar. Nao utilize nada do computador ate o codigo finalizar!")
    pg.PAUSE = 0.5
    autom()
    
elif confirmacao == "Bot Whatszapp":
    pg.hotkey('ctrl', 'shift', 'esc')
    pg.confirm(title= "Automaçao", text= "O codigo vai começar. Nao utilize nada do computador ate o codigo finalizar!\n Quando necesssario aponte a camera do seu smartphone para o QRCODE na tela e aguarde o Login")
    pg.PAUSE = 0.5
    enviar_msg_whats()