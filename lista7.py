def carrinho_montado():
    carro=[]
    x=0
    while x < 3:
        x = x + 1
        print("--- Bem vindo a loja de carro adcione qual marca você deseja buscar: ")
        
        c=input("Digite a marca do carro: ")
        carro.append(c)
        for i in carro:
            print(i)
        carro.sort    
        

carrinho_montado()
        