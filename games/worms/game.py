import pygame
pygame.init()
#
###


class Player:
    def __init__(self,x,y):
        self.size = 16
        self.image = pygame.Surface((self.size, self.size))  # Create Player Image
        self.image.fill(colors["RED"])  # Fill Player Red
        self.rect = pygame.Rect((x, y), (16, 16))  # Create Player Rect
        self.zoom = 1
        self.speed = 8
        self.camera = -1*x//2,-1*y//2

    def move_camera(self, dir_):

        print(f"camera old {self.camera}", end=" - ")

        pos_x, pos_y = self.camera  # Split camara_pos

        if dir_ == 1:
            pos_y += self.speed  # Move Camara Coord Against Player Rect
        if dir_ == 2:
            pos_x += self.speed
        if dir_ == 3:
            pos_y -= self.speed
        if dir_ == 4:
            pos_x -= self.speed

        if self.rect.x < W_WIDTH//2:  # Simple Sides Collision            
            pos_x = 0 # Reset Camera Pos Coord        
        elif self.rect.x > WIDTH - W_WIDTH//2 - self.size//2:            
            pos_x = -960
        if self.rect.y < W_HEIGHT//2:
            pos_y = 0
        elif self.rect.y > HEIGHT - W_HEIGHT//2 - self.size//2:            
            pos_y = -540


        self.camera = pos_x, pos_y

        print(f"new {self.camera}")
        return self.camera
        
    def zoomin(self,val):
        if val == 5:
            self.zoom -= 1
        else:
            self.zoom += 1        

        if self.zoom < 1:
            self.zoom = 1
        elif self.zoom > 2:
            self.zoom = 2

    def move(self, dir_):

        print(f"old {self.rect.x} , {self.rect.y}", end= " - ")

        if dir_ == 1:
            self.rect.y -= self.speed
        elif dir_ == 2:
            self.rect.x -= self.speed
        elif dir_ == 3:
            self.rect.y += self.speed
        else:
            self.rect.x += self.speed

        if self.rect.x < 0:  # Simple Sides Collision
            self.rect.x = 0  # Reset Player Rect Coord            
        elif self.rect.x > WIDTH - self.size :
            self.rect.x = WIDTH - self.size           
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > HEIGHT - self.size:
            self.rect.y = HEIGHT - self.size

        print(f"new {self.rect.x} , {self.rect.y}")

        return self.move_camera(dir_)

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
    player = Player(W_WIDTH,W_HEIGHT)  # Initialize Player Class
    camera_pos = -1*W_WIDTH//2,-1*W_HEIGHT//2  # Create Camara Starting Position
    #
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        key = pygame.key.get_pressed()  # Get Keyboard Input
        if key[pygame.K_w]:  # Check Key
            player.move(1)                
        if key[pygame.K_a]:
            player.move(2)                
        if key[pygame.K_s]:
            player.move(3)                
        if key[pygame.K_d]:
            player.move(4)                
        if key[pygame.K_q]:
            player.zoomin(5)
        elif key[pygame.K_e]:
            player.zoomin(6)
        #
        # Run Player Move Function And Return New Camera Pos
        
        #
        # Fill The Background White To Avoid Smearing
        #display.fill(colors["WHITE"])
        # Refresh The World So The Player Doesn't Smear
        #world.fill(colors["BLACK"])
        world.blit(image_bg, (0, 0))
        for x in range(10):
            pygame.draw.rect(world, colors["BLUE"], ((x*100, x*100), (20, 20)))
        player.render(world)  # Render The Player

        if player.zoom > 1:
            frame = pygame.transform.scale(world, (W_WIDTH, W_HEIGHT))
            display.blit(frame, frame.get_rect())
        else:
            world_padded = pygame.Surface((WIDTH+W_WIDTH, HEIGHT+W_HEIGHT))
            world_padded.fill(colors["GREEN"])
            display.blit(world_padded,(0,0))
            display.blit(world, player.camera)  # Render Map To The Display
        #
        pygame.display.flip()


###
#
if __name__ in "__main__":

    WIDTH, HEIGHT = 1920,1080
    SCALE_ZOOM = 2
    W_WIDTH, W_HEIGHT = WIDTH//SCALE_ZOOM , HEIGHT//SCALE_ZOOM
    display = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
    
    image_bg = pygame.image.load(r'test.png').convert()
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
