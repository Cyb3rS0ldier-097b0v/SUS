#!/bin/python3

import os,sys,webbrowser,platform,time

def comeco():
   os.system("clear")
   print("mostrar todas as senhas? [s/n]")
   pergunta = input(">>> ")

def verificacao():
     if platform.system() == "Windows":
      webbrowser.open_new_tab("https://youtu.be/dQw4w9WgXcQ")
     if platform.system() == "Linux":
      os.system("termux-open-url https://youtu.be/dQw4w9WgXcQ")


os.system("clear")
print("mostrar todas as senhas? [s/n]")
pergunta = input(">>> ")

if pergunta == 'n':
        resposta = print("ok, então thau")

if pergunta == 'n':
        resposta = sys.exit()

if pergunta == 's':
        resposta = verificacao()

else:
        print("sua resposta não foi entendida\nresponda apenas com s (sim) ou n (não)")
        time.sleep(6)
        comeco()
