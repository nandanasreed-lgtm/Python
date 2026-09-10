import pygame
import random
pygame.init()
SPRITE_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 2
blue = pygame.Color("blue")
lightblue = pygame.Color("lightblue")
darkblue = pygame.Color("darkblue")
yellow = pygame.Color("yellow")
magenta = pygame.Color("magenta")
orange = pygame.Color("orange")
white = pygame.Color("white")
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([1, -1]),random.choice([1, -1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundaryhit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = - self.velocity[0]
            boundaryhit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = - self.velocity[1]
            boundaryhit = True
        if boundaryhit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOUR_CHANGE_EVENT))
    def change_color(self):
        self.image.fill(random.choice([yellow, magenta, orange, white]))
def change_background_color():
    global bgcolor 
    bgcolor = random.choice([blue, lightblue, darkblue])
all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(white, 30, 20)
sp1.rect.x = random.randint(0, 470)
sp1.rect.y = random.randint(0, 380)
all_sprites_list.add(sp1)
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colourful Bounce")
bgcolor = blue
screen.fill(bgcolor)
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == SPRITE_COLOUR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOUR_CHANGE_EVENT:
            change_background_color()
    all_sprites_list.update()
    screen.fill(bgcolor)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.quit()