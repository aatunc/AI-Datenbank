import psycopg2
connection = psycopg2.connect(
    dbname="deine_db_name",
    user="dein_benutzername",
    password="dein_passwort",
    host="localhost",
    port="5432"
)
