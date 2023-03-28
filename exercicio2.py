fib = input('Digite seu número para descobrir a sequencia fibonacci: ')
fib = int(fib)#declarei como int pois nao quero entradas com números flutuantes
fib_2 = 0
fib_atual = 1
while True:
    
    while fib_atual < fib:
        proximo_fib = fib_2 + fib_atual
        fib_2 = fib_atual
        fib_atual = proximo_fib    

    if fib_atual == fib:
        print(f"{fib} pertence à sequência de Fibonacci.")
        break
    else:
        print(f"{fib} não pertence à sequência de Fibonacci.")
        break




