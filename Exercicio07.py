Time1 = input("Digite Qual seu TIME: ")
Gols1 = int(input("Digite quantos gols fez o Time1: "))

Time2 = input("Digite Qual seu TIME: ")
Gols2 = int(input("Digite quantos gols fez o Time2: "))

if Gols1 > Gols2:
    print(f" O Vencedor é o: {Time1}")
else:
    if Gols2 > Gols1:
        print(f"O Vencerdor é o: {Time2}")

    else:
        print("EMPATE!")
