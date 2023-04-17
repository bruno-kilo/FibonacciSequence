''' EXERCÍCIOS:

2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
*/

 SOLUÇÃO '''

num = int(input('Digite um número: '))
a, b = 0, 1
fib = [a, b]
while b < num:
    a, b = b, a + b
    fib.append(b)
if num in fib:
    print(f'{num} pertence à sequência de Fibonacci.')
else:
    print(f'{num} não pertence à sequência de Fibonacci.')

'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

 SOLUÇÃO '''    

import json

# Carregando os dados do faturamento mensal a partir de um arquivo JSON
with open('faturamento.json', 'r') as f:
    data = json.load(f)
    faturamento = data['faturamento']

# Calculando o menor e o maior valor de faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# Calculando a média mensal de faturamento
dias_com_faturamento = [dia for dia in faturamento if dia > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Calculando o número de dias com faturamento superior à média mensal
dias_acima_da_media = sum(1 for dia in dias_com_faturamento if dia > media_mensal)

# Imprimindo os resultados
print(f'Menor valor de faturamento: {menor_faturamento}')
print(f'Maior valor de faturamento: {maior_faturamento}')
print(f'Dias com faturamento superior à média mensal: {dias_acima_da_media}')
    
'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

 SOLUÇÃO '''    

# Definindo o dicionário com as informações de faturamento de cada estado
faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calculando o faturamento total mensal da distribuidora
faturamento_total = sum(faturamento_por_estado.values())

# Calculando o percentual de representação de cada estado
percentuais = {}
for estado, faturamento in faturamento_por_estado.items():
    percentuais[estado] = (faturamento / faturamento_total) * 100

# Imprimindo os resultados
for estado, percentual in percentuais.items():
    print('{} - {:.2f}%'.format(estado, percentual))    

    '''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse; 

SOLUÇÃO '''
    
    # Lendo a string de entrada do usuário
string = input('Digite uma string para inverter: ')

# Definindo a string previamente no código
# string = 'Exemplo de string para inverter'

# Criando uma lista vazia para armazenar os caracteres invertidos
caracteres_invertidos = []

# Percorrendo a string de trás para frente e adicionando os caracteres na lista
for i in range(len(string)-1, -1, -1):
    caracteres_invertidos.append(string[i])

# Convertendo a lista de caracteres invertidos para uma string
string_invertida = ''.join(caracteres_invertidos)

# Imprimindo a string invertida
print('A string invertida é:', string_invertida)
