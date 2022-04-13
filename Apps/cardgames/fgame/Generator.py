from PIL import Image, ImageDraw, ImageFont
import random

random.seed(a=None, version=2)
myFont = ImageFont.truetype("arialbd.ttf", 150)

red = ["ROJO", (225,10,5)]
green = ["VERDE", (5,85,5)]
blue = ["AZUL", (0,107,224)]
orange = ["NARANJA",(224,122,2)]
yellow = ["AMARILLO", (255,215,0)]
purple = ["MORADO", (110,0,110)]
black = ["NEGRO", (0,0,0)]
colors = [red,green,blue,orange, yellow, purple, black]
words = ["PICHA", "PUTA", "MIERDA", "PERRA", "HIJUEPUTA", "RUTA", "PERA", "DICHA" ]

counter = 0

ONECARD = True
#ONECARD = False

total_cards = 80
card_list = []
page = []


def Gnewcard():
	randomtext = 0
	isblack = 0

	TEXT = ""

	if counter < 5: # first five cards are "fuck cards"
		TEXT = "FUCK"
		isblack = counter % 2
	elif counter < total_cards - len(words)*4:# counter<48 #  colour cards
		textnum = random.randint(0,5)
		TEXT = colors[textnum][0]
		isblack = random.randint(0,1)
	elif counter < total_cards:  # word cards: there are 4 cards for each word
		textnum = (counter)%len(words)
		TEXT = words[textnum]
		isblack = counter % 2

	backgroundNum = random.randint(0,5)

	fontNum = 6 if isblack else random.randint(0,5)
	while(backgroundNum == fontNum):
		fontNum = 6 if isblack else random.randint(0,5)  

	newcard = ((TEXT) ,( backgroundNum) , (fontNum))

	return newcard



imgset = Image.new('RGB', (2550, 3300), color =(150,150,150) )

while (counter < total_cards):


	W, H = (1050,750)


	newcard = Gnewcard()
	((randommsg) ,( background) , (fontColor)) = newcard

	while True:
		if newcard in card_list:
			newcard = Gnewcard()
			((randommsg) ,( background) , (fontColor)) = newcard
		else:
			break
	card_list.append(newcard)

	img = Image.new('RGB', (W, H), color = colors[background][1])
	draw = ImageDraw.Draw(img)

	w, h = draw.textsize(randommsg, font=myFont)

	draw.text(((W-w)/2,(H-h)/2), randommsg, fill=colors[fontColor][1],font=myFont)

	out = img.rotate(90, expand=True)
	name = "card" + str(f"{counter:02d}") + ".png"
	#out.save(name)  # save each card

	page.append(out)
	imgset.paste(out,(((counter%9)//3)*800+50,(counter%3)*1080+50))

	if (counter%9 == 8):
		#saves the set when it's full
		imgset.save("set"+ str(counter//9) + ".png")
		page = []
		imgset = Image.new('RGB', (2550, 3300), color =(150,150,150) )


	counter += 1

	if(ONECARD): break

#saves the last set
imgset.save("set"+ str(counter//9)+ ".png")
