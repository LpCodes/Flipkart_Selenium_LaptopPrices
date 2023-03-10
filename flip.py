from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # req for sel4
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os

# path of the website
website = 'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_e6273f5c-19e4-41d4-ab88-d48dadf6e080_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics%7ELaptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y&sort=popularity'

# creating driver for sel4
driver_path = "./driver/chromedriver"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.set_page_load_timeout(10)
option  = Options() # for headless 
option.headless =True


try:
    # open site
    driver.get(website)

    # maximise browser
    driver.maximize_window()

except Exception as e:
    print('time out')
    driver.maximize_window()


products_lists = driver.find_elements(
    by='xpath', value="//div[@class='_2kHMtA']")
# print(products_lists)

names = []
prices = []
ratings = []

for item in products_lists:
    # important to add . in front of path to search in the item 
    item_name = item.find_element(
        by='xpath', value='.//div[@class="_4rR01T"]').text
    price = item.find_element(
        by='xpath', value=".//div[@class='_30jeq3 _1_WHN1']").text
    rating = item.find_element(
        by='xpath', value=".//div[@class='_3LWZlK']").text

    # print(item_name, price)
    names.append(item_name)
    prices.append(price)
    ratings.append(rating)


# driver.close()
driver.quit()


# print(len(names),len(ratings),len(prices))
mydict = {"laptop names":names,"laptop prices":prices,"Ratings":ratings}

data = pd.DataFrame(mydict)

outputpath = os.path.join("./output/","prices.csv")

data.to_csv(outputpath)

print("done")