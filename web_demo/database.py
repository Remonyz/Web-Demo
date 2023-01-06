import sqlite3

def item_search(item):
    conn = sqlite3.connect('item.db') #makes the database
    cursor = conn.cursor() #make cursor to tell databse what you want to do
    cursor.execute("SELECT * from items WHERE item_name = (?)", (item,)) #WHY DO I NEED COMMA HERE
    # cursor.execute('SELECT * from items WHERE item_name = "Ham"')
    # items = cursor.fetchall()[1]
    # for item in items:
    #     print(item)

    
    
    # conn.commit()

    # conn.close()

    return (cursor.fetchall()[0])

#create a table
# cursor.execute("""CREATE TABLE items (
#     item_name TEXT,
#     price TEXT
# )

# """)
def register_user(user, password):
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE user (
        username TEXT,
        password TEXT
        )
        """)
    cursor.execute("INSERT INTO user VALUES (?,?)", user, password)
    return (cursor.fetchall())

def list_users():
    conn = sqlite3.connect('item.db') #makes the database
    cursor = conn.cursor() #make cursor to tell databse what you want to do
    # cursor.execute("SELECT * from items WHERE item_name = (?)", (item,))
    cursor.execute('SELECT * FROM users')
    # items = cursor.fetchall()[1]
    # for item in items:
    #     print(item)

    
    
    # conn.commit()

    # conn.close()

    return (cursor.fetchall())

# conn = sqlite3.connect('item.db') #makes the database
# cursor = conn.cursor()
# many_items = [
#     ('Turkey', '$10'),
#     ('Beef', '12'),
#     ('Chicken', '$10')]

# cursor.executemany("INSERT INTO items VALUES (?,?)", many_items)

# cursor.execute("SELECT * FROM items")

# print(cursor.fetchall())




if __name__ == "__main__":
    item_search("Ham")