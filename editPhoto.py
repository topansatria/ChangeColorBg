import requests
import time
import os
from env import APIKEY

dir = '/storage/emulated/0/removeBg/'
# dir = 'output/'
if os.path.exists(dir) == False:
    os.mkdir(dir)

def editPhoto(img, bgColor):
    ress = requests.post('https://api.remove.bg/v1.0/removebg',
        # files = {
        #     'image_file': open(img, 'rb')
        # },
        data = {
            'image_url': img,
            'size': 'auto',
            'bg_color': bgColor
        },
        headers={'X-Api-Key': APIKEY},
    )

    if ress.status_code == requests.codes.ok:
        output = dir + str(time.time()) + '.png'
        with open(output, 'wb') as out:
            out.write(ress.content)
            print('Monngo, photona di cek didieunya : ' + output)
    else:
        print('Error :', ress.text)

print('==================')
print('Remove BG @EFFCODE')
print('==================')

while True:
    urlPhoto = input(('Url photo:'))
    if urlPhoto == "":
        print('Asupkeun hela url na cok :(')
        continue
    break

while True:
    color = input(('Warna (blue, red, dll):'))
    if color == "":
        print('Asupkeun hela warna na cok :(')
        continue
    break

editPhoto(urlPhoto, color)