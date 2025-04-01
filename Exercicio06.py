N1 = float(input("Digite sua Primeira nota: "))
N2 = float(input("Digite sua Segunda nota: "))
N3 = float(input("Digite sua Terceira nota: "))

Media = (N1 + N2 + N3) / 3
if Media >= 7:
    print(f"Aprovado! {Media}")
else:
    if Media <= 4:
        print(f"Reprovado! {Media}")
    else:
        print(f"Em Recuperação! {Media}")
