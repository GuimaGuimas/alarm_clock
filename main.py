from tkinter import *
from datetime import datetime
import time
import winsound
from threading import *

root = Tk()
root.geometry("400x200")
root.configure(bg="black")
root.resizable(0,0)


def Threading():
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)

        current_time = datetime.now().strftime("%H:%M:%S")

        print(current_time, set_alarm_time)

        if set_alarm_time == current_time:
            print('Time to Wake Up!')
            winsound.PlaySound('sound.wav', winsound.SND_ASYNC)
            break


Label(root, text="Alarm Clock", font="Helvetica 20 bold", fg="blue", bg="black").pack(pady=10)
Label(root, text="Set Alarm", fg="white", font="Helvetica 15 bold", bg="black").pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
        '08', '09', '10', '11', '12', '13', '14', '15',
        '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])

hour_menu = OptionMenu(frame, hour, *hours)
hour_menu.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
        '08', '09', '10', '11', '12', '13', '14', '15',
        '16', '17', '18', '19', '20', '21', '22', '23',
        '24', '25', '26', '27', '28', '29', '30', '31',
        '32', '33', '34', '35', '36', '37', '38', '39',
        '40', '41', '42', '43', '44', '45', '46', '47',
        '48', '49', '50', '51', '52', '53', '54', '55',
        '56', '57', '58', '59', '60'
        )
minute.set(minutes[0])

minute_menu = OptionMenu(frame, minute, *minutes)
minute_menu.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
        '08', '09', '10', '11', '12', '13', '14', '15',
        '16', '17', '18', '19', '20', '21', '22', '23',
        '24', '25', '26', '27', '28', '29', '30', '31',
        '32', '33', '34', '35', '36', '37', '38', '39',
        '40', '41', '42', '43', '44', '45', '46', '47',
        '48', '49', '50', '51', '52', '53', '54', '55',
        '56', '57', '58', '59', '60'
        )
second.set(seconds[0])

second_menu = OptionMenu(frame, second, *seconds)
second_menu.pack(side=LEFT)

Button(root, text="Set alarm", font="Helvetica 15", command=Threading).pack(pady=20)

root.mainloop()