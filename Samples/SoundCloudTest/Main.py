from selenium import webdriver

from Samples.SoundCloudTest.Artist import Artist
from Samples.SoundCloudTest.Songs import Song

def main():

    #ntializes the web driver
    driver = webdriver.PhantomJS()

    ##Navigates to artist's page
    ##Commented out because tests took too long, but i assure that it does work

    ##driver.get("https://soundcloud.com/")
    ##driver.find_element_by_xpath(
    ##'//*[@id="content"]/div/div/div[2]/div/div[1]/span/form/input').send_keys("carti")
    ##driver.find_element_by_xpath("""//*[@id="content"]/div/div/div[2]/div/div[1]/span/form/button""").click()
    #print(driver.current_url)
    #driver.find_element_by_xpath("""//*[@id="content"]/div/div/div[2]/div/div[1]/div/div/ul/li[4]/a""").click()
    #driver.find_element_by_link_text("playboicarti").click()
    #print(driver.current_url)
    #driver.find_element_by_xpath('''//*[@id="content"]/div/div[3]/div/div[1]/ul/li[2]/a''')

    #Skipping straight to the profile of the artist

    driver.get("https://soundcloud.com/678carti/tracks")

    ##Returns artist name
    name = driver.find_element_by_class_name("soundTitle__usernameText")

    ##Returns all the information of the artist such as followers, followings and number of tracks
    info = driver.find_elements_by_class_name("infoStats__value")

    followers = info[0]
    following = info[1]
    tracks = info[2]


    ##Intializes the artist with the 3 data fields
    carti = Artist(name.text, tracks.text, followers.text)

    ##Prints the info that was allocated within this object "carti"
    print(carti.name)
    print(carti.tracks)
    print(carti.followers)


    ##Returns a list of of the song name's on playboi carti's profile
    songNames = driver.find_elements_by_class_name("soundTitle__title")


    ##Returns a list of plays for each one of his songs
    plays = driver.find_elements_by_class_name("sc-ministats-plays")

    ##Returns a list of comments for each one of his songs
    comments = driver.find_elements_by_class_name("sc-ministats-comments")

    ##Adds object song in list songs for object carti
    for i in range(len(songNames)):
        carti.songs.append(Song(songNames[i].text,plays[i].text,comments[i].text))

    ##Print!f
    for i in range(len(carti.songs)):
        print(carti.songs[i].name)
main()
