import pygame
import random
pygame.init()

colors=[pygame.Color('blue'),pygame.Color('lightblue'),
        pygame.Color('darkblue'),pygame.Color('yellow'),
        pygame.Color('magenta'),pygame.Color('orange'),
        pygame.Color('white')]

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,size):
        super().__init__()
        self.image=pygame.Surface([size,size])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]), random.choice([-1,1])]

    def update(self):
        hit=False
        self.rect.move_ip(self.velocity)
        if self.rect.left<=0 or self.rect.right>=500:
            self.velocity[0] = -self.velocity[0]
            hit=True
        if self.rect.top<=0 or self.rect.bottom>=400:
            self.velocity[1] = -self.velocity[1]
            hit=True
        return hit

screen=pygame.display.set_mode([500,400])
pygame.display.set_caption("Two Squares with Color Change on Bounce")

def sprite_colors(group):
    return [s.image.get_at((0,0)) for s in group]

all_sprites=pygame.sprite.Group()
bg_color=random.choice(colors)
for i in range(2):
    sq_color=random.choice([c for c in colors if c!=bg_color])
    sprite=Sprite(sq_color,30)
    sprite.rect.x=random.randint(0,470)
    sprite.rect.y=random.randint(0,370)
    all_sprites.add(sprite)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill(bg_color)
    hit_any=False
    for s in all_sprites:
        if s.update():
            hit_any=True
    if hit_any:
        used=sprite_colors(all_sprites)
        for s in all_sprites:
            s.image.fill(random.choice([c for c in colors if c!=bg_color]))
        choices=[c for c in colors if c not in used]
        if choices:
            bg_color=random.choice(choices)
        else:
            bg_color=random.choice(colors)

    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
