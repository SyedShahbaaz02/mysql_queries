import mysql.connector

# Establish a connection to the MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)

cursor = mydb.cursor()

# Create the database
cursor.execute('CREATE DATABASE IF NOT EXISTS ds_blogs')

# Switch to the ds_blogs database
mydb = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password",
    database="ds_blogs"
)

cursor = mydb.cursor()


# cursor.execute("SELECT * FROM posts ")
# rows=cursor.fetchall()
# for row in rows:
#     print(row)



#using Where in query
# cursor.execute("SELECT * FROM posts WHERE author_id=3")
# rows=cursor.fetchall()
# for row in rows:
#     print(row)


#using groupby 
# cursor.execute("SELECT author_id,SUM(num_likes) FROM posts group by author_id ")
# rows=cursor.fetchall()
# for row in rows:
#     print(row)


#using having with group by

# cursor.execute("SELECT author_id,SUM(num_likes) FROM posts group by author_id having SUM(num_likes)>20 ")
# rows=cursor.fetchall()
# for row in rows:
#     print(row)

#using orderby
 
# cursor.execute("SELECT * FROM posts order by num_likes desc")
# rows=cursor.fetchall()
# for row in rows:
#     print(row)

# Commit the changes
# mydb.commit()

# # Close the cursor and connection
# cursor.close()
# mydb.close()
