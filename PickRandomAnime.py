from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import json

def pick_anime(username):
    options = Options()
    options.binary_location = "/usr/bin/firefox"
    options.headless = True
    
    driver = webdriver.Firefox(options=options, executable_path="/home/janseuwu/Documents/geckodriver")
    driver.get(f"https://myanimelist.net/animelist/{username}")
    
    element = driver.find_element(By.TAG_NAME, "table")
    raw_table = element.get_attribute("data-items")
    
    table = json.loads(raw_table)
    
    unwatchedList = []
        
    for dictionary in table:
        for key in dictionary:
            if key == "status" and dictionary["status"] == 6:
                unwatchedList.append(dictionary["anime_title"])
    
    animetowatch = random.choice(unwatchedList)
    print("The anime you should watch is:\n" + animetowatch)

if __name__ == "__main__":
    pick_anime(input("Username: "))
