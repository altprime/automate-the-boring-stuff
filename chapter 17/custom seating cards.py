'''
custom seating cards

create custom invitations from guest list

'''

import os
from PIL import Image, ImageDraw

# loads flower image and changes its size.
flowerImage = Image.open('flower.jpg')
width, height = flowerImage.size
smallFlowerIm = flowerImage.resize((int(width/5), int(height/5)))


# creates list of guests.
guestsFile = open('guests.txt')
text = guestsFile.read()
guestsList = text.split('\n')

for guest in guestsList:
    # creates image.
    image = Image.new('RGBA', (288, 360), 'yellow')

    # adds guest's name.
    draw = ImageDraw.Draw(image)
    draw.text((110, 60), guest, fill='blue')
    image.save(guest + '.jpg')
    
    # adds flower.
    image = Image.open(guest + '.jpg')
    image.paste(smallFlowerIm, (120, 100))

    # adds rectangles.
    blackImage = Image.new('RGBA', (292, 364), 'black')
    blackImage.paste(image, (2, 2))

    blackImage.save(guest + '.jpg')
    
