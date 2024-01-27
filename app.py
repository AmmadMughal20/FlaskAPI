from flask import Flask, render_template, jsonify, request
import pyodbc
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/page')
def page():
    return render_template('Page.html')

@app.route('/api', methods=[ 'GET', 'POST'])
def api():
    if(request.method == 'GET'):
        dictionary = {
            'name': 'Ammad',
            'age': 27    
        }

        return jsonify(dictionary)
    
    
# @app.route('/users', methods=['GET', 'POST'])
# def users():
#     cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=portfolio.cho0icqkw4r2.us-east-1.rds.amazonaws.com;DATABASE=Portfolio;UID=admin;TrustServerCertificate=yes;PWD=LED5Vredyellowgreen')
#     try:
#         crsr = cnxn.cursor()
#         crsr.execute("SELECT * FROM users")
        
#         columns = [column[0] for column in crsr.description]
#         rows = [dict(zip(columns, row)) for row in crsr.fetchall()]

#         if len(rows) > 0:
#             response_data = {
#                 "status": 200,
#                 "data": rows,
#                 "message": "Data received successfully!"
#             }
#         else:
#             response_data = {
#                 "status": 404,
#                 "data": [],
#                 "message": "No users found!"
#             }

#         return jsonify(response_data)
#     except pyodbc.Error as e:
#         print(e)
#         return jsonify({"status": 500, "message": "Internal Server Error"})
#     finally:
#         crsr.close()
#         cnxn.close()
    
