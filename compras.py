import os
import time

os.system('clear')
print('Olá, irei te ajudar a não esquecer o que você deve comprar.')
print('Para começarmos, digite o que você se lembra que está precisando.')
print('Os items devem estar separados por espaços.')

items_iniciais = input('Items: ')
lista = items_iniciais.split()
os.system('clear')

print('Excelente! Sua lista ficou assim:')
index = 0
item = 1
for i in lista:
    print(f'{item}. {lista[index]}')
    index += 1
    item += 1

while True:
    print('O que gostaria de fazer agora?')
    print('1. Adicionar item 2. Remover item 3. Visualizar lista 0. Sair')
    escolha = input()

    index = 0

    if escolha == '1':
        os.system('clear')
        print('Digite o nome dos items que deseja adicionar:')
        itens_adicionados = input()
        items_adicionados = itens_adicionados.split()
        lista += items_adicionados
        print('Itens adicionados com sucesso!')
        time.sleep(3)
        os.system('clear')
    elif escolha == '2':
        os.system('clear')
        print('Digite o indice to item que seja remover:')
        try:
            for i in lista:
                print(f'{index}. {lista[index]}')
                index += 1
            item_remover = int(input())
            del lista[item_remover]
            print('Item removido com sucesso!')
            time.sleep(3)
            os.system('clear')
        except:
            print('O item que você digitou não existe.')
            os.system('clear')
    elif escolha == '3':
        index = 0
        item = 1
        os.system('clear')
        for i in lista:
            print(f'{item}. {lista[index]}')
            index += 1
            item += 1
    elif escolha == '0':
        os.system('clear')
        print('Boas compras! Sua lista ficou assim:')
        print(f'{item}. {lista[index]}')
        break
    else:
        print('Digite uma opção válida!')
        time.sleep(3)
        os.system('clear')
