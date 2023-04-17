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
