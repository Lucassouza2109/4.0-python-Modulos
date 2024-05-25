# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime

from dateutil.relativedelta import relativedelta

valor_total = 1_000_000 # Valor do Emprestimo
data_emprestimo = datetime(2020, 12, 20) # Data do Emprestimo
delta_anos = relativedelta(years=5) # Acrescimo de +5 Anos - Tempo para Pagamento.
data_final = data_emprestimo + delta_anos # Diferenca de Anos. 

data_parcelas = []
data_parcela = data_emprestimo

while data_parcela < data_final: 
    # enquanto a data da parcela = data emprestimo,  for menor que a data fim.
    data_parcelas.append(data_parcela) # adiciona na lista : data_parcela, a parcela.
    data_parcela += relativedelta(months=+1) # acrescenta +1 mes. 

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas

for data in data_parcelas: # para cada data na lista = data_parcelas.
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}') # FORMATACAO. 

print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)


