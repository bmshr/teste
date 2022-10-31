import time
import random

def criptografia():
    global texto
    global chave
    chave = random.randint(1, 1000)
    mensagem = ""
    arq = open("mensagem_criptografada.txt", "w")
    texto = input("\nO'que você deseja criptografar? ")
    for i in texto:
        mensagem = mensagem + str(ord(i)* chave)
    arq.write(mensagem)
    arq.close()

def descriptografia():
    mensagem = ""
    arq = open("mensagem_descriptografada.txt", "w")
    for i in texto:
        mensagem = mensagem + chr(ord(i))
    arq.write(mensagem)
    arq.close()
    
titulo1 = "------------------------"
titulo2 = "PROGRAMA DE CRIPTOGRAFIA"

print(f"{titulo1.center(50)} \n{titulo2.center(50)} \n{titulo1.center(50)}")
print("\n1 - Criptografia \n2 - Descriptografia \n3 - Sair")

opcao = int(input("\nDigite a opção que você deseja: "))

while opcao <= 3 or opcao > 3:
    
    if opcao > 3 or opcao < 1:
        print("\nOpção inválida.")
        time.sleep(2)
        
    elif opcao == 1:
        confirmar = input("\nDigite [s] para confirmar ou [n] para voltar: ")
        
        if confirmar == "s" or confirmar == "S":
            criptografia()
            print("\nCriando arquivo com sua mensagem", end="")

            for i in range(0, 3):
                time.sleep(1)
                print(".", end="")

            time.sleep(1)
            print("\nPronto!")

            confirmar = input("\nVocê deseja ler sua mensagem criptografada? Digite [s] ou [n]: ")

            if confirmar == "s" or confirmar == "S":
                arq = open("mensagem_criptografada.txt", "r")
                msg = arq.readlines()
                print(f"\n{msg}")
                arq.close()
                time.sleep(4)
                
    elif opcao == 2:
        confirmar = input("\nDigite [s] para confirmar ou [n] para voltar: ")

        if confirmar == "s" or confirmar == "S":
            descriptografia()
            print("\nDescriptografando sua mensagem", end="")

            for i in range(0, 3):
                time.sleep(1)
                print(".", end="")

            time.sleep(1)
            print("\nPronto!")

            confirmar = input("\nVocê deseja ler sua mensagem descriptografada? Digite [s] ou [n]: ")

            if confirmar == "s" or confirmar == "S":
                arq = open("mensagem_descriptografada.txt", "r")
                msg = arq.readlines()
                print(f"\n{msg}")
                arq.close()
                time.sleep(4)
                
    elif opcao == 3:
        confirmar = input("\nDigite [s] para confirmar ou [n] para voltar: ")  

        if confirmar == "s" or confirmar == "S":
            break
            
    print("\n1 - Criptografia \n2 - Descriptografia \n3 - Sair")
    opcao = int(input("\nDigite a opção que você deseja: "))
 
