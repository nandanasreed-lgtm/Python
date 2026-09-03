import pygame
pygame.init()
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("adding images")
bg_image = pygame.transform.scale(pygame.image.load("bg.jpg").convert(),(screen_width, screen_height))
strawberry = pygame.transform.scale(pygame.image.load("strawberry.jpg").convert_alpha(),(200, 200))
strawberry_rect = strawberry.get_rect(center = (screen_width // 2, screen_height // 2 - 30))
text = pygame.font.Font(None, 36).render("Hello world", True, pygame.Color("black"))
text_rect = text.get_rect(center = (screen_width // 2, screen_height // 2 + 110))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_image, (0, 0))
    screen.blit(strawberry , strawberry_rect)
    screen.blit(text, text_rect)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()