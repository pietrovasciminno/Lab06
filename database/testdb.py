import mysql.connector

try:
    cnx = mysql.connector.connect(
        host="localhost",  # o 127.0.0.1
        port=3306,
        user="root",       # XAMPP default
        password="",       # XAMPP default
        database="autonoleggio",
        use_pure=True
    )
    print("Connessione al DB OK ✅")
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM automobile")
    rows = cursor.fetchall()
    print("Trovati record:", len(rows))
    for r in rows:
        print(r)
    cursor.close()
    cnx.close()

except mysql.connector.Error as err:
    print("Errore connessione:", err)