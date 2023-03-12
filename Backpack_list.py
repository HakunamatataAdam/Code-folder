'''A simple program to store item in a back pack and add,remove and read
by adam '''


'''Functions'''
def show_backpack():
    '''nicely print the backpack information'''
    print(f"{'Index:':<8}{'Name:':<20}{'Description:':<60}")
    i = 0
    for item in backpack:
        print(f"{i:<8}{item[0]:<20}{item[1]:<60}")
        i += 1

def get_item():
    '''get an item and description from the user and add to backpack'''
    item = input("Name ")
    description = input("Discription ")
    backpack.append((item,description))

def add_item(item_name, item_description):
    '''add an item and description to the backpack'''
    backpack.append((item_name,item_description))

def delete_item(item_index):
    '''delet an item from backpack by index'''
    try:
        del backpack[int(item_index)]
    except:
        print("Item does not exist")

#this is the main backpack list
backpack = list()

#main loop
while True:
    #get user option
    user_input = input("\nwhat do you want to do\n1. print backpack content\n2. add item\n3. delete an item\n4. Exit\n:")
    #deal with printing
    if user_input == "1":
        show_backpack()
    #now the adding
    elif user_input == "2":
        get_item()
    #how the deleting
    elif user_input == "3":
        item = input("\nwhat item index do you want to delete\n")
        delete_item(item)
    #now exit
    elif user_input == "4":
        print("\n\nGoodbye!\n\n")
        break



#test out adding
# add_item("Fish","a tasty animal from the sea")
# add_item("Bomb","an dangerous exblosive")
# add_item("Stick","just a regular stick from a tree")
# add_item("Metal pipe","???")
# show_backpack()

# delete_item(7)

# show_backpack()
