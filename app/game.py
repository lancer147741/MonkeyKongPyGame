import pygame

# инизалиция pygame
pygame.init()

# размер окна
window_size = (1280, 720)

# Название окна - название игры
pygame.display.set_caption("Monkey kong")

# создаем окно
screen = pygame.display.set_mode(window_size)

# Загрузка изображений
background_image = pygame.image.load("../image/background.png")
hero_image = pygame.image.load("../image/hero.png")
monkey_image = pygame.image.load("../image/monkey.png")
ball_image = pygame.image.load("../image/ball.png")
princess_image = pygame.image.load("../image/princess.png")
stairs = pygame.image.load("../image/stairs.png")

# Задаем фон и подгоняем масштаб под размер окна
background_image = pygame.transform.scale(background_image, window_size)

# накладываем изображение на поверхность
screen.blit(background_image, (0, 0))

# делаем видимость обновленияm в коде
pygame.display.flip()

# показываем окно, пока пользователь не нажмет кнопку "Закрыть"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

