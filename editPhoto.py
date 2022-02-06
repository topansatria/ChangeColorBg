from cherrypy import url
import requests
import time
from env import APIKEY

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
        output = 'output/' + str(time.time()) + '.png'
        with open(output, 'wb') as out:
            out.write(ress.content)
            print('Check in :' + output)
    else:
        print('Error :', ress.text)

print('Remove BG @EFFCODE')

urlPhoto = input(('Asupkeun url photo:'))
color = input(('Asupkeun warna (blue, red, dll):'))

editPhoto(urlPhoto, color)