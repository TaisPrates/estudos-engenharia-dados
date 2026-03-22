import pandas as pd
import numpy as np

# --- 1. SIMULAÇÃO DE DADOS BRUTOS  ---
data = {
    'Paciente': ['Ana Silva', 'Bruno Costa', 'Carlos Oliveira', 'Ana Silva', np.nan],
    'Data_Vacinacao': ['2023-01-15', '15/02/2023', '2023-03-10', '2023-01-15', '2023-05-20'],
    'Idade': [25, -5, 45, 25, 30],
    'Dose': ['1ª Dose', '1a dose', '2ª DOSE', '1ª Dose', '1ª Dose'],
    'Cidade': ['Lisboa', 'Porto', 'lisboa', 'Lisboa', 'Coimbra']
}

df_bruto = pd.DataFrame(data)
print("--- Dados Brutos (Sujos) ---")
print(df_bruto, "\n")

# --- 2. LIMPEZA ---

# A. Remover duplicados
df_limpo = df_bruto.drop_duplicates()

# B. Tratar valores nulos
df_limpo = df_limpo.dropna(subset=['Paciente'])

# C. Corrigir erros de lógica (Idade não pode ser negativa)
df_limpo.loc[df_limpo['Idade'] < 0, 'Idade'] = 0 # Ou colocar a média

# D. Padronizar textos (Colocar tudo em maiúsculas e corrigir variações)
df_limpo['Cidade'] = df_limpo['Cidade'].str.capitalize()
df_limpo['Dose'] = df_limpo['Dose'].str.upper().replace({'1A DOSE': '1ª DOSE'})

# E. Formatar Datas
df_limpo['Data_Vacinacao'] = pd.to_datetime(df_limpo['Data_Vacinacao'], errors='coerce')

# F. Adiciona nova coluna chamada pais e preenche todas as linhas com "Brasil".
df_limpo['Pais'] = 'Brasil'

print("--- Dados Limpos e Processados ---")
print(df_limpo)

# --- 3. EXPORTAÇÃO ---
df_limpo.to_csv("relatorio_final_saude.csv", index=False)
print("\nFicheiro 'relatorio_final_saude.csv' gerado com sucesso!")