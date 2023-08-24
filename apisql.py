import mysql.connector
post = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
)
posting = post.cursor()
if(posting):
    posting.execute("CREATE DATABASE IF NOT EXISTS `university_db`")
    print("Database created.")
else:
    print("not connected.")