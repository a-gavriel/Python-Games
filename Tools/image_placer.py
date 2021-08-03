from PIL import Image, ImageDraw, ImageFont
import random

file_names = '''zchop.diamant_cards.x000.y000.jpg
zchop.diamant_cards.x000.y1520.jpg
zchop.diamant_cards.x000.y2280.jpg
zchop.diamant_cards.x000.y760.jpg
zchop.diamant_cards.x1512.y000.jpg
zchop.diamant_cards.x1512.y1520.jpg
zchop.diamant_cards.x1512.y2280.jpg
zchop.diamant_cards.x1512.y760.jpg
zchop.diamant_cards.x2268.y000.jpg
zchop.diamant_cards.x2268.y1520.jpg
zchop.diamant_cards.x2268.y2280.jpg
zchop.diamant_cards.x2268.y760.jpg
zchop.diamant_cards.x3024.y000.jpg
zchop.diamant_cards.x3024.y1520.jpg
zchop.diamant_cards.x3024.y2280.jpg
zchop.diamant_cards.x3024.y760.jpg
zchop.diamant_cards.x3780.y000.jpg
zchop.diamant_cards.x3780.y1520.jpg
zchop.diamant_cards.x3780.y760.jpg
zchop.diamant_cards.x4536.y000.jpg
zchop.diamant_cards.x4536.y1520.jpg
zchop.diamant_cards.x4536.y760.jpg
zchop.diamant_cards.x5292.y000.jpg
zchop.diamant_cards.x5292.y1520.jpg
zchop.diamant_cards.x5292.y760.jpg
zchop.diamant_cards.x6048.y000.jpg
zchop.diamant_cards.x6048.y1520.jpg
zchop.diamant_cards.x6048.y760.jpg
zchop.diamant_cards.x6804.y000.jpg
zchop.diamant_cards.x6804.y1520.jpg
zchop.diamant_cards.x6804.y4560.jpg
zchop.diamant_cards.x6804.y760.jpg
zchop.diamant_cards.x756.y000.jpg
zchop.diamant_cards.x756.y1520.jpg
zchop.diamant_cards.x756.y2280.jpg
zchop.diamant_cards.x756.y760.jpg
'''

files_list = file_names.splitlines()




def create_card(current_i):
  if current_i < len(files_list):
    newcard = Image.open(files_list[current_i]) 
  else:
    newcard = Image.new('RGB', (756, 760), color =(255,255,255) )
  return newcard


def create_game():
  cards_per_page = 12
  card_i = 0
  cards_padded = len(files_list) + ( cards_per_page - (len(files_list) % cards_per_page ))
  
  while (card_i < cards_padded):
    if (card_i % cards_per_page) == 0:
      full_img = Image.new('RGB', (2550, 3300), color =(150,150,150) )

    out_card = create_card(card_i)
    full_img.paste(out_card,(((card_i//4)%3)*800+50,(card_i%4)*800+50))

    if ((card_i % cards_per_page) == (cards_per_page - 1)):
      full_img.save("set"+ str(card_i// cards_per_page )+ ".png")

    card_i += 1

create_game()