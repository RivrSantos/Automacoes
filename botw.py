import os
import pyautogui as pg
import time as t
from tkinter.messagebox import askyesnocancel

def autom():   
    try:
        os.startfile("c:/Windows/system32/notepad")
        t.sleep(4)
        pg.write(" Data: __/__/__ \n\n * Concordo e estou ciente Ass: ___________\n\n") # escreva seu documento aqui
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
        pg.write("fulano") # voce pode buscar por contato ou grupo sw WhatsApp
        t.sleep(5)
        pg.press("enter")
        pg.write("Ola! ") # escreva a mensagem que deseja enviar
        pg.press("enter")
        t.sleep(3)
        pg.screenshot("screen.png")
        t.sleep(1)
        pg.click(1365,1) # verifique a resoluçao do seu monitor para configurar o movimento do mouse
        pg.confirm(title= "Confirmaçao",text="O código foi finalizado. Você já pode utilizar o computador!")
        pg.press("esc")
    except KeyboardInterrupt:
        pg.alert("Falha na execuçao!")
        KeyboardInterrupt
 
confirmacao = pg.confirm(title= "Automaçao",text="Ola!\n Deseja iniciar o programa?", buttons=["Bot Serviço", "Bot Whatszapp"])
if confirmacao == "Bot Serviço":
    # pg.hotkey('ctrl', 'shift', 'esc')
    pg.PAUSE = 0.5
    autom()
    
elif confirmacao == "Bot Whatszapp":
    pg.hotkey('ctrl', 'shift', 'esc')
    pg.confirm(title= "Automaçao", text= "O codigo vai começar. Nao utilize nada do computador ate o codigo finalizar!\n Quando necesssario aponte a camera do seu smartphone para o QRCODE na tela e aguarde o Login")
    pg.PAUSE = 0.5
    enviar_msg_whats()
