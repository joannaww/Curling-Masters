

import mysql.connector as mysql

from generators import *

from fill import *


def main():    
    
    #tworzymy połączenie
    my_connection = mysql.connect(
    host="giniewicz.it",
    user="team9",
    password="te@mqP@ss"
    )

    cursor = my_connection.cursor()
    

    #tworzymy tabele
    with open('DataBaseSchema/curlingmasters_create.sql') as file:
        a = file.read()

    execs = a.split(';')

    for item in execs:
        item = item.replace('\n', ' ')
        if len(item) == 0:
            pass
        else:
            cursor.execute(item)
    
    #wypełniamy bazę
    fill(cursor)
    
    #zapisujemy zmiany
    my_connection.commit()
    cursor.close()
    my_connection.close()
    

if __name__ == "__main__":
    main()