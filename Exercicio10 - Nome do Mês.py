Mes = int(input("Digite o Mês: "))

if Mes >= 1 and Mes <= 12:

    if Mes == 1:
        print(f"Janeiro")
    elif Mes == 2:
        print(f"Fevereiro")
    elif Mes == 3:
        print(f"Março")
    elif Mes == 4:
        print(f"Abril")
    elif Mes == 5:
        print(f"Maio")
    elif Mes == 6:
        print(f"Junho")
    elif Mes == 7:
        print(f"Julho")
    elif Mes == 8:
        print(f"Agosto")
    elif Mes == 9:
        print(f"Setembro")
    elif Mes == 10:
        print(f"Outubro")
    elif Mes == 11:
        print(f"Novembro")
    else:
        print(f"Dezembro")

else:
    print("Mês informado não Existe!")