# Facebook messenger spam messages Script ,A Facebook Bot --->
# Developer Waqar Ali Abbas --->
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
print("---> Facebook messenger spam messages Script a Facebook-Bot")
print("---> Developer:  Waqar Ali Abbas")
User_email=input("Enter Your Facebook Email:  ")
User_password=input("Enter Your Facebook Password:  ")
Enter_Xpath=input('Enter Targeted User XPATH:  ')
Enter_FileName=input('Enter File name with .txt Extension:  ')
url="https://mbasic.facebook.com/"
driver=webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get(url)
email=driver.find_element_by_xpath("//input[@name='email']").send_keys(User_email)
password=driver.find_element_by_xpath("//input[@name='pass']").send_keys(User_password)
submit=driver.find_element_by_xpath("//input[@type='submit']").click()
# time.sleep(1)
Not_now=driver.find_element_by_xpath("//a[@class='bk bl bm bn bp']").click()
msg=driver.find_element_by_xpath("//nav[@class='be']/a[3]").click()
driver.find_element_by_xpath(Enter_Xpath).click()
def Loader_By_Waqar():
    #Put Your File Name Here
    with open(Enter_FileName,"r",encoding="UTF-8") as f:
        while True:
            x=f.readline()
            if x!="\n":
                driver.find_element_by_xpath("//textarea[@id='composerInput']").send_keys(x)
                driver.find_element_by_xpath("//input[@name='send']").send_keys(Keys.RETURN)
                driver.find_element_by_tag_name("body").send_keys(Keys.END)
                time.sleep(4)
                if f.readline()=="":
                    Loader_By_Waqar()
Loader_By_Waqar()
# Automation Script By Waqar , Facebook Bot ---