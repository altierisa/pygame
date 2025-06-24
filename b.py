nome = input("Digite o seu nome: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / altura ** 2

print(f' o imc de {nome} é {imc}')