print("*********************************")
print("Bem vindo ao jogo de adivinhaçao!")
print("*********************************")

numero_secreto = 42

tentativa = int(input("Digite o seu numero: "))

print("Voce Digitou", tentativa)

if (numero_secreto == tentativa):
    print("Voce acertou!!!")
else:
    print("Voce errou!!!")

