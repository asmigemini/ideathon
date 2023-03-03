from datetime import *
from flask import Flask
from flask import render_template
import webbrowser



app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')


def wakeup():
    a=input("Enter the time you usually wake up at (AM) (hr:min): ")
    wrong=False
    while not wrong:
        if ":" in a:
            b=a.split(":")
            break
        else:
            print("Invalid input. Please enter again.")
            b=wakeup()
            break
    return b

def sleep_time():
    a=input("Enter the time you usually sleep at (PM) (hr:min): ")
    wrong=False
    while not wrong:
        if ":" in a:
            b=a.split(":")
            break
        else:
            print("Invalid input. Please enter again.")
            b=sleep_time()
            break
    return b


try:
    f=open("database.txt","r")
    data=eval(f.read())
    start_time=data["wake_up"]
    end_time=data["sleep"]
    while datetime.now().hour!=end_time.hour:
        if (datetime.now().hour>start_time.hour and datetime.now().minute==00 and datetime.now().second==00):
            url = 'http://127.0.0.1:5000/'
            webbrowser.open(url)

            if __name__ == '__main__':
                app.run()

except:
    wake_up=".".join(wakeup())
    sleep=".".join(sleep_time())
    total_hours=12-(int(float(wake_up))+1)+int(float(sleep))-1
    water_goal_l=float(input("Enter the amount of water you plan to drink in a day(L): "))
    water_goal_ml=water_goal_l*1000
    every_hour=water_goal_ml/total_hours
    start_time=time(int(wake_up.split(".")[0])+1,int(wake_up.split(".")[1]))
    end_time=time(int(sleep.split(".")[0])+11,int(sleep.split(".")[1]))
    f=open("database.txt","w")
    l={"wake_up":start_time, "sleep":end_time, "every_hour":every_hour, "goal":water_goal_ml}
    f.write(f"{l}")
    f.close()

    while datetime.now().hour!=end_time.hour:
        if (datetime.now().hour>start_time.hour and datetime.now().minute==24 and datetime.now().second==00) or True:
            url = 'http://127.0.0.1:5000/'
            webbrowser.open(url)

            if __name__ == '__main__':
                app.run()

    
        






