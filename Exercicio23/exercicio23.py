i = -1
alunos = []
while True:
    try:
        i +=1   
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Digite uma idade válida")
            continue
    
        nota = int(input("Digite sua nota: "))
        if nota > 10 or nota < 0:
            print("Nota inválida!")
            continue
        
        alunos = [
            'nome' : nome,
            'idade' : idade,
            'nota' : nota
        ]
        def situacao():
            if nota >= 7:
                return "Aprovado"
            elif nota >= 5 and nota < 7:
                return "Recuperação"
            else:
                return "Reprovado"
            
            

        print("Olá,",alunos['nome'],"\n","Você tem:", alunos["idade"], "anos", "\n", "Sua nota é:",alunos['nota'], "\n Situação:", situacao())
        
        c = input("Deseja continuar? (s/n)")
        
    except ValueError:
        print("Erro: Digite um valor válido!")
    
    def media_sala():
        media_alunos = 0
        for i in alunos:
            media_alunos+= i['nota']
    # c = continuar
    if c == "n":
        media_sala()
    elif c == "s":
        continue
    else:
        print("Digite um valor válido")
        continue
    
    
