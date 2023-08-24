import mysql.connector
sequel = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'university_db'
)
poster = sequel.cursor()
if(poster):
    poster.execute("""
                    CREATE TABLE IF NOT EXISTS `api_data`(
                    `Country` VARCHAR(50),
                    `Domains` VARCHAR(50),
                    `Alpha_two_code` VARCHAR(50),
                    `State_province` VARCHAR(50),
                    `Web_pages` VARCHAR(50),
                    `Name` VARCHAR(50)
                    );
    """)
    print("Table created.")
else: 
    print("Table not created.")