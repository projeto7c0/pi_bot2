import os
import twitter

f = open("Pi - Dec.txt", "wr")

t = f.read(250)
twitter.tweet("..." + str(t) + "...")

f.write(f.read())
f.close()