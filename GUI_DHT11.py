from tkinter import *
import Adafruit_DHT
import time
import threading

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 2

GUI = Tk()
GUI.title('Temperature Monitoring')
GUI.geometry('500x400+50+50') #+x+y อยู่ตรงไหนของหน้าจอ

GUI.attributes('-fullscreen',True) #full screen
GUI.bind('<F1>',lambda x: GUI.attributes('-fullscreen',False)) #กด F1 เพื่อออกจาก full screen
GUI.bind('<F2>',lambda x: GUI.attributes('-fullscreen',True)) #กด F2 เพื่อเข้าโหมด full screen

FONT1 = (None,40)
FONT2 = (None,40,'bold')

L = Label(GUI,text='Temperature',font=FONT1)
L.pack(pady=40) #pack จะวางไว้ที่บนสุด ตรงกลาง
#L.place(x=50, y=100) place จะวางไว้ตามพิกัด x,y

v_temperature = StringVar()
v_temperature.set('XX.YY °C')
L = Label(GUI, textvariable=v_temperature, font=FONT2, fg='blue')
L.pack(pady=40)

def UpdateTemp():
    global temperature
    h, t = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    temperature = t
    v_temperature.set('{:.1f} °C'.format(temperature))
    #print('updated')

def RunUpdateTemp():
    while True:
        try:
            UpdateTemp()
        except:
            v_temperature.set('ERROR')
        time.sleep(10)

B = Button(GUI,text='Update',command=UpdateTemp) #เมื่อกดปุ่มจะไปทำที่ฟังก์ชัน UpdateTemp
B.pack()

task = threading.Thread(target=RunUpdateTemp)
task.start()

GUI.mainloop()
