import sqlite3

DATABASE_FILE = "backpack.db"

'''Functions'''
def show_backpack(connection):
    '''nicely print the backpack information''' 
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM contents"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"\n{'Name:':<20}{'Description:':<60}")
        for item in results:
            print(f"{item[1]:<20}{item[2]:<60}")
    except:
        print("something went wrong with connection")

def add_item(connection, item_name, item_discription):
    '''add item to backpack database'''
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO contents(name,discription) VALUES (?,?)"
        cursor.execute(sql,(item_name,item_discription))
        connection.commit()
    except:
        print("counldn't add an item")

def delete_item(connection, item_name):
    '''delete and item by name from the datebase'''
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM contents WHERE name = ?"
        cursor.execute(sql,(item_name,))
        num_rows_affected = cursor.rowcount
        if num_rows_affected == 0:
            print("can't find item")
        else:
            connection.commit()
        connection.commit()
    except:
        print("item does exisit ")

def update_description(connection, item_name, new_description):
    try:
        cursor = connection.cursor()
        sql = "UPDATE contents SET description = ? WHERE name = ?"
        cursor.execute(sql,(new_description,item_name))
        num_rows_affected = cursor.rowcount
        if num_rows_affected == 0:
            print("can't update item")
        else:
            connection.commit()
    except:
        print("failed to update the item")


with sqlite3.connect(DATABASE_FILE) as connection:
   show_backpack(connection)
   #add item
   update_description(connection,"bullet","unidetifyed bullet type")
   show_backpack(connection)

