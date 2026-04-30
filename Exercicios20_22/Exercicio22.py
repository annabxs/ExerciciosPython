try:
    num1 = float(input("Digite o primeiro número:"))
    num2 = float(input("Digite o segundo número:"))
    soma = num1+num2
    print("\n","A soma dos dois números é:",soma)
except ValueError:
    print("\n","Digite um valor válido")

