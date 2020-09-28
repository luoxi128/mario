import re
import urllib.request
import os

with open("mario.txt", "r", encoding='UTF-8') as f:  # open file
    data = f.read()  # read file
    f.close()  # close file
it = re.finditer(r'http:\\/\\/.+?\.mp3', data)  #
string = []
n = 1
path = "./music"
if not os.path.exists(path):
    os.makedirs(path)

for match in it:
    string.append(match.group())
print(string)

for url in string:
    clr_format = re.sub(r'\\', "", url)
    print(clr_format)
    name = "music/" + str(n).zfill(3) + ".mp3"
    print(name)
    urllib.request.urlretrieve(clr_format, name)
    n += 1

