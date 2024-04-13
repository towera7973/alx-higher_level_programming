#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn_to_db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur_obj = conn_to_db.cursor()
    cur_obj.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur_obj.fetchall()
    for row in query_rows:
        print(row)
    cur_obj.close()
    conn_to_db.close()
