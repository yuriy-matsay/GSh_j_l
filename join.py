import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account



SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'credentials.json')

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

SPREADSHEET_ID = '1EVZZ0SzX1f_1cyA12VgQa8Q-E8Ujy5--jPq-nLXrRvI'

service = build('sheets', 'v4', credentials=credentials)

sheet = service.spreadsheets()

data_1_values: list = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                         range='data1'
                                         ).execute().get('values', [])

data_2_values: list = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                         range='data2'
                                         ).execute().get('values', [])

result_values = []

for i in range(len(data_1_values)):
    for j in range(len(data_2_values)):
        if str(data_1_values[i][0]) == str(data_2_values[j][0]):
            data_1_values[i][3] = int(data_1_values[i][3]) + int(data_2_values[j][3])
            result_values.append(data_1_values[i])
            break
        elif j == len(data_2_values)-1:
            result_values.append(data_1_values[i])

for e in range(len(data_2_values)):
    for r in range(len(data_1_values)):
        if str(data_2_values[e][0]) == str(data_1_values[r][0]):
            break
        elif r == len(data_1_values)-1:
            result_values.append(data_2_values[e])


request = service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID,
                                                 range='result',
                                                 valueInputOption='RAW',
                                                 body={'values': result_values}
                                                 ).execute()
