from utilidades import moeda
from utilidades import dado

p = dado.leia_dinheiro('digite um preço: R$')
moeda.resumo(p, 35, 22)
