# Tabela para testes e possível implementação futura... convertendo para html.
# Possível forma de passar uma tabela para o pdf.

import pandas as pd
import numpy as np


# Função gera DataFrame com pandas
def gerar_tabela():
    coluna = ["Quantidades"]

    linha = ["Bornes de passagem",
             "Capacitor cilíndrico",
             "Disjuntor",
             "Fusivel",
             "Gavetas",
             "Inversor de frequencia",
             "Modulos mca",
             "Soft-starter",
             "Switch_gerenciavel",
             "Tampa traseira",
             "Tampa lateral"]

    quantidades_dos_itens = np.random.randint(1, 10, 11).reshape(11, 1)

    tabela = pd.DataFrame(data=quantidades_dos_itens,
                          index=linha, columns=coluna)
    print(tabela)
