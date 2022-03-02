import math
import numpy as np
import decimal
# log = ln
from sympy import Symbol, lambdify, exp, sqrt, log, cos, sin
import pandas as pd

x = Symbol('x')

"""""""""INPUTS"""""""""
# N = número de casas decimais de precisão
N = int(20)
# A = extremo esquerdo
A = decimal.Decimal(0)
# B = extremo direito
B = decimal.Decimal(1)
# adapted from https://stackoverflow.com/a/9877279
# y = função qualquer de x
y = x*exp(x) - 2
""""""""""""""""""

f = lambdify(x, y, 'numpy')
# yprime = f.diff(x)

# Set decimal precision to 2 more than the required significant figures
decimal.getcontext().prec = N + 2

n_list, a_list, b_list, c_list, f_list, e_list = [], [], [], [], [], []

# n = número da repetição do algoritmo, pertence a |N (1,2,3,...)
n = int(0)
a = A
b = B
while(True):
    print(f"Etapa {n} em progresso", flush=True)
    c = (a + b) / 2
    n += 1
    n_list.append(n), a_list.append(a), b_list.append(b), c_list.append(c),
    e = (B - A) / (2**n)
    f_c = f(c)
    f_list.append(f_c), e_list.append(e),
    if f_c > 0:
        b = c
    elif f_c < 0:
        a = c
    else:
        break
    if e < 10**(-N):
        break
print(c)

d = {'n': n_list, 'a': a_list, 'b': b_list,
     'c': c_list, 'f_c': f_list, 'e': e_list}
df = pd.DataFrame(data=d)
print(df)
print(f"`{c_list[-1]}` é a melhor estimativa para a raiz `c` da função `{y}`, com `{N}` casas decimais de precisão.")
