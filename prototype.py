# PROTOTIPAÇÃO DO GERENCIADOR DE TAREFAS
# CRIADO PARA APENAS MOSTRAR COMO SERIA O SISTEMA, NÃO HÁ FUNCIONALIDADES APENAS O LAYOUT

import os
from datetime import datetime
from time import sleep

# CORESS
RESET = "\x1b[0m"
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'

#def adicionar_tarefa():
#    os.system("clear")
 #   print("SISTEMA DE GERENCIAMENTO DE TAREFAS (TO-DO List) ***")

# MENU DO CABEÇALHO SERÁ SEMPRE UTILIZADO NAS FUNÇÕES PARA APARECER NO INICIO
def menu_cabecalho():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(RED + "*" * 60 + RESET)
    print(RED + "*** SISTEMA DE GERENCIAMENTO DE TAREFAS (TO-DO List) ***" + RESET)
    print(RED + "*" * 60 + RESET)

def layout_tarefa(titulo, descricao, data_criacao, data_vencimento, prioridade, categoria, status):
    print("\t [01] TAREFA: " + titulo)
    print(BLUE + "*" * 60 + RESET)
    print("\t [02] DESCRIÇÃO: " + descricao)
    print(BLUE + "*" * 60 + RESET)
    print("\t [03] DATA CRIACAO: " + data_criacao)
    print(BLUE + "*" * 60 + RESET)
    print("\t [04] DATA FINAL: " + data_vencimento)
    print(BLUE + "*" * 60 + RESET)
    print("\t [05] PRIORIDADE: " + prioridade)
    print(BLUE + "*" * 60 + RESET)
    print("\t [06] CATEGORIA: " + categoria)
    print(BLUE + "*" * 60 + RESET)
    print("\t [07] STATUS: " + status)
    print(BLUE + "*" * 60 + RESET)

# LAYOUT PARA APARECER APOS AS INSERÇÕES DOS DADOS DA TAREFA
def layout_add_tarefa(titulo, descricao, data_criacao, data_vencimento, prioridade, categoria, status):
    menu_cabecalho()
    layout_tarefa(titulo, descricao, data_criacao, data_vencimento, prioridade, categoria, status)
    print("PARA VOLTAR AO MENU DIGITE 0: ")

# FUNÇÃO PARA ADICIONAR A TAREFA COM VALIDAÇÕES DE CAMPO
def adicionar_tarefa():
    titulo = " "
    descricao = " "
    data_criacao = " "
    data_vencimento = " "
    prioridade = " "
    categoria = " "
    status = " "
    while True:
        achou = 0 # Variável de validação para o primeiro e segundo while em DATA DE VENCIMENTO E DATA DE CRIAÇÃO
        layout_add_tarefa(titulo, descricao, data_criacao, data_vencimento, prioridade, categoria, status)

        if (titulo != "0") or (descricao != "0") or (data_criacao != "0") or (data_vencimento != "0") or (prioridade != "0") or (categoria != "0") or (status != "0"):
            # TÍTULO
            print(YELLOW + "[01] - TÍTULO" )
            titulo = input(">> ")
            if titulo == "0": # PARA VOLTAR AO MENU PRINCIPAL DO PROGRAMA
                break
            layout_add_tarefa(titulo, descricao, data_criacao, data_vencimento, prioridade, categoria, status)
            # DESCRIÇÃO
            print("[02] - DESCRIÇÃO")
            descricao = input(">> ")
            if descricao == "0": # PARA VOLTAR AO MENU PRINCIPAL DO PROGRAMA
                break

            layout_add_tarefa(titulo, descricao, data_criacao, data_vencimento, prioridade, categoria, status)

            # DATA DE CRIAÇÃO DA TAREFA
            while True:
                data_criacao = input("INFORME A DATA DE CRIAÇÃO | (FORMATO: DD/MM/YYYY): ")
                if data_criacao == "0":
                    achou = 1
                    break
                try:
                    data_valida = datetime.strptime(data_criacao, "%d/%m/%Y")
                    print("Data válida: ", data_valida.strftime("%d/%m/%Y"))
                    layout_add_tarefa(titulo, descricao, data_criacao, data_vencimento, prioridade, categoria, status)
                    break
                except ValueError:
                    layout_add_tarefa(titulo, descricao, data_criacao, data_vencimento, prioridade, categoria, status)
                    print(RED + "FORMATO DE DATA INVÁLIDO... Tente novamente.." + RESET)

            if achou: # PARA VOLTAR AO MENU PRINCIPAL DO PROGRAMA
                break

            # DATA DE VENCIMENTO
            while True:
                data_vencimento = input("INFORME A DATA DE VENCIMENTO | (FORMATO: DD/MM/YYYY): ")
                if data_vencimento == "0":
                    achou = 1
                    break
                try:
                    data_valida = datetime.strptime(data_vencimento, "%d/%m/%Y")
                    layout_add_tarefa(titulo, descricao, data_criacao, data_vencimento, prioridade, categoria, status)
                    print("Data válida: ", data_valida.strftime("%d/%m/%Y"))
                    break
                except ValueError:
                    layout_add_tarefa(titulo, descricao, data_criacao, data_vencimento, prioridade, categoria,
                                      status)
                    print(RED + "FORMATO DE DATA INVÁLIDO... Tente novamente.." + RESET)

            if achou: # PARA VOLTAR AO MENU PRINCIPAL DO PROGRAMA
                break

            # PRIORIDADE
            print("NÍVEL DE IMPORTÂNCIA DA TAREFA: [01] - BAIXO | [02] - MÉDIO | [03] - ALTO\n")
            op = input(">> ")
            if op == '1':
                prioridade = 'BAIXO'
            elif op == '2':
                prioridade = 'MÉDIO'
            elif op == '3':
                prioridade = 'ALTO'
            elif op == '0': # PARA VOLTAR AO MENU PRINCIPAL DO PROGRAMA
                break
            else:
                input(RED + "Entrada Invalida...Tente novamente" + RESET)

            layout_add_tarefa(titulo, descricao, data_criacao, data_vencimento, prioridade, categoria, status)

            # CATEGORIA
            print("[06] - CATEGORIA\n")
            print("[01] - TRABALHO\n")
            print("[02] - PESSOAL\n")
            print("[03] - FÉRIAS\n")
            print("Escolha uma categoria |1|2|3| ou defina uma")
            op = input(">> ")
            if op == '1':
                categoria = 'TRABALHO'
            elif op == '2':
                categoria = 'PESSOAL'
            elif op == '3':
                categoria = 'FRIAS'
            elif op == '0': # PARA VOLTAR AO MENU PRINCIPAL DO PROGRAMA
                break
            else:
                categoria = op

            layout_add_tarefa(titulo, descricao, data_criacao, data_vencimento, prioridade, categoria, status)

            # STATUS
            print("[07] - STATUS")
            print("[01] - PENDENTE\n")
            print("[02] - CONCLUIDA\n")
            print("[03] - EM ANDAMENTO\n")
            print("Escolha uma |1|2|3|:")
            op = input(">> ")

            if op == '1':
                status = 'PENDENTE'
            elif op == '2':
                status = 'CONCLUIDA'
            elif op == '3':
                status = 'EM ANDAMENTO'
            elif op == '0':
                break # PARA VOLTAR AO MENU PRINCIPAL DO PROGRAMA

            layout_add_tarefa(titulo, descricao, data_criacao, data_vencimento, prioridade, categoria, status)

            if (titulo != " ") and (descricao != " ") and (data_criacao != " ") and (data_vencimento != " ") and (prioridade != " ") and (categoria != " ") and (status != " "):
                resp = input("DESEJA CONFIRMAR SEUS DADOS?: ").upper()
                if resp == 'S' or resp == 'SIM' or resp == ' ':
                    # CADASTRANDO OS DADOS
                    print("Dados sendo validados...Aguarde....")
                    sleep(1)
                    # VERIFICAR SE O BANCO DE DADOS ARMAZENOU A TAREFA
                    print("Tarefa Cadastrada com sucesso!")
                    sleep(1)
                    break
                elif resp == 'N' or resp == 'n' or resp == "NAO" or resp == "Não" or resp == "NÃO":
                    continue

        else:
            break


# MENU PRINCIPAL DO SISTEMA
if "__main__" == __name__:
    while True:
        menu_cabecalho()
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
            adicionar_tarefa() # FIX 01
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
