import pyodbc 
from Credentials import db_credentials

server = db_credentials().server
database = db_credentials().database    
username = db_credentials().username
password = db_credentials().password
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
