##############################################################################
#                                                                            #
##############################################################################

import threading
import sys
import os
import random
from memsql.common import database

class Mythread(threading.Thread):
    def __init__(self,conn,tid):
        threading.Thread.__init__(self)
        self.conn = conn
        self.threadid = tid
    def run(self):
        run_insert(self.conn,self.threadid)

def run_insert(db,tid):

        # The below value will be within the range of 1 to 7
        scan_count = random.randint(1,7)        # This is to emulate number of SCANS of a PARCEL before it reaches destination
        scan_hash = ""
        ## Using memsql to generate random SCAN HASH of length 11 chars.

        rand_scan_hash = """ select concat(
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
        ) """

        #sql = """ insert into SCANS select %s,%s,null,%s,null,null,current_timestamp() ON DUPLICATE KEY UPDATE SCAN_ID = SCAN_ID + %s """

        #print "thread %s executing sql:%s"%(id,sql)

        try:
                result = db.get(rand_scan_hash)
                for val in result.values():
                        scan_hash = val

                for scan in range(scan_count):
                        sql = """ insert ignore into SCANS values (%s,"%s",null,%s,null,null,current_timestamp()) """ % (tid+scan,scan_hash,scan+1)
                        db.execute(sql)

                #db.commit()
                db.close()

        except database.MySQLError, e:
            print "An error has been passed. %s" %e


def main():
        '''
                Main procedure where threads are spawned for each connection object
        '''

        try:
                threadList = []
                threadID = 1
                for con in connections:
                        thread = Mythread(con,threadID)
                        thread.start()
                        threadList.append(thread)
                        threadID += 1

                # Wait for all threads/connections to end.

                for thread in threadList:
                        thread.join()


        except:
                print "Failed to create thread"
        sys.exit(0)


def get_connection(host=None, port=None, db="memsql_demo"):
        """ Returns a new connection to the database. """

        memsql_host = "127.0.0.1"
        memsql_pass = ""
        memsql_user = "root"
        memsql_port = 3306

        return database.connect(host=memsql_host, user=memsql_user, password=memsql_pass, database=db, port=memsql_port)


def test_connection():
    try:
        with get_connection(db="information_schema") as conn:
            conn.ping()
    except database.MySQLError:
        print("Unable to connect to MemSQL with provided connection details.")
        print("Please verify that MemSQL is running @ %s:%s" % ('localhost',3306 ))
        sys.exit(1)

def cleanup():
    try:
        with get_connection() as conn:
            conn.query('truncate table SCANS')
    except database.MySQLError:
        pass


if __name__ == "__main__":

        if len(sys.argv) > 1:
                conn_limit = int(sys.argv[1])

                memsql_host = "127.0.0.1"
                memsql_pass = ""
                memsql_user = "root"
                memsql_port = 3306
                memsql_db = "memsql_demo"

                conn_limit = int(sys.argv[1])

                connections = []

                test_connection()
                cleanup()

                for conn in range(conn_limit):
                        try:
                                connections.append(database.connect(host=memsql_host, user=memsql_user, password=memsql_pass, database=memsql_db, port=memsql_port))
                        except database.MySQLError, e:
                                print "Error %d: %s"%(e.args[0], e.args[1])
                                sys.exit (1)
                main()
        else:
                print 'Usage: python threaded.py <number of parallel sessions>'
