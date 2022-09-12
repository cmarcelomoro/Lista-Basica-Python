lista = []
def menu():
    print("1 - Adicionar nome na lista")
    print("2 - Excluir nome da lista")
    print("3 - Ver lista")
    print("4 - Sair")
menu()
op = int(input("O que você gostaria de fazer?\n"))
while op != 0:
    match op:
     case 1:
       qtd = int(input("Quantos nomes você gostaria de inserir na lista?\n"))
       for i in range(qtd):
           nome = input("Digite um nome\n")
           lista.append(nome.lower())  ##insere na lista os nomes desejados
       print(lista)
       menu()
       op = int(input("O que você gostaria de fazer?\n"))
     case 2:
        if len(lista) == 0:
            print("A lista está vazia!")
            menu()
            op = int(input("O que você gostaria de fazer?\n"))

        else :
            qtd = int(input("Quantos nomes você gostaria de excluir da lista?\n"))

            i = 0
            for i in range(qtd):  ## percorre a lista e procura o nome para exclusão
                nome = input("Qual nome você quer excluir da lista?\n")
                if nome == lista[i]:
                    lista.remove(nome)
            print("O nome", nome, "foi excluido da lista\n")
            print(lista)
            menu()
            op = int(input("O que você gostaria de fazer?\n"))


     case 3:
        print(lista)
        menu()
        op = int(input("O que você gostaria de fazer?\n"))

     case 4:
         exit()




