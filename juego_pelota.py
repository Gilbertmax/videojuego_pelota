import pygame

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Juego de pelota")

# Configurar la pelota
ball_color = (255, 255, 255)
ball_radius = 20
ball_position = [size[0] // 2, size[1] // 2]
ball_speed = [5, 5]

# Bucle principal del juego
done = False
while not done:
    # Manejar eventos de la pantalla
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Invertir la dirección de la pelota al hacer clic en la pantalla
            ball_speed[0] = -ball_speed[0]
            ball_speed[1] = -ball_speed[1]

    # Mover la pelota
    ball_position[0] += ball_speed[0]
    ball_position[1] += ball_speed[1]

    # Rebotar la pelota al llegar a los bordes de la pantalla
    if ball_position[0] < ball_radius or ball_position[0] > size[0] - ball_radius:
        ball_speed[0] = -ball_speed[0]
    if ball_position[1] < ball_radius or ball_position[1] > size[1] - ball_radius:
        ball_speed[1] = -ball_speed[1]

    # Dibujar la pelota
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, ball_color, ball_position, ball_radius)
    pygame.display.flip()

    # Esperar un poco antes de volver a dibujar
    pygame.time.wait(10)

# Cerrar Pygame
pygame.quit()