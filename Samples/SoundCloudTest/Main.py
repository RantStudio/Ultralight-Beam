from selenium import webdriver


def main():

    ##Intializes the web driver
    driver = webdriver.PhantomJS()

    ##Navigates to artist's page
    driver.get("https://soundcloud.com/")
    driver.find_element_by_xpath(
    '//*[@id="content"]/div/div/div[2]/div/div[1]/span/form/input').send_keys("carti")
    driver.find_element_by_xpath("""//*[@id="content"]/div/div/div[2]/div/div[1]/span/form/button""").click()
    print(driver.current_url)
    driver.find_element_by_xpath("""//*[@id="content"]/div/div/div[2]/div/div[1]/div/div/ul/li[4]/a""").click()
    driver.find_element_by_link_text("playboicarti").click()
    print(driver.current_url)
    driver.find_element_by_xpath('''//*[@id="content"]/div/div[3]/div/div[1]/ul/li[2]/a''')


    ##Returns artist name

    name = driver.find_element_by_class_name("soundTitle__usernameText")

    ##Returns all the information of the artist such as followers, followings and number of tracks
    info = driver.find_elements_by_class_name("infoStats__value")

    followers = info[0]
    following = info[1]
    tracks = info[2]


    ##printing shit
    print(name.text)
    print(followers.text)
    print(following.text)
    print(tracks.text)



    ##Returns a list of of the song name's on playboi carti's profile
    songNames = driver.find_elements_by_class_name("soundTitle__title")

    ##Returns a list of plays for each one of his songs
    plays = driver.find_elements_by_class_name("sc-ministats-plays")

    ##Returns a list of comments for each one of his songs
    comments = driver.find_elements_by_class_name("sc-ministats-comments")

main()
