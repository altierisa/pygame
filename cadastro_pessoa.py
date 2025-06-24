nome = input('Digite o nome: ')
email = input("Digite o email: ")

with open('pessoa.txt', 'a') as arquivo:
    arquivo.write(nome + " / contato: " + email + "\n")
