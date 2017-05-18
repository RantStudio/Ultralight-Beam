from selenium import webdriver
from main.Items.items import item
from main.Items.items import category

#run driver class that will be expanded once the main program finishes with gui

def rundriver():

    # Intializes the web driver
    driver = webdriver.PhantomJS()

    #goes to supreme new york
    driver.get("http://www.supremenewyork.com/shop/all")

    #putting in a test category name for now
    catName = ("pants")

    #using the getCategory function that is defined bewlo
    cat = getCategory(catName, driver)

    #get an array ot items on the page so we can do some lin alg memes to get the item + color
    items = driver.find_elements_by_class_name("name-link")

    #test name of the item
    itemName = ("Obama Pant")

    colorDesired = ("Red")

    #IMPORTANT TO KNOW. SUPREME ORGANIZES ALL OF ITS CLICKABLE LINKS BY THE CLASS NAME "name-link"
    #because of this we can simply check where we have the desired item and the position right after
    #it in the array should be the color. so if I in the array is equal to our desired itemName
    #and i+1 is our desired color. then we should click on that link.


    #will find the for loop for where the item first shows up
    for i in range(len(items)):
        if((items[i].text == itemName) and (items[i+1].text == colorDesired)):
            itemPos = i
            break





def getCategory(name, driver):
    driver.find_element_by_link_text(name)
    items = driver.find_elements_by_class_name("name-link")
    group = category(name, items.len())
    return group

