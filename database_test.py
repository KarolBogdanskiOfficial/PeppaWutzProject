
import mysql.connector as sql


db = sql.connect(host = "localhost", user = "root", passwd = "Montekija3")

mcr = db.cursor()               #my cursor

mcr.execute("SHOW DATABASES")
