print(''' 'Teste de  conhecimentos bíblicos:
Quem negou Jesus 3 vezes?.

a) Mateus
b) Pedro
c) Judas  ''')


negou = input('R.').upper().strip()

if negou == 'PEDRO' or negou == 'Mateus' or negou == 'Judas':
    print('continuando...')
    
    
else:
    print('Você não escolheu nehuma das opções acima.')

print(''' ' Qual é o primeiro livro da bíblia?
a) Apocalipse
b) Genesis
d) Êxodo ''')


livro = input('R. ').upper().strip()

if livro == 'GENESIS' or livro == 'Apocalipse' or livro == 'Êxodo' :
    print('Segura essa ansiedade')

else:
    print("Você precisar ler mais a bíblia.")

print(''' Última perguntinha, essa é a mai difícil.
Qual é o nome da esposa de Abraão?
a) Sara
b) Noemi
c) Rute ''')

esposa = input('R .').upper().strip()


if esposa == 'SARA' and  livro == 'GENESIS' and negou == 'PEDRO':
    print('Muito bem!')


else:
    print('Tente novamnete')




    
    

    



















    
    
          
