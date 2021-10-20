#!/usr/bin/python37all

import RPi.GPIO as GPIO
import cgi
import cgitb 
cgitb.enable()   

Pin1 = 17
Pin2 = 22
Pin3 = 27

GPIO.setmode(GPIO.BCM) # choose pin numbering convention (alt = BOARD)
GPIO.setwarnings(False) # ignore warnings due to multiple scripts at same time
GPIO.setup(Pin1, GPIO.OUT)
GPIO.setup(Pin2, GPIO.OUT)
GPIO.setup(Pin3, GPIO.OUT)

data = cgi.FieldStorage()
s = data.getvalue('slider')

if data.getvalue('button') == Pin1:
 with open('value.txt', w) as f:
  f.write(str(17))
 with open('led-pwm.txt', 'w') as f:
  f.write(str(s))  

if data.getvalue('button') == Pin2:
 with open('value.txt', w) as f:
  f.write(str(22))
 with open('led-pwm.txt', 'w') as f:
  f.write(str(s))    

if data.getvalue('button') == Pin3:
 with open('value.txt', w) as f:
  f.write(str(27))
 with open('led-pwm.txt', 'w') as f: 
  f.write(str(s))   

print("Content-type: text/html\n\n")<head>
<title>Lab 4<title/>
<head/>
<body>
<div style="width:600px;background:#AAAAFF;border:1px;text-align:center">
<br>

<form action="/cgi-bin/Buttons.py" method="POST">
  <input type="submit" name="button" value="17">
  <input type="submit" name="button" value="22">
  <input type="submit" name="button" value="27">
  <input type="range" name="slider" min ="0" max="100" value ="50"/>
  <br>
  <input type="submit" value= "Change LED brightness">

</form>
<div/>
<body/>
</html>

