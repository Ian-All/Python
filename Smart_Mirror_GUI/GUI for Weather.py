import tkinter as tk
import time
import requests

#Fonts
#Mash look alike: Bernard MT Condensed


def get_weather():
	#collecting data from servers-----------------------------------------------------------------------
	conn1 = requests.get("https://api.thingspeak.com/channels/CHANNELID/feeds.json?results=1")
	dataset = conn1.json()
	conn2 = requests.get('http://api.openweathermap.org/data/2.5/weather?id=WEATHERID&units=imperial')
	dataset2 = conn2.json()
	#Thingspeak data -----------------------------------------------------------------------------------
	real_temp=(dataset['feeds'][0]['field1'])
	real_light=(dataset['feeds'][0]['field2'])
	real_pressure=float(dataset['feeds'][0]['field3'])
	real_humidity=(dataset['feeds'][0]['field4'])
	#---------------------------------------------------------------------------------------------------
	#Open Weather Data----------------------------------------------------------------------------------
	iot_temp=str((dataset2['main']['temp']))
	iot_humidity=str((dataset2['main']['humidity']))
	#Making a decent-looking output---------------------------------------------------------------------
	final_real=real_temp+'°'+'\n'+real_humidity+'%\n'+str(int(real_pressure))+' Pa\n'+real_light
	final_iot=iot_temp+'°\n'+iot_humidity+'%'
	#Accuracy calculations------------------------------------------------------------------------------
	temp1= float(real_temp)
	temp2= float(dataset2['main']['temp'])
	
	current_error = (abs(temp1-temp2)/temp1)*100
	current_error1=round(current_error, 2)
	current_error = str(100-current_error1)
	error=current_error
	tempvar = 'Current: ' +current_error + '%'
	current_error+='%'

	
	return final_real, final_iot,tempvar, error
	
def update_weather():
	weather_out['text']=get_weather()[0]
	accuracy['text']=get_weather()[2]
	time.sleep(2)
	report_accuracy()
	root.after(30000, update_weather)
	
	
def report_accuracy():
	api_key='APIKEY'
	x=float(get_weather()[3])
	payload = {'api_key': api_key, 'field1': x}
	requests.post('https://api.thingspeak.com/update', params=payload)
	time.sleep(3)
	
	
root = tk.Tk()


HEIGHT= 700
WIDTH= 800

root.wm_attributes('-fullscreen','true')
#HEIGHT= root.winfo_screenheight()
#WIDTH= root.winfo_screenwidth()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
	
frame=tk.Frame(root, bg="black")
frame.place(relwidth=1, relheight=1)


tempimage=tk.PhotoImage(file='DATAIMG.png')
imglabel=tk.Label(frame, image=tempimage,bg='black')
imglabel.place(x=1,y=30,width=70,height=200)

title1=tk.Label(frame, text='Live Data',fg="white", bg="black",font=("Times",20))
title1.place(x=30, y=3)

weather_out = tk.Label(frame,text=get_weather()[0], fg="white", bg="black",font=("Times",30))
weather_out.place(x=70, y=40)


tempimage2=tk.PhotoImage(file='DATAIMG2.png')
imglabel2=tk.Label(frame, image=tempimage2,bg='black')
imglabel2.place(relx=.9,rely=.05,relwidth=.1)

title2=tk.Label(frame, text='Weather Report',fg="white", bg="black",font=("Times",20))
title2.place(relx=.79,rely=0.01,relwidth=.2,)

weather_out2 = tk.Label(frame,text=get_weather()[1], fg="white", bg="black",font=("Times",30))
weather_out2.place(relx=.82, rely=.07, width=110)

title3=tk.Label(frame, text='Temperature Accuracy',fg="white", bg="black",font=("Times",15))
title3.place(relx=.75,rely=0.24,width=300,)

accuracy=tk.Label(frame, text=get_weather()[2],fg="white", bg="black",font=("Times",15))
accuracy.place(relx=.79,rely=0.28,relwidth=.2,)

#Data is hard set temporarily
title4=tk.Label(frame, text='Hourly: 88.56%',fg="white", bg="black",font=("Times",15))
title4.place(relx=.75,rely=0.32,width=300,)

#Data is hard set temporarily
title5=tk.Label(frame, text='Daily: 91.98%',fg="white", bg="black",font=("Times",15))
title5.place(relx=.75,rely=0.36,width=300,)

update_weather()

root.mainloop()

