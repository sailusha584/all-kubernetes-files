import os
from flask import Flask, request, render_template
import mysql.connector
app = Flask(__name__)

#color = os.environ.get('APP_COLOR')
DB_HOST= os.environ.get('DB_HOST')
DB_ROOT=os.environ.get('DB_ROOT')
DB_PWD=os.environ.get('DB_PWD')

@app.route("/")
def main():
    #print(color)
    mysql.connector.connect(host='DB_HOST',database='mysql',user='DB_ROOT',password='DB_PWD')
    return render_template('render.html', color=color)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
