from selenium import webdriver
import time
from threading import *

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

account_daten = []

with open("accountdaten.txt", 'r') as filehandle:
    for line in filehandle:
        account_daten.append((line.rstrip()))

nutzername = account_daten[0]
passwort = account_daten[1]

class PropagatingThread(Thread):
    def run(self):
        self.exc = None
        try:
            if hasattr(self, '_Thread__target'):
                # Thread uses name mangling prior to Python 3.
                self.ret = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)
            else:
                self.ret = self._target(*self._args, **self._kwargs)
        except BaseException as e:
            self.exc = e

    def join(self):
        super(PropagatingThread, self).join()
        if self.exc:
            raise self.exc
        return self.ret

def logging():
    driver.get("http://moodle.bildung-lsa.de/gym-oekumene/")
    try:
        username = driver.find_element_by_id("login_username")
        username.clear()
        username.send_keys(nutzername)

        password = driver.find_element_by_id("login_password")
        password.clear()
        password.send_keys(passwort)

        driver.find_element_by_xpath("//input[@value='Login']").click()
        courses = driver.find_elements_by_class_name("coursename")

        for x in range(len(courses)-1):
            courses[x].click()
            driver.execute_script("window.history.go(-1)")
            courses = driver.find_elements_by_class_name("coursename")
        driver.quit()
        quit()
    except:
        driver.quit()
        quit()

logging_process = PropagatingThread(target=logging)

def timeout():
    logging_process.start()
    time.sleep(1)
    raise Exception

t = PropagatingThread(target=timeout)

try:
    t.start()
    t.join()
except:
    driver.quit()
    quit() #probably not needed

