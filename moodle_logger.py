from selenium import webdriver
import time
import threading
import sys

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

account_daten = []

with open("accountdaten.txt", 'r') as filehandle:
    for line in filehandle:
        account_daten.append((line.rstrip()))

nutzername = account_daten[0]
passwort = account_daten[1]

help_me = 0 #does not work if made into a boolean??

def logging():
    global  help_me

    try:
        driver.get("http://moodle.bildung-lsa.de/gym-oekumene/")

        username = driver.find_element_by_id("login_username")
        username.clear()
        username.send_keys(nutzername)

        password = driver.find_element_by_id("login_password")
        password.clear()
        password.send_keys(passwort)

        driver.find_element_by_xpath("//input[@value='Login']").click()
        courses = driver.find_elements_by_class_name("coursename")

        for x in range(len(courses)):
            courses[x].click()
            checkboxes = driver.find_elements_by_xpath("//*[contains(@src,'https://moodle.bildung-lsa.de/gym-oekumene/theme/image.php/classic/core/1603737858/i/completion-manual-n')]")
            if (len(checkboxes) != 0):
                for i in range(len(checkboxes)):
                    driver.execute_script("arguments[0].click();", checkboxes[i])

            pdf_files = driver.find_elements_by_xpath("//*[contains(@src,'https://moodle.bildung-lsa.de/gym-oekumene/theme/image.php/classic/core/1603737858/f/pdf-24')]")
            if (len(pdf_files) != 0):
                for i in range(len(pdf_files)):
                    driver.execute_script("arguments[0].click();", pdf_files[i])

                handles = driver.window_handles
                parent_handle = driver.current_window_handle
                for i in range(len(handles)):
                    if handles[i] != parent_handle:
                        driver.switch_to.window(handles[i])
                        driver.close()

                driver.switch_to.window((parent_handle))

            driver.execute_script("window.history.go(-1)")
            courses = driver.find_elements_by_class_name("coursename")

        driver.quit()
        help_me = 1
    except Exception as e:
        driver.quit()
        help_me = 1

t1 = threading.Thread(target=logging)
t1.daemon = True
t1.start()

def pocketwatch():
    global help_me
    time.sleep(300)
    help_me = 1

t2 = threading.Thread(target=pocketwatch)
t2.daemon = True
t2.start()

while True:
    if (t1.is_alive()==True and help_me==1) or (t1.is_alive()==False and help_me==1):
        driver.quit()
        sys.exit()

