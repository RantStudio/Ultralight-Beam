from tkinter import *
import Main.supremeDriver as supremeDriver

def get_data(event):
    supremeDriver.supremeDriver(categoryName.get(), itemName.get(), itemColor.get(), fullName.get(), email.get(), telephone.get(), addressLineOne.get(), addressLineTwo.get(), city.get(), zip.get(), creditCardCompany.get(), creditCardNumber.get(), expirationMonth.get(), expirationYear.get(), securitycode.get())



root = Tk()


#Values For the GUI
categoryName = StringVar()
itemName = StringVar()
itemColor = StringVar()
fullName = StringVar()
email = StringVar()
telephone = StringVar()
addressLineOne = StringVar()
addressLineTwo = StringVar()
city = StringVar()
zip = StringVar()
creditCardCompany = StringVar()
creditCardNumber = StringVar()
expirationMonth = StringVar()
expirationYear = StringVar()
securitycode = StringVar()



# Assign the variable to either textvariable or variable
# Also create the labels
categoryName = Entry(root, textvariable=categoryName)
categoryName.grid(row = 0, sticky =W, padx = 4)
Label(root, text="Name of Category").grid(row = 0, column = 1, sticky = W)

itemName = Entry(root, textvariable=itemName)
itemName.grid(row = 1, sticky =W ,padx = 4)
Label(root, text="Name of Item").grid(row = 1, column = 1, sticky = W)


itemColor = Entry(root, textvariable=itemColor)
itemColor.grid(row = 2, sticky =W,padx = 4)
Label(root, text="Color of Item").grid(row = 2, column = 1, sticky = W)

fullName = Entry(root, textvariable=fullName)
fullName.grid(row = 3, sticky =W,padx = 4)
Label(root, text="Full Name").grid(row = 3, column = 1, sticky = W)

email = Entry(root, textvariable=email)
email.grid(row = 4, sticky =W,padx = 4)
Label(root, text="Email").grid(row = 4, column = 1, sticky = W)


telephone = Entry(root, textvariable=telephone)
telephone.grid(row = 5, sticky =W,padx = 4)
Label(root, text="Telephone Number").grid(row = 5, column = 1, sticky = W)

addressLineOne = Entry(root, textvariable=addressLineOne)
addressLineOne.grid(row = 6, sticky =W,padx = 4)
Label(root, text="Address Line One").grid(row = 6, column = 1, sticky = W)

addressLineTwo = Entry(root, textvariable=addressLineTwo)
addressLineTwo.grid(row = 7, sticky =W,padx = 4)
Label(root, text="Address Line Two").grid(row = 7, column = 1, sticky = W)


city = Entry(root, textvariable=city)
city.grid(row = 8, sticky =W,padx = 4)
Label(root, text="City Name").grid(row = 8, column = 1, sticky = W)

zip = Entry(root, textvariable=zip)
zip.grid(row =9, sticky =W,padx = 4)
Label(root, text="Zip Code").grid(row = 9, column = 1, sticky = W)

creditCardCompany = Entry(root, textvariable=creditCardCompany)
creditCardCompany.grid(row =10, sticky =W,padx = 4)
Label(root, text="Credit Card Company Name").grid(row = 10, column = 1, sticky = W)

creditCardNumber = Entry(root, textvariable=creditCardNumber)
creditCardNumber.grid(row = 11, sticky =W,padx = 4)
Label(root, text="Credit Card Number").grid(row = 11, column = 1, sticky = W)

expirationMonth = Entry(root, textvariable=expirationMonth)
expirationMonth.grid(row = 12, sticky =W,padx = 4)
Label(root, text="Credit Card Expiration Month (00 Form)").grid(row = 12, column = 1, sticky = W)

expirationYear = Entry(root, textvariable=expirationYear)
expirationYear.grid(row =13, sticky =W,padx = 4)
Label(root, text="Credit Card Expiration Year (0000 Form)").grid(row = 13, column = 1, sticky = W)

securitycode = Entry(root, textvariable=securitycode)
securitycode.grid(row =14, sticky =W,padx = 4)
Label(root, text="Credit Card 3 Digit Secuirty Code").grid(row = 14, column = 1, sticky = W)


# Call the function get_data on click
getDataButton = Button(root, text="Run Bot")
getDataButton.bind("<Button-1>", get_data)
getDataButton.grid(row = 15, sticky =W)


root.geometry("500x400+200+200")

root.mainloop()
