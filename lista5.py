def carrinho_compras():
    pc = []
    
    print("--- Seja bem-vindo o loja de python")
    
    while True:
        produto = input("Digite o produto que deseja adcionar ao carrinho caso contrario 'sair': ")
        
        if produto == 'sair':
            break
        
        pc.append(produto)
        print(f"-> {produto} foi adcionado ao carrinho")
    print("\n--- SEU CARRINHO DE COMPRAS ---")
    if len(pc) == 0:
        print("Seu carrinho está vazio")
    else:
         for item in pc:
                print(f"- {item}")
    print(f"\nTotal de itens no carrinho: {len(pc)}")
carrinho_compras()
