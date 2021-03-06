from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Main.items import category



def supremeDriver(categoryName, itemName, itemColor, fullName, email, telephone, addressLineOne, addressLineTwo, city, zip, creditCardCompany,creditCardNumber, expirationMonth, expirationYear, securitycode ):

    # Intializes the web driver
    driver = webdriver.Firefox()

    #goes to supreme new york
    driver.get("http://www.supremenewyork.com/shop/all")

    #putting in a test category name for now
    catName = (categoryName)

    #using the getCategory function that is defined bewlo
    cat = getCategory(catName, driver)

    element = WebDriverWait(driver , 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.name-link"))
    )
    #get an array ot items on the page so we can do some lin alg memes to get the item + color

    #test name of the item
    itemName = (itemName)

    colorDesired = (itemColor)


    items = driver.find_elements_by_css_selector("a.name-link")

    #IMPORTANT TO KNOW. SUPREME ORGANIZES ALL OF ITS CLICKABLE LINKS BY THE CLASS NAME "name-link"
    #because of this we can simply check where we have the desired item and the position right after
    #it in the array should be the color. so if I in the array is equal to our desired itemName
    #and i+1 is our desired color. then we should click on that link.


    #will find the for loop for where the item first shows up
    for i in range(len(items)):
        if((itemName in items[i].text) and (items[i+1].text == colorDesired)):
            items[i].click()
            break


    element2 =  WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "commit")))

    driver.find_element_by_name('commit').click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.button"))
    )

    #driver.find_element_by_link_text("checkout now").click()
    checkout = driver.find_elements_by_css_selector("a.button")

    print(len(checkout))
    print(checkout[0].text)
    print(checkout[1].text)
    print(checkout[2].text)


    #driver.get("https://www.supremenewyork.com/checkout")

    checkout[2].click()


    element4 =  WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "order_billing_name")))

    driver.find_element_by_id("order_billing_name").send_keys(fullName)
    driver.find_element_by_id("order_email").send_keys(email)
    driver.find_element_by_id("order_tel").send_keys(telephone)
    driver.find_element_by_id("bo").send_keys(addressLineOne)
    driver.find_element_by_id("oba3").send_keys(addressLineTwo)
    driver.find_element_by_id("order_billing_zip").send_keys(zip)
    driver.find_element_by_id("order_billing_city").send_keys(city)
    driver.find_element_by_xpath("//select[@name='order[billing_state]']/option[text()='NY']").click()
    #the following line is for credit card type select add later.
    driver.find_element_by_xpath("//select[@name='credit_card[type]']/option[text()='" + creditCardCompany + "']").click()
    driver.find_element_by_id("cnb").send_keys(creditCardNumber)
    #for the following the user will input the month the user's credit card expires
    driver.find_element_by_xpath("//select[@name='credit_card[month]']/option[text()='"+expirationMonth+"']").click()
    #for the following the user will input the year the user's credit card expires
    driver.find_element_by_xpath("//select[@name='credit_card[year]']/option[text()='"+expirationYear+"']").click()
    driver.find_element_by_id("vval").send_keys(securitycode)
    driver.find_element_by_id("order_terms").click()
    driver.find_element_by_name("commit").click()


def getCategory(name, driver):
    driver.find_element_by_link_text(name).click()
    items = driver.find_elements_by_class_name("name-link")
    group = category(name, len(items))
    return group

#supremeDriver()
