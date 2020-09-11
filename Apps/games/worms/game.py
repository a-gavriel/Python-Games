import pygame
pygame.init()
#
###


class Player:
    def __init__(self):
        self.image = pygame.Surface((16, 16))  # Create Player Image
        self.image.fill(colors["RED"])  # Fill Player Red
        self.rect = pygame.Rect((50, 50), (16, 16))  # Create Player Rect
        self.zoom = 1

    def move_camera(self, camera_pos, dir):
        pos_x, pos_y = camera_pos  # Split camara_pos

        if dir_ == 1:
            pos_y += 8  # Move Camara Coord Against Player Rect
        if dir_ == 2:
            pos_x += 8
        if dir_ == 3:
            pos_y -= 8
        if dir_ == 4:
            pos_x -= 8
        

    def move(self, camera_pos):
        pos_x, pos_y = camera_pos  # Split camara_pos
        #
        key = pygame.key.get_pressed()  # Get Keyboard Input
        if key[pygame.K_w]:  # Check Key
            self.rect.y -= 8  # Move Player Rect Coord
            pos_y += 8  # Move Camara Coord Against Player Rect
        if key[pygame.K_a]:
            self.rect.x -= 8
            pos_x += 8
        if key[pygame.K_s]:
            self.rect.y += 8
            pos_y -= 8
        if key[pygame.K_d]:
            self.rect.x += 8
            pos_x -= 8
        if key[pygame.K_q]:
            self.zoom -= 0.1
        elif key[pygame.K_e]:
            self.zoom += 0.1

        if self.zoom < 1:
            self.zoom = 1
        elif self.zoom > 3:
            self.zoom = 3
            
        #
        if self.rect.x < 0:  # Simple Sides Collision
            self.rect.x = 0  # Reset Player Rect Coord
            pos_x = camera_pos[0]  # Reset Camera Pos Coord
        elif self.rect.x > 984:
            self.rect.x = 984
            pos_x = camera_pos[0]
        if self.rect.y < 0:
            self.rect.y = 0
            pos_y = camera_pos[1]
        elif self.rect.y > 984:
            self.rect.y = 984
            pos_y = camera_pos[1]
        #
        return (pos_x, pos_y)  # Return New Camera Pos

    def render(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))
###
#
#
###


def Main(display, clock):
    world = pygame.Surface((WIDTH, HEIGHT))  # Create Map Surface
    world.blit(image_bg, (0, 0))
    #world.fill(colors["BLACK"])  # Fill Map Surface Black
    for x in range(10):
        # Put Blue Rectagles On Map Surface
        pygame.draw.rect(world, colors["BLUE"], ((x*100, x*100), (20, 20)))
    #
    player = Player()  # Initialize Player Class
    camera_pos = (192, 192)  # Create Camara Starting Position
    #
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        #
        # Run Player Move Function And Return New Camera Pos
        camera_pos = player.move(camera_pos)
        #
        # Fill The Background White To Avoid Smearing
        #display.fill(colors["WHITE"])
        # Refresh The World So The Player Doesn't Smear
        #world.fill(colors["BLACK"])
        world.blit(image_bg, (0, 0))
        for x in range(10):
            pygame.draw.rect(world, colors["BLUE"], ((x*100, x*100), (20, 20)))
        player.render(world)  # Render The Player

  
        frame = pygame.transform.scale(world, (int(WIDTH/player.zoom), int(HEIGHT/player.zoom)))
        display.blit(frame, frame.get_rect())
        
        #  display.blit(world, camera_pos)  # Render Map To The Display
        #
        pygame.display.flip()


###
#
if __name__ in "__main__":
    display = pygame.display.set_mode((640, 360))
    image_bg = pygame.image.load(r'test.png').convert()

    WIDTH, HEIGHT = (1920,1080)
    
    pygame.display.set_caption("Scrolling Camera")
    clock = pygame.time.Clock()
    #
    global colors  # Difign Colors
    colors = {
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255),
        "BLACK": (0, 0, 0)
    }
    Main(display, clock)  # Run Main Loop
