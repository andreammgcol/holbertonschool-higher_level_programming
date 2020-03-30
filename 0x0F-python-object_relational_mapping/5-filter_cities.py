#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == '__main__':

    mydb = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = mydb.cursor()
    cur.execute("SELECT * FROM cities\
                JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (argv[4], ))
    states = cur.fetchall()
    list_cities = []
    for records in states:
        if records[4] == argv[4]:
            list_cities.append(records[2])
    print(', '.join(list_cities))
    cur.close()
    mydb.close()
