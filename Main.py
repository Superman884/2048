import pygame
from random import randrange
from time import sleep
import keyboard
pygame.init()
pygame.font.init()
def add(grid):
	options=[]
	for y in range(4):
		for x in range(4):
			if grid[y][x]==None:
				options.append((y,x))
	thing=options[randrange(len(options))]
	grid[thing[0]][thing[1]]=(randrange(2)+1)*2
	return grid
def move(grid, direction):
	ynummy=0
	xdata=(0,4,1)
	ydata=(0,4,1)
	if direction=='up':
		ydata=[0,4,1]
	elif direction=='down':
		ydata=[3,-1,-1]
	elif direction=='right':
		xdata=[3,-1,-1]
	else:
		xdata=[0,4,1]
	for y in range(ydata[0], ydata[1], ydata[2]):
		if direction=='up' or direction=='down':
			r=y
		for x in range(xdata[0], xdata[1], xdata[2]):
			if not( direction=='up' or direction=='down'):
				 r=x
			if grid[y][x]==None:
				if direction=='up' or direction=='down':
					r=y
				continue
			in_question=grid[y][x]
			if direction=='up' or direction=='down':
				change=ydata[-1]
			else:
				change=xdata[-1]
			fuse=False
			if direction=='up' or direction=='down':
				while limit(r, direction):
					if grid[r-change][x]==None:
						r-=change
					elif grid[r-change][x]==in_question:
						r-=change
						fuse=True
					else:
						break
			else:
				while limit(r, direction):
					if grid[y][r-change]==None:
						r-=change
					elif grid[y][r-change]==in_question:
						r-=change
						fuse=True
					else:
						break
			grid[y][x]=None
			if fuse==True:
				in_question*=2
			if direction=='up' or direction=='down':
				grid[r][x]=in_question
			else:
				grid[y][r]=in_question
			r=y
	return grid
def limit(r,direction):
	if direction=='down' or direction=='right':
		return r+1<=3
	else:
		return r-1>=0
win=pygame.display.set_mode((700,700))
grid=[[None for i in range(4)] for i in range(4)]
run=True
bg=pygame.image.load('bg.png')
side=149
gap=21
do=True
delay=0
key=None
myfont = pygame.font.SysFont('Robinson Typeface', 100)
win.blit(bg, (0,0))
pygame.display.update()
grid=add(grid)
grid=add(grid)
block=pygame.image.load('sake.png')
while run:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
	win.blit(bg, (0,0))
	ynum=0
	for y in range(gap, 701, side+gap):
		xnum=0
		for x in range(gap, 701, side+gap):
			if grid[ynum][xnum]!=None:
				textsurface = myfont.render(str(grid[ynum][xnum]), True, (136, 0, 21))
				win.blit(block, ((x,y)))
				win.blit(textsurface, (x+55, y+50))
			xnum+=1
		ynum+=1
	pygame.display.update()
	if delay!=0:
		delay-=1
	if keyboard.is_pressed('up') and delay==0:
		key='up'
		chang=[-1,0]
	elif keyboard.is_pressed('down') and delay==0:
		key='down'
		chang=[1,0]
	if keyboard.is_pressed('right') and delay==0:
		key='right'
		chang=[0,1]
	elif keyboard.is_pressed('left') and delay==0:
		key='left'
		chang=[0,-1]
	if key!=None:
		possible=False
		for y in range(4):
			for x in range(4):
				if grid[y][x]==None:
					continue
				if y+chang[0]<0 or x+chang[1]<0 or y+chang[0]>3 or x+chang[1]>3:
					continue
				if grid[y+chang[0]][x+chang[1]]==None or grid[y+chang[0]][x+chang[1]]==grid[y][x]:
					print(y+chang[0],x+chang[1])
					print(y,x)
					print('break')
					possible=True
					break
		if possible:
			grid=move(grid, key)
			do=False
			delay=10
			grid=add(grid)
			key=None