
ano = int(input("Digite o ano: "))
anoNasc = int(input("Digite qual ano você nasceu: "))

if (ano - anoNasc >= 16):
    print("Você pode votar este ano!")
else:
    print("Você não pode votar este ano!")