import os
import twitter

f = open("pi_bot2/pi.txt", "r")

t = f.read(251)
twitter.tweet("pi = " + t + "...")

text = f.read()

f = open("pi_bot2/pi.txt", "w")
f.write(text)
f.close()