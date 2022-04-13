import sqlite3
try:
    connection = sqlite3.connect('database.db')
    while True:
        inp = int(input())
        if inp==1:
            query = """SELECT A.id,BD.B,A.A 
                       FROM BD JOIN A ON BD.id=A.id 
                       WHERE BD.TYME = (SELECT MAX(BD.TYME) FROM BD) 
                       ORDER BY D;"""
        elif inp==2:
            query = """SELECT [//I/I/I]||'-'||[I+I] 
                       FROM I 
                       ORDER BY rowid DESC 
                       LIMIT 1;"""
        elif inp==9:
            break
        cursor = connection.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        for line in res:
            print(line)
        cursor.close()


except sqlite3.Error as error:
    print("Connection Error: ", error)
    
finally:
    if (connection):
        connection.close()
