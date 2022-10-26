import requests
import json
from datetime import datetime
import pandas as pd

# ----------------------------------------------------------------------------------------------------------------------

url = "https://api.hidroview.com.br/o/token/"

payload = "client_id=TOTplk0fseH6SQ3gsh1bswziOchglFxbrPrBrQrs&client_secret=MPb4buMzVYhFxEqtAFOme6y7xJdrt0pcVea5YIvNX" \
          "QhDIupkZThNf1jdZmnWw8Dg6wouN7dKxt6S9j8w8fGz2hHbTqsgQatEK5qlFyomd0WoFMjeNnoGJvgHcOk2s1Pk&grant_type=passwor" \
          "d&username=juliano.baiero%40egesolucoes.com.br&password=jb250181"
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache"
}

response = requests.request("POST", url, data=payload, headers=headers)
out = json.loads(response.text)
data_A = out.get('access_token')

format_date = '%m/%d/%Y %H:%M:%S %p'

data_disp = datetime.now().strftime('%m/%d/%Y %H:%M:%S %p')
print(data_disp)

print(f'AUTHENTICATION: {response.text}' f'\nTOKEN ACCESS:{data_A}')

# ----------------------------------------------------------------------------------------------------------------------
data_ini = '2022-09-25 20:59:00'
date_fim = '2022-09-26 20:59:00'

# ETA = 2287629 / ETE = 2287630

id_disp = 2287629

url = "https://api.hidroview.com.br/v1/reporte/"

payload = f"id_dispositivo={id_disp}&timestamp_dispositivo_ini={data_ini}&timestamp_dispositivo_fim={date_fim}"

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    'Authorization': f"Bearer {data_A}"
}

# ----------------------------------------------------------------------------------------------------------------------

data_request = requests.post(url=url, data=payload, headers=headers)
json_data = json.loads(data_request.text)

# print(json_data)
a = (json_data[1])

json_data = json.loads(data_request.text)
pulse = json_data[0]['pulso'][0]
date_get = (json_data[1])

date_disp = date_get.get('data_hora_dispositivo')


timestamp_disp = date_get.get('timestamp_dispositivo')

df = pd.DataFrame(json_data)

df.head()

# ----------------------------------------------------------------------------------------------------------------------
# DROP COLUMNS FOR ETA#
df = df.drop(columns=['energia_ativa_negativa', 'horimetro', 'entradas_4a20', 'status', 'codigo_erro',
                      'codigo_produto', 'corrente', 'rele', 'timestamp_servidor', 'dia_sem', 'energia_ativa',
                      'fator_potencia_trifasica', 'tensao', 'ct_pulso', 'energia_ativa'])


"""


# DROP COLUMNS FOR ETE#
df = df.drop(columns=['entradas_4a20', 'status', 'codigo_erro', 'rele', 'timestamp_servidor', 'dia_sem',
'ct_pulso', 'codigo_produto'])
"""
# ----------------------------------------------------------------------------------------------------------------------
df['Data_Completa'] = date_disp
df['Data_Dia'] = date_disp
df['Data_Hora'] = date_disp

df = df[['Data_Completa', 'Data_Dia', 'Data_Hora', 'id_dispositivo', 'pulso', 'timestamp_dispositivo']]

df.info()
get_datetime_disp = df.get('data_hora_dispositivo')
get_pulse = df.get('pulso]')
print(f"DEBUGGER ***** {get_pulse}")
get_id_disp = df.get('id_dispositivo')


df.to_csv("AMBEV_DEBUG.csv")
