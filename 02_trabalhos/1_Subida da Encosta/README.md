# Trabalho 1: Relatório

A Aplicação da técnica Subida da Encosta ao problema do caixeiro viajante consistiu em:

1 - Organizar as cordenadas do arquivo em um dicionário, em que, a ordem que as cordenadas são inseridas determina o percurso.

2 - A partir do (1) dicionário com as cordenadas, produzir novos dicionários atravez das operações definidas nos requisitos da atividade.

A solução consiste em um programa em python dividido em dois arquivos: operacoes.py e solution.py

    operacoes.py define 8 funcoes que intercambiadas costituem 8 variações da técnica Subida da Enconsta

        initial_1(n) :  Tem como parametro o nome de um arquivo. Essa função ler o arquivo e organiza
                        as cordenadas em um dicionario, as keys das cordenadas são letras do alfabeto. Retorna um dicionario com as cordenadas.

        initial_2(n) :  Recebe como parametro um dicionário. Essa função salva as keys do 
                        dicionário em uma lista, então permuta de maneira aleatória os elementos dessa lista e a apatir dela, monta outro dicionário usando as keys em posições randomizadas com as cordenadas do dicionário parametro, retorna esse dicionário.
        
        op_1(n)      :  Recebe um dicionário como parametro. Sorteia dois números aleatório dentre o
                        intervalo de 0 ao número de cordenadas no dicionário, salva as keys do dicionário em uma lista, troca os elementos referente ao indice dos dois números sorteados e apartir da nova lista, monta um novo dicionário com as a lista de indices trocados e retorna uma lista com essa dicionário e os índices trocados.
        
        op_2(n)      :  Recebe um dicionário como parametro. Sorteia dois números aleatórios dentre
                        o intervalo de 0 ao número de cordenadas no dicionário, salva as keys do dicionário. Gera uma lista com keys apatir das condições abaixo, inverte a ordem da lista de tras para frente, então cria uma nova lista intercalando os elementos da lista invertida com a lista keys do dicionário, com critério similar aos definidos abaixo. Monta um dicionário apartir da nova lista e retorna uma lista com esse dicionário e os números sorteados.

                            Se o primeiro número sorteado for menor que o segundo, então monta uma lista comecando elemento com indice igual ao primeiro número até o elemento com indice igual ao segundo número.
                            
                            Se o primeiro número for maior que o segundo, monta uma lista a partir do elemento de indice do primeiro número até o ultimo elemento e concatena com uma lista que começa do elemento de indice 0 até o elemento com indice do segundo número.

        randomNeighbor_op1(n) : Recebe uma lista com um dicionario e uma lista de dois números, a
                                partir de uma lista com as keys do dicionário, remove os elementos referente aos dois números recebido como parametro... retorna uma lista com trinta dicionarios com as keys que não correspondem aos indices recebidos como parametro permutados.

        randomNeighbor_op2()  : .. retorna uma lista com 30 dicionários com os
        
        path()                : Recebe como parametro um dicionario e retorna uma string com as keys
                                desse dicionario em ordem.


        

    solution.py define 4 funções referente aos requisitos da atividade, e a main.
        
        variacao_1(n)  : Recebe um dicionário como parametro, implementa a variaçao 1 e 5 da
                         atividade.
        
        variacao_2(n)  : Recebe um dicionário como parametro, implementa a variaçao 2 e 6 da
                         atividade.
                         
        variacao_3(n)  : ...
        variacao_4(n)  : Recebe um dicionário como parametro, implementa a variaçao 4 e 8 da
                         atividade.

        main()         :

