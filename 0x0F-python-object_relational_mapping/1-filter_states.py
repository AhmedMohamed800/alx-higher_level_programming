#!/usr/bin/python3
""" lists all states with a name starting with N"""

if "__main__" == __name__:
    import MySQLdb
    import sys
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    db_connection = MySQLdb.connect(host="localhost", port=3306, user=user,
                                    passwd=password, db=db)
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
            ORDER BY id")
    states = cursor.fetchall()
    for state in states:
        print(f"{state}")
    db_connection.close()
