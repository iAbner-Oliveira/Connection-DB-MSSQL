# Importa o módulo pandas
import pandas as pd

# Defina um dicionário contendo dados de Alunos
data = {
        'Nome': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Altura': [5.1, 6.2, 5.1, 5.2],
        'Qualificação': ['Msc', 'MA', 'Msc', 'Msc']
        }

# Converta o dicionário em DataFrame
df = pd.DataFrame(data)

# Declare uma lista que deve ser convertida em uma coluna
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']

# Usando 'Address' como o nome da coluna
# e igualando-o à lista
df['Address'] = address

# observe o resultado
print(df)