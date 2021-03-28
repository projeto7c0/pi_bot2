import os
import twitter

f = open("Pi - Dec.txt", "r")

t = f.read(251)
twitter.tweet("pi = " + t + "...")

text = f.read()

f = open("Pi - Dec.txt", "w")
f.write(text)
f.close()