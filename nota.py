nota = float(input("Digite sua nota: "))


if 6.99 <  nota <= 7:
    print("Recuperação")
elif nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")

with open('pessoa.txt', 'a') as arquivo:
    arquivo.write(str(nota) + "\n") 