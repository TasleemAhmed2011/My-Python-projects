import random
import pygame
screen_width, screen_height = 500,400
mov_speed=5
font_fize=25

pygame.init()

bg_image=pygame.transform.scale(pygame.image.load("collisons bg image.jpg"),(screen_width,screen_height))

font=pygame.font.SysFont("Times New Roman",font_fize)

class sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()

    def move(self,x_change,y_change):
        self.rect.x=max(min(self.rect.x + x_change,screen_width-self.rect.width),0) 
        self.rect.y=max(min(self.rect.y + y_change,screen_height-self.rect.height),0)
    
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Detecting Collisions")
all_sprites=pygame.sprite.Group()

sprite1= sprite(pygame.Color('black'),20,30)
sprite1.rect.x, sprite1.rect.y =random.randint(0,screen_width-sprite1.rect.width), random.randint(0,screen_height-sprite1.rect.height)
all_sprites.add(sprite1)

sprite2= sprite(pygame.Color('red'),20,30)
sprite2.rect.x, sprite2.rect.y =random.randint(0,screen_width-sprite2.rect.width), random.randint(0,screen_height-sprite2.rect.height)
all_sprites.add(sprite2)

running, won= True, False
clock= pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_x):
            running=False

        
        if event.type==pygame.KEYDOWN and event.key==pygame.K_r and won:
            # Reset win state
            won = False
            all_sprites.empty()   # remove old sprites

            # Respawn player
            sprite1 = sprite(pygame.Color('black'),20,30)
            sprite1.rect.x = random.randint(0, screen_width - sprite1.rect.width)
            sprite1.rect.y = random.randint(0, screen_height - sprite1.rect.height)
            all_sprites.add(sprite1)

            # Respawn target
            sprite2 = sprite(pygame.Color('red'),20,30)
            sprite2.rect.x = random.randint(0, screen_width - sprite2.rect.width)
            sprite2.rect.y = random.randint(0, screen_height - sprite2.rect.height)
            all_sprites.add(sprite2)

    if not won:
       keys=pygame.key.get_pressed()
       x_change = ((keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])) * mov_speed
       y_change = ((keys[pygame.K_DOWN]  or keys[pygame.K_s]) - (keys[pygame.K_UP]   or keys[pygame.K_w])) * mov_speed

       sprite1.move(x_change,y_change)

       if sprite1.rect.colliderect(sprite2.rect):
           all_sprites.remove(sprite2)
           won=True

    screen.blit(bg_image,(0,0))
    all_sprites.draw(screen)

    if won:
        win_text=font.render("You Win! If you want to replay so press R",True,pygame.Color('black'))
        screen.blit(win_text,(screen_width//2-win_text.get_width()//2,screen_height//2-win_text.get_height()//2))
    
    pygame.display.flip()
    clock.tick(90)

pygame.quit()
print()