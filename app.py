def lista_de_numeros():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for numero in numeros:
        print(f'.{numero}')

def lista_de_nomes():
    nomes = ['Olavo', 'Millena', 'Nicolas', 'José']

    for nome in nomes:
        print(f'.{nome}')

def lista_ano_nascimento_ano_atual():
    ano = [1998, 2024]

    for data in ano:
        print(f'.{data}')

def calcular_numeros():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultado = 0

    for numero in numeros:
        if numero % 2 != 0:
            resultado = resultado + numero
    
    print(f'O resultado é {resultado}')

def ordem_decrescente():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    numeros_decrescente = sorted(numeros, reverse=True)
    for numero in numeros_decrescente:
        print(numero)

def tabuada():
    numero = int(input('Digite um número qual você queira saber a tabuada de 1 a 10 : '));
    i = 1

    for i in range(11):
        print(numero * i)

tabuada()
