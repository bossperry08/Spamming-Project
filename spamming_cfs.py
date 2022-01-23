#Comments for who wanting to use the source code

#Modules
from selenium import webdriver
from time import sleep

#Declare a variable named `browser`` representing your browser (Chrome, Firefox, Internet Explorer,...)
browser = webdriver.Chrome(executable_path="chromedriver.exe")

#Opening the confession site
browser.get("https://docs.google.com/forms/d/e/1FAIpQLScmwUDWJfrh8zOT6Z5ErxOjmWtkdZCCx2MpBOqCMOQX8dGV9Q/viewform")

#Spamming
#Iterate the progress 100 times 
for i in range(0, 100):
    print("The " + str(i + 1) + " time")
    #Spamming
    #Find the category you want
    browser.find_element_by_id("i23").click()    
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea").send_keys("hello")
    browser.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span").click()

    #Send another one
    if(i != 99):
        browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()
    print("The " + str(i + 1) + " time is successful!!")
        

#Close the browser
browser.close()