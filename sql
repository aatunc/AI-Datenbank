cursor = connection.cursor()
cursor.execute("SELECT * FROM deine_tabelle")
rows = cursor.fetchall()
