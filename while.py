nome = 'Gabriele'
n = 0
novo = ''

while n < len(nome):
    letra = nome[n]
    novo += f'*{letra}'
    n += 1

novo += '*'
print(novo)