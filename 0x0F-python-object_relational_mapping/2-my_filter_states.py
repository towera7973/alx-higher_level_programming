#!/usr/bin/python3
"""Script displays all values in states table that match given argument
Takes four arguments:
    mysql username
    mysql password
    database name
    name to match
Connects to default host (localhost) and port (3306)
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn_to_db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur_obj= conn_to_db.cursor()
    query = """
SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(argv[4])
    cur_obj.execute(query)
    query_rows = cur_obj.fetchall()
    for row in query_rows:
        print(row)
    cur_obj .close()
    conn_to_db.close()
