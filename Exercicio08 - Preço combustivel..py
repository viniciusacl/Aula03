tipo = input("Digite qual o tipo de combustivel:\n"
             "G Para Gasolina\n"
             "E Para Etanol\n")
qtd = float(input("Qauntos Litros: "))
vGas = 5.8
vEtal = 4.9

if tipo == "G":
    valor = vGas * qtd
else:
    valor = vEtal * qtd

print(f"Você gastou R${valor:.2f}")
