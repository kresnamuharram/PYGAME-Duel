import pygame,sys
pygame.init()
pygame.font.init()
pygame.font.get_fonts()

#color
black = (255,255,255)
red = (255,0,0)
white = (0,0,0)

#screen
screen_width = 852
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("coba1")

#load
walkRight = [pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png'),]
walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png'),]
char = pygame.image.load('standing.png')
bg = pygame.image.load('bg.jpg')
ball = pygame.image.load('ball.png')

#sound
bulletsound = pygame.mixer.Sound("bullet.wav")
hitsound = pygame.mixer.Sound("hit.wav")
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)


class Player:

    def __init__(self,x,y,width,length):
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.jump_count = 10
        self.jump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.ball_jump = False
        self.speed = 5
        self.standing = False
        self.hitbox = [self.x+10, self.y+10, 45, 55]

    def screen(self,screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not self.standing :
            if self.left:
                screen.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                screen.blit(walkRight[game.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.left:
                screen.blit(walkLeft[0], (self.x, self.y))
            if self.right:
                screen.blit(walkRight[0], (self.x, self.y))
            if not self.left and not self.right:
                screen.blit(char,(self.x, self.y))
        self.hitbox = [self.x+10, self.y+10, 45, 55]

    def hit(self, screen):
        self.x = 60
        self.y = 410
        self.walkCount = 0
        pygame.font.get_fonts()
        font_score =pygame.font.SysFont('freesansbold.tff', 32)
        text_font = font_score.render("-5",1,(255,255,255))
        screen.blit(text_font,(screen_width/2-(text_font.get_width()/2),screen_height/2 -(text_font.get_height()/2)))
        pygame.display.update()
        i = 0
        while i<100:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
class Projectile:

    def __init__ (self, x, y, color, radius, facing):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.facing = facing
        self.vel = 8 * facing

    def makeCircle(self, screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y), self.radius)

class Enemy:
    walkRight = [pygame.image.load('R1E.png'),pygame.image.load('R2E.png'),pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'),pygame.image.load('R5E.png'),pygame.image.load('R6E.png'),
                 pygame.image.load('R7E.png'),pygame.image.load('R8E.png'),pygame.image.load('R9E.png'),
                 pygame.image.load('R10E.png'),pygame.image.load('R11E.png')]
    walkleft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                 pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                 pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                 pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self,x,y, length, width, start, stop, speed):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.start = start
        self.stop = stop
        self.move = [start,stop]
        self.speed = speed
        self.walkCount = 0
        self.position = 1
        self.interval_enemy = self.speed * self.position
        self.hitbox = [self.x+10, self.y+10, 45, 55]
        self.health = 0
        self.health_green = [self.x, self.y-20 , 20, 50]
        self.health_red = [self.x, self.y-20 , 20, 50]
        self.health_bar = 0
        self.visible = True

    def move_game(self):
        if self.interval_enemy > 0:
            if self.x <= self.move[1] - self.speed:
                self.x += self.interval_enemy
            else:
                self.interval_enemy = self.interval_enemy * -1
                self.walkCount = 0
        else:
            if self.x > self.move[0] + self.speed:
                self.x += self.interval_enemy
            else:
                self.interval_enemy = self.interval_enemy * -1
                self.walkCount = 0

    def draw(self,screen):
        self.health_green = [self.x, self.y-20 , 50, 20]
        self.health_red = [self.x, self.y-20 , 50 - self.health_bar, 20]
        pygame.draw.rect(screen,(255,0,0),self.health_green)
        pygame.draw.rect(screen,(0,255,0),self.health_red)
        if self.walkCount +1 >= 33:
            self.walkCount = 0
        if self.interval_enemy >= 1:
            screen.blit(Enemy.walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        if self.interval_enemy <= 1:
            screen.blit(Enemy.walkleft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = [self.x+10, self.y+10, 45, 55]
        
    def hit(self):
        print("adaw")
        
        
def redrawGameWindow():
    screen.blit(bg,(0,0))
    game.screen(screen)
    if goblin.visible:
        text = font_game.render("Score "+ str(score),1,(255,255,255))
        goblin.draw(screen)
        screen.blit(text,(0,0))
    for bullet in bullets:
        bullet.makeCircle(screen)
    pygame.display.update()

score = 0
font_game = pygame.font.Font(pygame.font.get_default_font(),32)
game = Player(200, 400, 64, 64)
goblin = Enemy(400,400,64,64,64,700,8)
loading_bullet = 0
bullets = []

pygame.init()
clock = pygame.time.Clock()

while True:
    if -1 * game.hitbox[3] < game.hitbox[1]-goblin.hitbox[1] <= game.hitbox[3] and -1 * game.hitbox[2] < game.hitbox[0]-goblin.hitbox[0] <= game.hitbox[2]:
        game.hit(screen)

    
    if loading_bullet < 3:
        loading_bullet += 1
    else:
        loading_bullet = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    goblin.move_game()

    for bullet in bullets:
        if goblin.visible:    
            if bullet.y-bullet.radius <= goblin.hitbox[1]+goblin.hitbox[3] and bullet.y >= goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    goblin.hit()
                    hitsound.play()
                    bullets.remove(bullet)
                    score += 1
                    goblin.health_bar = score * 5 * 0.5
                    if goblin.health_bar > 50:
                        goblin.visible = False

        if bullet.x < screen_width and bullet.x >0:
            bullet.x += bullet.vel
        else:
            bullets.remove(bullet)
    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and loading_bullet == 0:
        loading_bullet = 1
        bulletsound.play()
        if game.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 10:
            bullets.append(Projectile(round(game.x + game.width //2), round(game.y + game.length//2), (0,0,0), 6, facing))

    if keys[pygame.K_LEFT] and game.x > game.speed :
        game.x -= game.speed
        game.left = True
        game.right = False
        game.standing = False
    elif keys[pygame.K_RIGHT] and game.x < 852 - game.speed - game.width :
        game.x += game.speed
        game.right = True
        game.left = False
        game.standing = False
    else:
        game.standing = True
        game.walkCount = 0

    if not game.jump:
        if keys[pygame.K_UP]:
            game.jump = True
    if game.jump:
        if game.jump_count >= -10:
            neg = 1
            if game.jump_count < 0:
                neg = -1
            game.y -= (game.jump_count ** 2) * neg * 0.5
            game.jump_count -= 1
        else:
            game.jump = False
            game.jump_count = 10


    redrawGameWindow()

    pygame.display.flip()
    clock.tick(27)




