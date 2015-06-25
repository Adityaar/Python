##############################################################################
#                                                                            #
##############################################################################

import threading
import sys
import os
import MySQLdb
import random


class Mythread(threading.Thread):
    def __init__(self,db):
        threading.Thread.__init__(self)
        self.db = db
    def run(self):
        run_insert(self.db)

def run_insert(db):
        sql = """insert into SCANS
        select null,concat(
        substring('0123456789abcdefghijklmnopqrstuvwxyz',floor(rand()*36)+1,1),
        substring('0123456789abcdefghijklmnopqrstuvwxyz',floor(rand()*36)+1,1),
        substring('0123456789abcdefghijklmnopqrstuvwxyz',floor(rand()*36)+1,1),
        substring('0123456789abcdefghijklmnopqrstuvwxyz',floor(rand()*36)+1,1),
        substring('0123456789abcdefghijklmnopqrstuvwxyz',floor(rand()*36)+1,1),
        substring('0123456789abcdefghijklmnopqrstuvwxyz',floor(rand()*36)+1,1),
        substring('0123456789abcdefghijklmnopqrstuvwxyz',floor(rand()*36)+1,1),
        substring('0123456789abcdefghijklmnopqrstuvwxyz',floor(rand()*36)+1,1),
        substring('0123456789abcdefghijklmnopqrstuvwxyz',floor(rand()*36)+1,1),
        substring('0123456789abcdefghijklmnopqrstuvwxyz',floor(rand()*36)+1,1),
        substring('0123456789abcdefghijklmnopqrstuvwxyz',floor(rand()*36)+1,1)
        ),null,null,null,null,current_timestamp() ON DUPLICATE KEY UPDATE SCAN_ID = SCAN_ID + 10 """

        #print "thread executing sql:%s"%(sql)
        try:
            cursor = db.cursor()
            cursor.execute(sql)
            cursor.close()
            db.commit()
            db.close()
        except MySQLdb.Error, e:
            print "An error has been passed. %s" %e

def init_thread():
    backgrounds = []
    for db in connections:
       background = Mythread(db)
       background.start()
       backgrounds.append(background)
    for background in backgrounds:
       background.join()

def main():
    try:
        init_thread()
    except:
        print "failed to initiate threads"
    sys.exit(0)

if __name__ == "__main__":
    mysql_host = "10.177.130.34"
    mysql_pass = "admin"
    mysql_user = "root"
    mysql_port = 3306
    mysql_db = "test"
    threads = int(40)

    connections = []
    for thread in range(threads):
      try:
       connections.append(MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_pass, db=mysql_db, port=mysql_port))
      except MySQLdb.Error, e:
       print "Error %d: %s"%(e.args[0], e.args[1])
       sys.exit (1)

    main()
