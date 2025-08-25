# %%
import os
import pandas as pd

def formula(x:float):
    return pow(x,2) - 4*x + 3


df = pd.DataFrame(columns=["an", "bn", "f(an)", "f(bn)", "xn", "f(xn)", "E"])

an, bn = 2, 5

df["an"], df["bn"] = [an], [bn]

n = 13

for i in range(n):
    # calcular valores
    fan = formula(an)
    fbn = formula(bn)
    xn = (an + bn) / 2
    fxn = formula(xn)
    E = abs(bn - an) / 2

    # adicionar nova linha
    df.loc[i] = [an, bn, fan, fbn, xn, fxn, E]

    # verificar intervalos
    if fan * fxn < 0:
        bn = xn
    elif fbn * fxn < 0:
        an = xn
    else:
        break  # encontrou raiz exata

arquivo = "teste_numerico.xlsx"

if os.path.exists(arquivo):
    os.remove(arquivo)

df.to_excel(arquivo)

df