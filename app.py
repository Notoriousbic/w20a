import mariadb
import dbcreds


username = input("Please enter your user name: ")
content = input("Please enter your content to be stored in our DB: ")


conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, host = dbcreds.host, port = dbcreds.port, database = dbcreds.database)
cursor = conn.cursor()
cursor.execute("INSERT INTO blog_post(username, content) VALUES(?,?)", [username, content])
conn.commit()
cursor.close
conn.close

posts = input("Would you like to see the blog posts? Y/N?")

# if(posts == "Y"):
#     for post in posts:
#         print(content)

conn = mariadb.connect(user = dbcreds.user, password = dbcreds.password, port = dbcreds.port, host = dbcreds.host, database = dbcreds.database)
cursor = conn.cursor()
cursor.execute("SELECT content FROM blog_post")
content = cursor.fetchall()
for post in posts:
    # print(blog_post.content)
    print(content)
