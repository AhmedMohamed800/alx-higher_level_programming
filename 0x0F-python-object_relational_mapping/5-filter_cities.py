#!/usr/bin/python3
""" lists all states with a name starting with N"""

if "__main__" == __name__:
    import MySQLdb
    import sys
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    state_input = sys.argv[4]
    db_connection = MySQLdb.connect(host="localhost", port=3306, user=user,
                                    passwd=password, db=db)
    cursor = db_connection.cursor()
    query = """SELECT cities.name FROM cities
            INNER JOIN states ON states.id=cities.state_id
            WHERE states.name = %s
            ORDER BY cities.id"""
    cursor.execute(query, (state_input,))
    states = cursor.fetchall()
    for state in states:
        print(f"{state[0]}", end="\n" if states[-1][0] == state[0] else ", ")
    db_connection.close()
