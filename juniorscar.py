import pygame
import random

# Initialisation de Pygame
pygame.init()
# Paramètres de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Junior's Car")
# Couleurs
blanc = (255, 255, 255)
rouge = (255, 0, 0)
# Chargement des images
voiture_image = pygame.image.load('car.png')
voiture_image = pygame.transform.scale(voiture_image, (50, 100))

# Chargement des images
voiture_image = pygame.image.load('car.png')
voiture_image = pygame.transform.scale(voiture_image, (50, 100))

# Position initiale de la voiture
voiture_x = largeur_fenetre // 2 - 25
voiture_y = hauteur_fenetre - 120
# Vitesse de la voiture
vitesse_voiture = 5

# Position initiale des obstacles
obstacle_x = random.randint(0, largeur_fenetre - 50)
obstacle_y = -50
obstacle_vitesse = 5

try:
    # Boucle principale du jeu
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Déplacement de la voiture
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            voiture_x -= vitesse_voiture
        if keys[pygame.K_RIGHT]:
            voiture_x += vitesse_voiture

        # Déplacement de l'obstacle
        obstacle_y += obstacle_vitesse

        # Gestion des collisions
        if voiture_x < 0:
            voiture_x = 0
        elif voiture_x > largeur_fenetre - 50:
            voiture_x = largeur_fenetre - 50

        if obstacle_y > hauteur_fenetre:
            obstacle_x = random.randint(0, largeur_fenetre - 50)
            obstacle_y = -50

        if (
            voiture_x < obstacle_x + 50
            and voiture_x + 50 > obstacle_x
            and voiture_y < obstacle_y + 50
            and voiture_y + 100 > obstacle_y
        ):
            running = False

        # Effacement de l'écran
        fenetre.fill(blanc)

        # Dessin de la voiture
        fenetre.blit(voiture_image, (voiture_x, voiture_y))

        # Dessin de l'obstacle
        pygame.draw.rect(fenetre, rouge, (obstacle_x, obstacle_y, 50, 50))

        # Mise à jour de l'affichage
        pygame.display.update()

except Exception as e:
    print("Une erreur s'est produite :", e)
    pygame.quit()
