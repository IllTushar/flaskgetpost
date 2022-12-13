import mysql.connector
import json

class model_class():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost",user="root",password="",database="api_pratice")
            self.con.autocommit= True
            self.cur = self.con.cursor(dictionary=True)
            print("Connected")
        except:
            print("Something went wrong")

    def get_all_data(self):
        self.cur.execute("SELECT * FROM student_table")
        result = self.cur.fetchall()
        if len(result)>0:
           return result
        else:
            return "Not Found!!"
    
    def post_all_details(self,data):
        self.cur.execute(f"INSERT INTO student_table(name,email,password) VALUES('{data['name']}','{data['email']}','{data['password']}');")
        return "Request Posted Successful"
