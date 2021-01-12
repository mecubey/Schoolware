
import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import schedule
import time

root = tk.Tk()
root.geometry("700x500")
root.resizable(width=0, height=0)
root.title("moodle logger")
root.configure(background="black")

username_input = tk.StringVar(root)
username = tk.Entry(root, textvariable=username_input)
username.place(rely=0.5)
username.insert(0, "MOODLE_USERNAME")

password_input = tk.StringVar(root)
password = tk.Entry(root, textvariable=password_input)
password.place(rely=0.55)
password.insert(0, "MOODLE_PASSWORT")

interval_input = tk.StringVar(root)
interval  = tk.Entry(root, textvariable=interval_input)
interval.place(rely=0.6)
interval.insert(0, "INTERVAL EINFÜGEN")

display_text = tk.StringVar()
show_chrdriver = tk.Label(root, textvariable=display_text)
show_chrdriver.place(rely=0.95)


def uploadAction(event=None):
    filename = filedialog.askopenfilename()
    s = str(filename)
    display_text.set(s)


custom_time_entry_text = tk.StringVar()
custom_time_entry = tk.Entry(root, width=10, textvariable=custom_time_entry_text)
custom_time_entry.place(rely=0.1, relx=0.32)

times = tk.Listbox(root, width=35, height=12, bg="black", fg="white")
times.place(rely=0.05)

def moodle_logging():
    PATH = display_text.get().replace("\\", "/")
    USERNAME = username_input.get()
    PASSWORD = password_input.get()

    driver = webdriver.Firefox(executable_path=PATH)
    driver.set_page_load_timeout(5)
    driver.set_script_timeout(5)

    try:
        driver.get("https://moodle.bildung-lsa.de/gym-oekumene/")

        username = driver.find_element_by_id("login_username")
        username.clear()
        username.send_keys(USERNAME)

        password = driver.find_element_by_id("login_password")
        password.clear()
        password.send_keys(PASSWORD)

        driver.find_element_by_xpath("//input[@value='Login']").click()

        courses = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'coursename')))

        for x in range(len(courses)):
            courses[x].click()

            pdf_files = driver.find_elements_by_xpath(
                "//*[contains(@src,'https://moodle.bildung-lsa.de/gym-oekumene/theme/image.php/classic/core/1603737858/f/pdf-24')]")
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
            courses = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'coursename')))

        driver.quit()
        logs.insert(tk.END,
                    "Alle Kurse und PDF-Dateien erfolgreich besucht! ({})".format(datetime.now().strftime("%H:%M:%S")))
    except:
        logs.insert(tk.END, "ERROR ({})".format(datetime.now().strftime("%H:%M:%S")))
        driver.quit()

def add_time_to_list():
    schedule.every().day.at(str(custom_time_entry_text.get())).do(moodle_logging)
    times.insert(tk.END, custom_time_entry_text.get())

add_timebutton = tk.Button(root, text='ZEIT HINZUFÜGEN', command=add_time_to_list)
add_timebutton.place(rely=0.05, relx=0.32)


logs = tk.Listbox(root, width=50, height=25, bg="black", fg="white")
logs.place(relx=0.5, rely=0.1)

button = tk.Button(root, text='OPEN GECKODRIVER', command=uploadAction)
button.place(rely=0.65)

def spec_time_log():
    while True:
        schedule.run_pending()
        time.sleep(1)

start = tk.Button(root, text="START", width=10, command=spec_time_log)
start.place(relx=0.3, rely=0.853)

root.mainloop()