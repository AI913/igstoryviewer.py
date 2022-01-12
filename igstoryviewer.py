from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import username, pw
from pandas import DataFrame
import pandas as pd
import sys
import os

target_user = sys.argv[1]

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not now')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[1]/div").click()
        
# for the next story:
    def get_viewers(self, number):
        if len(self.driver.find_elements_by_xpath("/html/body/div[1]/section/div[1]/div/section/div/div[3]/div[2]/button")) == 0:
            print("No one has seen your number " + str(number) + " story yet!")
            return
        else:
            self.driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div/section/div/div[3]/div[2]/button").click()

        scroll_box = self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/div/div")

        last_ht, ht = 0, 1
        names = []

        while last_ht != ht:
            last_ht = ht
            links = scroll_box.find_elements_by_tag_name('a')
            newname = [name.text for name in links if name.text != '']
            [names.append(name) for name in newname if name not in names]
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)

            if target_user in newname:
                print(target_user + " has seen your " + str(number) + " story!")
                self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div/div[2]/button").click()

        print(target_user + " hasn't seen your " + str(number) + " story yet!")
        self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div/div[2]/button").click()

        number += 1
        if len(self.driver.find_elements_by_xpath("/html/body/div[1]/section/div[1]/div/section/div/button[2]")) == 0:
            self.driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div/section/div/button").click()
            InstaBot.get_viewers(number)
        else:
            self.driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div/section/div/button[2]").click()

        return

        
    def Diff(li1, li2):
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
        return li_dif
    
        
my_bot = InstaBot(username, pw)
sleep(2)
my_bot.get_viewers(1)

# number = 1
# while len() > 0:
#     my_bot.get_viewers(number)
#     number += 1



#return list(set(following) - set(followers))
#people who have liked at least one of my past n posts
#total_likers = my_bot.total_likers(int(sys.argv[1]))
#print(total_likers)

# unfollowers = [user for user in following if user not in followers]
#unfollowers = [i for i in followers + following if i not in followers or i not in following]

#unlikers = [user for user in following if user not in total_likers]
# print("Here are the unfollowers:", unfollowers)
#print(unlikers)
#df = DataFrame(unlikers)
#export_excel = df.to_excel (r'/Users/chiuyiuwah/Data/unlikers.xlsx', index = None, header=True) #Don't forget to add '.xlsx' at the end of the path
#os.system("open -a '/Applications/Microsoft Excel.app' '/Users/chiuyiuwah/Data/unlikers.xlsx'")
