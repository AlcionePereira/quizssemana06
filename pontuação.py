def mantendo_pontuação(score):
    return acertou + 1

    
score = 0
acertou = 1


print('''Qual personagem de desenho animado diz:
"Olá velhinho" ''')


desenho = str(input('R.').lower().strip())

if desenho == 'pernalonga':
    print('você tem 1 ponto')


else:
    print('Você tem 0 ponto.')
    


módulo = input('Onde fica o módulo math em Python? \nR.')


if módulo == 'biblioteca' and  desenho == 'pernalonga':
    print('Você tem 2 pontos.')
    



elif módulo == 'biblioteca' and desenho != 'pernalonga' or módulo != 'biblioteca' and desenho == 'pernalonga': 
    print('Você tem 1 ponto.')

    
    
else:
    print('Você tem 0 ponto.')
    

print('Quem é o único que merece toda honra e toda glória? ')

criador = input('R.').upper().strip()


if criador == 'DEUS' and módulo == 'biblioteca' and  desenho == 'pernalonga':
    print('Fim de jogo...\nvocê tem 3 pontos.')
    
    

elif criador == 'DEUS' and módulo == 'biblioteca' and desenho != 'pernalonga' or criador == 'DEUS' and desenho == 'pernalonga' and módulo != 'biblioteca':
    print('Fim de jogo...\nVocê tem 2 pontos.')

    

elif criador == 'DEUS' and módulo != 'biblioteca' and desenho != 'pernalonga' or criador != 'DEUS' and módulo != 'biblioteca' and desenho == 'pernalonga' or criador != 'DEUS' and desenho != 'pernalonga' and módulo == 'biblioteca':
   print('Fim de jogo...\nVocê tem 1 ponto.')
    



else:
    print("Fim de jogo...\n .Você tem 0 pontos'")
    







    


    
    




    
   
    




                      



