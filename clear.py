import mysql.connector as mysql

def main():    
    
    #tworzymy połączenie
    my_connection = mysql.connect(
    host="giniewicz.it",
    user="team9",
    password="te@mqP@ss"
    )

    cursor = my_connection.cursor()
    
    #czyścimy bazę
    with open('DataBaseSchema/clear_database.txt') as file:
        a = file.read()

    execs = a.split(';')

    for item in execs:
        item = item.replace('\n', ' ')
        if len(item) == 0:
            pass
        else:
            cursor.execute(item)
            
   
    #zapisujemy zmiany
    my_connection.commit()
    cursor.close()
    my_connection.close()
    
    
    
    
if __name__ == "__main__":
    main()