def calcular ():
    
    creditos = "Calculadora Simples - Desenvolvida por Anderson G Lignelli"
    
    while True:
        
        print("\n===========================")
        print("***Selecione a operação: ***")
        print(" 1.Soma")
        print(" 2.Subtração")
        print(" 3.Multiplicação")
        print(" 4.Divisão")
        print(" 5.Ptência")
        print(" 6.Raiz Quadrada")
        print(" 0.Sair")
        print("============================")
        print(creditos)
        print("============================")
        opcao =input("Digite o número da opção desejada: ")
        if opcao == '0':
            break
        try:
            if opcao in("1","2","3","4","5"):
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número:"))
                if opcao == '1':
                    resultado = num1 + num2
                elif opcao == '2': 
                    resultado = num1 - num2
                elif opcao == '3': 
                    resultado = num1 * num2      
                elif opcao == '4': 
                    if num2 == 0:
                        print("Erro: Divisão por zero.")
                        continue
                    resultado = num1 / num2
                elif opcao == '5':
                      resultado = num1 ** num2
                elif opcao == '6':
                    num1 = float (input("Digite o número: "))
                    if num1 < 0:
                        print("Erro: Raiz quadrada de zero ou número negativo.")
                        continue 
                    resultado = (num1 ** (1/2))
                else:
                    print("Opção inválida.")
                    continue
                
                print("===================")
                print("Resultado", resultado)
                print("===================")
                
        except ValueError:
            print("Entrada inválida. Digite apaenas números.")
            
            calcular()
       
        



