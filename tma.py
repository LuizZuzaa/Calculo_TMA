### Coloque quantos atendimentos você realizou no total e depois o programa solicitará o tempo de cada atendimento

def tma(n):
    cont = 0
    total = 0
    while cont < n:
        total += float(input(f'Qual foi o tempo de atendimento para o {cont+1}° contato: '))
        cont += 1
    print(f'O seu tempo médio de atendimento é {total / cont:.2f}')

tma(5)