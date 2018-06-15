import gspread
from oauth2client.service_account import ServiceAccountCredentials
#from google.oauth2 import service_account

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

#credentials = service_account.Credentials.from_service_account_file('client_secret.json')
#scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/cloud-platform'])

#client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("temp_data").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
