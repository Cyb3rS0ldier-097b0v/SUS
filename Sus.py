#!/bin/python3

import os,sys,time


def SUS():
      os.system("termux-open-url https://youtu.be/YFGZURDRsuE")



def susNormal():
      os.system("termux-open-url https://youtu.be/0bZ0hkiIKt0")



def instalacao():
     print("voce ja tem você já tem instalado o termux-api no seu termux?\nse não, deseja instalar? [s/jt (ja tenho)/n]")
     pergunta1 = input(">>> ")




os.system("clear")
print("voce ja tem você já tem instalado o termux-api no seu termux?\nse não, deseja instalar? [s/jt (ja tenho)/n]")
pergunta1 = input(">>> ")

if pergunta1 == 's':
        resposta = os.system("apt install termux-api -y")

if pergunta1 == 's':
        resposta = os.system("apt install figlet -y")

if pergunta1 == 'n':
        resposta = print("ok")

if pergunta1 == 'n':
        resposta = sys.exit()

if pergunta1 == 'jt':
        resposta = print("blz")



else:
        print("sua resposta não foi entendida\nresponda apenas com S para sim, N para nao e jt para se voce ja tem")
        time.sleep(9)
        os.system("clear")
        instalacao()


def sus():
        os.system("clear")
        print("vc ta muito sus[s(sus)/n(não)]")

time.sleep(2)
os.system("clear")
print("vc ta muito sus[s(sus)/n(não)]")
pergunta = input(">>> ")

if pergunta == 'n':
        resposta = print("ok, então thau")

time.sleep(1)
if pergunta == 'n':
        resposta = SUS()

if pergunta == 's':
        resposta = susNormal()

if pergunta == 'sus':
        resposta = susNormal()

else:
        print("sua resposta não foi entendida\nresponda apenas com s (sim) ou n (não)")
        time.sleep(6)
        sus()

os.system("clear")
os.system("figlet SUS")
