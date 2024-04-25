import pandas as pd
import json

# Carregar o arquivo JSON
with open('contratos.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Converter o JSON em um DataFrame do Pandas
df = pd.json_normalize(data)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('contratos.csv', index=False)

print("Arquivo CSV gerado com sucesso!")
