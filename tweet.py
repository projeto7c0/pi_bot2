import os
import twitter

f = open("pi_bot2/pi-00", "r")

t = f.read(250)
twitter.tweet("..." + t + "...")

text = f.read()

f = open("pi_bot2/pi-00", "w")
f.write(text)
f.close()
