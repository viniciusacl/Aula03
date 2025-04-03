tipo = input("Digite qual o tipo de combustivel:\n"
             "G Para Gasolina\n"
             "E Para Etanol\n")
qtd = float(input("Qauntos Litros: "))
vGas = 5.8
vEtal = 4.9
valor = 0

if tipo == "G" or tipo == "g":
    valor = vGas * qtd
elif tipo == "E" or tipo == "e":
    valor = vEtal * qtd
else:
    print("Tipo de combustível inválido!")

print(f"Você gastou R${valor:.2f}")

