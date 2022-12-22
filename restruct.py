import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
from pprint import pprint


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

result_values = []
NoDiam = 14
k = 0
s = 0
for i in range(0, int(len(data_1_values)/NoDiam)):
    mylist= []
    mylist.append(data_1_values[k][1])
    for j in range(0, NoDiam):
        mylist.append(data_1_values[s][0])
        s += 1
    k += NoDiam
    result_values.append(mylist)

pprint(result_values)

request = service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID,
                                                 range='result',
                                                 valueInputOption='RAW',
                                                 body={'values': result_values}
                                                 ).execute()