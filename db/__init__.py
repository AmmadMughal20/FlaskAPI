import pyodbc

def db_connection():
    conn = None
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=portfolio.cho0icqkw4r2.us-east-1.rds.amazonaws.com;DATABASE=Portfolio;UID=admin;TrustServerCertificate=yes;PWD=LED5Vredyellowgreen')
    except pyodbc.Error as e:
        print(e)
    return conn