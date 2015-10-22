import random, pygame, sys

class Deck(object):
	def __init__(self,symbol,color):
		self.symbol=symbol
		self.color=color
		self.hidden = True
		self.card = pygame.image.load("deck/b2fv.gif")
	def unhide(self):
		self.hidden=False
		self.card = pygame.image.load("deck/"+self.color.lower()+self.symbol.lower()+".gif")
	def hide(self):
		self.hidden = True
		self.card = pygame.image.load("deck/b2fv.gif")

talia=[]
for i in range (0,15):
	if i in range (0,10):
		talia.append(Deck(str(i+1),"S"))
	elif i==11:
		talia.append(Deck("J","S"))
	elif i==12:
		talia.append(Deck("Q","S"))
	elif i==13:
		talia.append(Deck("K","S"))
for i in range (0,15):
	if i in range (0,10):
		talia.append(Deck(str(i+1),"H"))
	elif i==11:
		talia.append(Deck("J","H"))
	elif i==12:
		talia.append(Deck("Q","H"))
	elif i==13:
		talia.append(Deck("K","H"))
for i in range (0,15):
	if i in range (0,10):
		talia.append(Deck(str(i+1),"C"))
	elif i==11:
		talia.append(Deck("J","C"))
	elif i==12:
		talia.append(Deck("Q","C"))
	elif i==13:
		talia.append(Deck("K","C"))
for i in range (0,15):
	if i in range (0,10):
		talia.append(Deck(str(i+1),"D"))
	elif i==11:
		talia.append(Deck("J","D"))
	elif i==12:
		talia.append(Deck("Q","D"))
	elif i==13:
		talia.append(Deck("K","D"))