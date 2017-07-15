# Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro N.
def calcularFatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return calcularFatorial(n - 1) * n


# Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência Fibonacci.
def calcularFibo(n):  # sempre começa com 0
    if n == 1 or n == 2:
        return 1
    else:
        return calcularFibo(n - 1) + calcularFibo(n - 2)


# Crie uma função recursiva que receba um número inteiro positivo N e calcule o somatório dos números de 1 a N.
def calcularSoma(n):
   if n == 1:
       return 1
   else:
       return calcularSoma(n - 1) + n


#Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem crescente
vetor = []
def exibirNaturais(n):
    if n == 0:
        vetor.append(n)
        vetor.sort()
        print(vetor)
        return 0
    else:
        vetor.append(n)
        print(vetor)
        return exibirNaturais(n-1)


# Escreva uma função recursiva que calcule a soma dos primeiros n cubos
def calcularSomaCubo(n):
    if n == 1:
        return 1
    else:
        return calcularSomaCubo(n-1) + n**3


