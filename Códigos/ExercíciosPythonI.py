# Exercício 1

valorcompra = float(input("Digite o valor da compra: "))
if valorcompra > 100.00 : 
    print("Você tem um desconto disponível!")
else :
    print("Você não tem descontos disponíveis")
    


# Exercício 2
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 // num2
print("Soma=", result1, "\n Subtração=", result2, "\n Multiplicação=", result3, "\n Divisão inteira=", result4)
    


# Exercício 3
id = int(input("Digite o código do vendedor: "))
codpeca = int(input("Digite o código da peça: "))
preco = float(input("Digite o preço unitário da peça: "))
qtd = int(input("Digite a quantidade de peças vendidas: "))

total = qtd * preco
comissao = total * 0.05
print("O total do valor da comissão referente ao vendedor código", id, "é de:", comissao, 
        "\n Código da peça:", codpeca, 
        "\n Valor total da compra: ", total)




#Exercício 4 
valorcarro = float(input("Digite o valor total do carro: "))
valori = valorcarro * 0.45
valorco = (valori + valorcarro) * 0.12
total = valori + valorco + valorcarro
print("Valor do carro sem imposto: ", valorcarro,
        "\n Valor do imposto: ", valori,
        "\n Valor da distribuidora: ", valorco,
        "\n Total do valor do carro: ", total)

 #Exercício 5

nome = (input("Digite seu nome: "))
valor = float(input("Digite seu salário: "))
salario = 0
if salario == 0 and salario <= 1000:
    aumento = valor * 0.20
    salario = valor + aumento
elif salario >= 1000.01 and salario <= 5000:
    aumento = valor * 0.10
    salario = valor + aumento
else:
    aumento = valor * 0.05
    salario = valor + aumento
    
print("Olá,", nome,", seu novo salário é de: ", salario)


#Exercício 6

contador = 1
while contador <= 10:
   print(contador)
   contador += 1


#Exercício 7

for i in range(1,11):
    print(i)
    i += 1


#Exercício 8

contador = 1
soma = 0
while contador <= 5:
    num = int(input("Digite um número: "))
    contador += 1
    soma += num
print("A soma dos números é: ", soma)