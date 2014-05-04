__author__ = 'marcos'


import MySQLdb

con = MySQLdb.connect(host='localhost', user='root', passwd='11', db='agenda')

c = con.cursor()

c.execute('SELECT * FROM login')

c.fetchall
