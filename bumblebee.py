import pgzrun,random
WIDTH=500
HEIGHT=500
TITLE= "bee stuner"
bee=Actor("bee")
flower=Actor("flower")

gameover=False

score=0

def place_flower():
    #if flower.collidepoint(bee):
        flower.x=random.randint(70,WIDTH-100)
        flower.y=random.randint(70,HEIGHT-100)

def update():
    global score
    if keyboard.left:
        bee.x -= 2
        if bee.x <= 0:
            bee.x = 10
    if keyboard.right:
        bee.x += 2
        if bee.x >= WIDTH:
            bee.x = 10
    if keyboard.up:
        bee.y -= 2
        if bee.y <= 0:
            bee.y = 10
    if keyboard.down:
        bee.y += 2
        if bee.y >= HEIGHT:
            bee.y = 10

    if bee.colliderect(flower):
        score=score+1
        place_flower()

def change():
    global gameover
    gameover = True

def draw():
    screen.clear()
    #screen.blit("field",(0,0))
    screen.fill("blue")
    if gameover:
        screen.fill("pink")
        screen.draw.text("You died! \nreason \nYour final score: " + str(score), center=(WIDTH/2,250),color="red")
    else:
       bee.draw()
       flower.draw()
       screen.draw.text("Score: " + str(score), color="orange", topleft=(10,10))
clock.schedule(change,40.0)
pgzrun.go()