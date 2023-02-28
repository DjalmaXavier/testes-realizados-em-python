dic = [
    {
    'Estado': 'SP',
    'Faturamento': 67836.43
     }, 
    {
    'Estado': 'RJ',
    'Faturamento': 36678.66
    },
    {
    'Estado': 'MG',
    'Faturamento':  29229.88
    }, 
    {
    'Estado': 'ES',
    'Faturamento' : 27165.48
    },
    {
    'Estado': 'Outros',
    'Faturamento': 19849.53
    }
    ]

total = 0

for i in (range(len(dic))):
    total += dic[i]['Faturamento']

for x in (range(len(dic))):
    porcentagem = (100 * dic[x]['Faturamento']) / (total)
    print(f'{dic[x]["Estado"]} representa {porcentagem:.1f}% do valor total')
print(f'\nValor total = {total}')