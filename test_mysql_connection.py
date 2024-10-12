import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
          host='172.29.66.162',
          user='Reza',
          password='*******',
          database='Filmverwaltungsystem'
     )
    return connection

try:
    conn = create_connection()
    print("Verbindung zur MySQL-Datenbank erfolgreich")
    conn.close()
except mysql.connector.Error as err:
    print(f"Fehler: {err}")
