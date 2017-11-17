from twilio.rest import Client
import json
import pprint

Shoplist = {} #sets the initial empty dictionary
list = True #toggles the run loop to add additional items before sending

print("Welcome to ShopLister")

while list == True:
    food, quantity = input("Enter the food followed by a space and the quantity, or type 'q q' to quit").split(); quantity
    Listadd = {food: quantity} #adds the food and quantity of the food into a holding dictionary, Listadd
    Shoplist.update(Listadd) #updates Shoplist dictionary
    for k, v in Shoplist.items(): #Concatenates dictionary into strings for ease of reading
        print(str(k) + ', ' + str(v)) #Shows user an updated shopping list

    if quantity == 'q': #Indicates the user is finished updating their list
        del Shoplist['q']
        Shoplist = str(Shoplist).replace("{","").replace("}","").replace("\'","")
        print(Shoplist)
        Shoplist = pprint.pformat(Shoplist)
        print(Shoplist)
        json_dump = json.dumps(Shoplist)
        print("json_dump", json_dump) #debug code
        print("We'll now save and text the shopping list. Thanks for using ShopLister!")
        newfile = open("list.txt", "w+") #the next 3 lines save the list as a txt file for future manipulation
        str1 = str(Shoplist)
        newfile.write(str1)
        list = False #breaks the loop and closes the program
    else:
        continue #continues the loop so user can enter more than one item

client = Client("Xxxxxx, "xxxxxx") #Texts the list to designated number


client.messages.create(to="+XXXXXXX", #phone numbers blanked for privacy
                       from_="+XXXXXXX,
                       body= json_dump)
