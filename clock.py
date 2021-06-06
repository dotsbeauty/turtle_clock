import turtle as t
import datetime as dt
import time as ti

now = dt.datetime.now()
secs= now.second
mins= now.minute
hrs= now.hour
dates= now.date()
print()
t.bgcolor('lightblue')
t.write(str(hrs)+":"+str(mins)+":"+str(secs)+"\n"+str(dates), align="center", font=('Arial',18,'bold'))
t.hideturtle()
input()