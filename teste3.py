import json

with open('dados.json', 'r', encoding='utf8') as arquivo:
    dic = json.load(arquivo)
media = 0
tam_dic = len(dic)
count = tam_dic
dias = 0
x = min(dic, key=lambda chave: chave['valor'])
y = max(dic, key=lambda chave: chave['valor'])
for i in range(tam_dic):
    if dic[i]['valor'] <= 0:
        count -= 1
        continue
    else:
        media += dic[i]['valor']
media /= count
for j in range(tam_dic):
    if dic[j]['valor'] > media:
        dias += 1

print(
    f'\nO menor valor de faturamento ocorrido em um dia do mês foi no dia'\
    f' {x["dia"]}, com o valor de: R${x["valor"]:.2f}\n\nO maior valor de'\
    f' faturamento ocorrido em um dia do mês, foi no dia {y["dia"]}, com o '\
    f'valor de R${y["valor"]:.2f}.'
      )
print(
    f'\nPor fim, foram ao todo {dias} dias no mês em que o valor do faturamento' \
    f' diário foi superior à média de R${media:.2f} mensal\n'
)