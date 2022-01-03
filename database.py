import mysql.connector

cnn = mysql.connector.connect(user='root', password='aline', host='localhost', database='crud_escola')
cursor = cnn.cursor()