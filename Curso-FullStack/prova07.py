def caucula_media(total_notas, quantidade_provas):   
    #calcula a media aritimetica
    media = total_notas / quantidade_provas
    
    return media

menu = -1

lista_media = []
print("Bem vindo ao sistema de notas")
while menu != 0:
    #cadastrar nota ate pedir para parar
    total_notas = 0
    quantidade_prova = int(input("Digite a quantidade de provas que deseja saber a media: "))
    for i in range(0, quantidade_prova):
        print(f"Digite a {i+1} nota de {quantidade_prova}")
        nota = float(input())
        total_notas += nota
          
    
    lista_media.append(caucula_media(total_notas, quantidade_prova)) 
    
    menu = int(input("Digite 0 para sair ou 1 para continuar"))
  
numero_de_notas = len(lista_media)

for i in range(0, numero_de_notas):
    print(f'A media de nota do {i+1} foi {lista_media[i]}')    

