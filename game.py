import sys, pygame, time, cards, random
from pygame.locals import *
pygame.init()

size = width, height = 1024, 768
height = 768

pygame.font.init()
myfont = pygame.font.SysFont("monospace", 15)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Clock Solitaire 0.1 beta")
halved = pygame.image.load("deck/b2pr.gif")
halved_rect = halved.get_rect()
black = 0, 0 , 0
game_over = pygame.image.load("deck/game_o.png")


def draw_cards(wid,hei,hour,zasieg):
	screen.blit(clock[hour][0].card, (wid,hei))
	wid=wid-12
	for i in range (1,len(clock[hour])):
		screen.blit(clock[hour][i].card.subsurface(halved_rect), (wid,hei))
		wid=wid-12


def draw_board():
	for i2 in range(13):
		draw_cards(hour_position[i2][0],hour_position[i2][1],i2,3)

def shuffle_cards():
	random.shuffle(cards.talia)
	global clock
	clock=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
	i=0
	for i2 in range (13):
		for i3 in range(4):
			clock[i2].append(cards.talia[i])
			clock[i2][i3].hide()
			i=i+1
	clock[12][0].unhide()
	global filled_hour
	filled_hour=[False,False,False,False,False,False,False,False,False,False,False,False,False,False]

def check_if_full(ite):
	if ite is not 12:
		if len(clock[ite])==4:
			for item in  clock[ite]:
				if item.hidden==True:
						break
				else:
					filled_hour[ite]=True
	else:
		for item in  clock[ite]:
			if item.hidden==True:
				break
			if item.symbol != "K":
				break
		else:
			filled_hour[ite]=True
def win():
	screen.fill((0,0,0))
	win_picture = pygame.image.load("deck/win.jpeg")
	screen.blit(win_picture, (20,20))
	wynik = myfont.render("You won! Congratulations! Press R to restart or ESC to exit. Your final score: "+str(score),1,(255,255,0))
	screen.blit(wynik,(100,100))
	wynik = myfont.render("Your final score: "+str(score),1,(255,255,0))
	screen.blit(wynik,(width-200,height-100))
	pygame.display.flip()
	win_condition = False
	key = pygame.key.get_pressed()
	if key[K_ESCAPE]:
		sys.exit()
	if key[K_r]:
		score=0
		main_loop()



hour_position = [
(width/2-50,70),
(width/2+70,160),
(width/2+190,250),
(width/2+310,340),
(width/2+190,430),
(width/2+70,520),
(width/2-50,610),
(width/2-170,520),
(width/2-290,430),
(width/2-410,340),
(width/2-290,250),
(width/2-170,160),
(width/2-50,340)]


hours_list=dict([('Q',0),('1',1),('2',2),('3',3),('4',4),('5',5),('6',6),('7',7),('8',8),('9',9),('10',10),('J',11),('K',12)])


games_played = -1
games_won = 0

def main_loop():
	lost = False
	score = 0
	MousePressed=False
	MouseDown=False
	MouseReleased=False
	Target=None
	shuffle_cards()
	global games_played
	games_played=games_played+1
	cought = False
	global win_condition
	win_condition = False
	while 1:
		screen.fill((0,0,0))
		pos=pygame.mouse.get_pos()
		key = pygame.key.get_pressed()
		if lost == False:
			draw_board()
			wynik = myfont.render("Your score: "+str(score),1,(255,255,0))
			screen.blit(wynik,(100,100))
			wynik = myfont.render("Games played: "+str(games_played),1,(255,255,0))
			screen.blit(wynik,(100,height-100))
			reset = myfont.render("Click here to restart",1,(255,255,0))
			screen.blit(reset,(width-250,height-100))
			reset_button = reset.get_rect()
			wynik = myfont.render("Games won: "+str(games_won),1,(255,255,0))
			screen.blit(wynik,(width-205,100))
			wynik = myfont.render("By Konrad Dryja",1,(255,255,0))
			screen.blit(wynik,(100,height-40))
			wynik = myfont.render("Copyright (c) 2014 KD",1,(255,255,0))
			screen.blit(wynik,(100,height-20))
			wynik = myfont.render("Hold T to view rules",1,(255,255,0))
			screen.blit(wynik,(width/2-100,height-20))
		else:
			screen.blit(game_over, (20,20))
			wynik = myfont.render("You lost, press R to restart or ESC to exit. Your final score: "+str(score),1,(255,255,0))
			screen.blit(wynik,(100,100))
			pygame.display.flip()
			key = pygame.key.get_pressed()
			if key[K_ESCAPE]:
				pygame.quit()
				sys.exit()
			if key[K_r]:
				score=0
				main_loop()
		if False not in filled_hour:
			win()
		for Event in pygame.event.get():
			if Event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()
			if Event.type == pygame.MOUSEBUTTONDOWN:
				MousePressed=True 
				MouseDown=True 
			if Event.type == pygame.MOUSEBUTTONUP:
				MouseReleased=True
				MouseDown=False
		
		if MousePressed==True:
			for ite in range(13):
				if (pos[0]>=(hour_position[ite][0]) and 
				pos[0]<=(hour_position[ite][0]+71) and 
				pos[1]>=(hour_position[ite][1]) and 
				pos[1]<=(hour_position[ite][1]+96) and
				clock[ite][0].hidden==False and
				filled_hour[ite] == False):
					Target=clock[ite][0]
					clock[ite].remove(Target)
					temp_pos=ite
					cought = True
					check_if_full(ite)
					break
			else:
				cought = False
			if (pos[0]>=(width-250) and 
				pos[0]<=(width-70) and 
				pos[1]>=(height-100) and 
				pos[1]<=(height-80)):
				score=0
				main_loop()
		if MouseDown and Target is not None and cought is True:
			screen.blit(Target.card,(pos[0]-20,pos[1]-20))
		if MouseReleased and cought is True:
			for ite in range(13):
				if (pos[0]>=(hour_position[ite][0]) and 
					pos[0]<=(hour_position[ite][0]+71) and 
					pos[1]>=(hour_position[ite][1]) and 
					pos[1]<=(hour_position[ite][1]+96) and
					hours_list[Target.symbol]==ite):
					score=score+1
					clock[ite].append(Target)
					clock[ite][0].unhide()
					temp_pos = None
					Target=None

					check_if_full(ite)
					if (filled_hour[ite] == True) and (ite != 12):
						i=ite
						while clock[i][0].hidden is False:
							if i>=11: i=i-12
							clock[i+1][0].unhide()
							i=i+1
					elif (filled_hour[ite] == True) and (ite == 12):
						lost = True
					break

			else:
				if temp_pos is not None:
					clock[temp_pos].insert(0,Target)
					filled_hour[temp_pos]=False
					Target=None
					temp_pos=None

		if key[K_ESCAPE]:
			pygame.quit()
			sys.exit()
		if key[K_t]:
			screen.fill((0,0,0))
			tut=pygame.image.load("deck/rules.png")
			screen.blit(tut,(200,200))
			pygame.display.flip()
			for Event in pygame.event.get():
				if Event.type==pygame.KEYDOWN:
					continue
		MousePressed=False
		MouseReleased=False
		pygame.display.flip()

main_loop()