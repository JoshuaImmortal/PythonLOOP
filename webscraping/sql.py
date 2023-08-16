import mysql.connector
Scrape = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'management_db'
)

cursor = Scrape.cursor()
if(cursor):
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS `content`(
                   `id` INT PRIMARY KEY AUTO_INCREMENT,
                   `note` LONGTEXT
                    )
                   """)
else:
    print("could not create table")