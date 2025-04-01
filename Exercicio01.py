nome = input("Insira o seu Nome: ")
idade = int(input("Digite a sua Idade: "))
salario =  float(input("Informe seu Salario: "))


print(f"Seu nome é {nome}, Você tem {idade}, e recebe {salario}, por mês! ")

percentual = float(input("Quantos porcento de aumento você teve: "))
aumento = salario * (percentual/100)
aumento = aumento + salario

print(f"{nome}, você teve um aumento de {aumento} R$ ")