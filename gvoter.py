########### Feichangha0 - auto voter (firefox)
########### To use - create text file "auth.txt" in the same directory, enter usernames and passwords, each in a new line
########### ########### ###########
########### ########### ###########
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

########### DRIVER - edit path here
########### ########### ###########
########### ########### ###########
driver = webdriver.Firefox(executable_path=r"C:\<PATH_TO_DRIVER>\geckodriver.exe")


########### VOTE
########### ########### ###########
########### ########### ###########
def vote():
    driver.get("https://YOURWEBSITE.com/index.php?do=vote")
    html = driver.page_source
    phrase = "You can Vote!"
    x = 0
    x = html.count(phrase)
    print(x, "votes remaining")
    if x == 2:
        # vote1
        driver.find_element_by_xpath(
            r'/html/body/div/table/tbody/tr[4]/td[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/div/form/table/tbody/tr[2]/td[2]/input').click()
        try:
            driver.back()
        except:
            pass
        sleep(1)
        driver.get("https://YOURWEBSITE.com/index.php?do=vote")
        # vote2
        driver.find_element_by_xpath(
            r'/html/body/div/table/tbody/tr[4]/td[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/div/form/table/tbody/tr[2]/td[3]/input').click()
        try:
            driver.back()
        except:
            pass
        sleep(1)
        driver.get("https://YOURWEBSITE.com/index.php?do=vote")
    if x == 1:
        # vote2only
        driver.find_element_by_xpath(
            r'/html/body/div/table/tbody/tr[4]/td[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/div/form/table/tbody/tr[2]/td[3]/input').click()
        try:
            driver.back()
        except:
            pass
        sleep(1)
        driver.get("https://YOURWEBSITE.com/index.php?do=vote")
    driver.find_element_by_xpath(r'//*[@id="img1782"]').click()  # click logout button


########### LOGIN
########### ########### ###########
########### ########### ###########
def login(usr, psw):
    try:
        driver.get("https://YOURWEBSITE.com/")
    except:
        pass
    sleep(2)
    usr_in = driver.find_element_by_xpath(
        r'/html/body/div/table/tbody/tr[4]/td[1]/div/table[2]/tbody/tr/td[3]/div/form/table[2]/tbody/tr/td[2]/div/table/tbody/tr[4]/td[1]/input')
    usr_in.send_keys(usr)
    psw_in = driver.find_element_by_xpath(
        r'/html/body/div/table/tbody/tr[4]/td[1]/div/table[2]/tbody/tr/td[3]/div/form/table[2]/tbody/tr/td[2]/div/table/tbody/tr[6]/td/input')
    psw_in.send_keys(psw)
    login_btn = driver.find_element_by_xpath(r'//*[@id="img812"]')
    login_btn.click()
    vote()


#   driver.execute_script("window.history.go(-1)")

########### IMPORT CREDENTIALS - from "auth.txt"
########### ########### ###########
########### ########### ###########
def main(filename):
    file1 = open(filename)
    usr = file1.readline()
    psw = file1.readline()
    while usr != "" and psw != "":
        print(usr + psw)
        login(usr, psw)
        usr = file1.readline()
        psw = file1.readline()
        sleep(1)
    file1.close()


main("auth.txt")
try:
    driver.back()
except:
    pass
driver.close()
