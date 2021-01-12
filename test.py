
import schedule
import time

def job():
    print("I'm working...")

schedule.every().day.at("18:51").do(job)
schedule.every().day.at("18:52").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)