try:
    valor = float(input("Digite o valor do produto: "))
    qtd = int(input("Digite a quantidade do produto: "))
    total = valor * qtd
    print("\n O valor total da compra foi de: R$", total)
except ValueError:
    print("Erro! Digite valores válidos")
