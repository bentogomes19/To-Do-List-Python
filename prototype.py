# PROTOTIPAÇÃO DO GERENCIADOR DE TAREFAS
# CRIADO PARA APENAS MOSTRAR COMO SERIA O SISTEMA, NÃO HÁ FUNCIONALIDADES APENAS O LAYOUT

import os
from datetime import datetime
# CORESS
RESET = "\x1b[0m"
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'

#def adicionar_tarefa():
#    os.system("clear")
 #   print("SISTEMA DE GERENCIAMENTO DE TAREFAS (TO-DO List) ***")

if "__main__" == __name__:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(RED + "*" * 60 + RESET)
        print(RED + "*** SISTEMA DE GERENCIAMENTO DE TAREFAS (TO-DO List) ***" + RESET)
        print(RED  + "*" * 60 + RESET)
        print("Data de hoje:" + YELLOW + f" {datetime.now().strftime('%d/%m/%Y')}" + RESET)
        print("MENU DE OPÇÕES\n")
        print("[01] - Adicionar Tarefa\n")
        print("[02] - Editar Tarefa\n")
        print("[03] - Excluir Tarefa\n")
        print("[04] - Consultar Tarefas | BUSCAR | FILTRAR\n ")
        print("[05] - Sair do Programa\n")
        print("*" * 60)
        print("Digite uma opção")
        op = input(">> ")
        if op == "1":
            pass
        elif op == "2":
            pass
        elif op == "3":
            pass
        elif op == "4":
            pass
        elif op == "5":
            break
        else:
            input("Código Inválido...Tente Novamente...")
