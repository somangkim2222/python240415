import pygame
import random

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색깔 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 블록 파라미터
BLOCK_WIDTH = 60
BLOCK_HEIGHT = 20
BLOCK_ROWS = 5
BLOCK_COLUMNS = 10

# 패들 파라미터
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20

# 공 파라미터
BALL_RADIUS = 10

# 게임 속도 설정
FPS = 60

# 블록 클래스
class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([BLOCK_WIDTH, BLOCK_HEIGHT])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# 패들 클래스
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([PADDLE_WIDTH, PADDLE_HEIGHT])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
        self.rect.y = SCREEN_HEIGHT - PADDLE_HEIGHT

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x > SCREEN_WIDTH - PADDLE_WIDTH:
            self.rect.x = SCREEN_WIDTH - PADDLE_WIDTH

# 공 클래스
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([BALL_RADIUS * 2, BALL_RADIUS * 2])
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, RED, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed_x = 3
        self.speed_y = 3

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - BALL_RADIUS * 2:
            self.speed_x = -self.speed_x
        if self.rect.y <= 0 or self.rect.y >= SCREEN_HEIGHT - BALL_RADIUS * 2:
            self.speed_y = -self.speed_y

# 메인 함수
def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("블록 깨기 게임")

    all_sprites_list = pygame.sprite.Group()
    block_list = pygame.sprite.Group()
    paddle = Paddle()
    ball = Ball()
    all_sprites_list.add(paddle)
    all_sprites_list.add(ball)

    for i in range(BLOCK_ROWS):
        for j in range(BLOCK_COLUMNS):
            block = Block(BLUE, j * (BLOCK_WIDTH + 2) + 1, i * (BLOCK_HEIGHT + 2) + 1)
            block_list.add(block)
            all_sprites_list.add(block)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites_list.update()

        if pygame.sprite.spritecollide(ball, block_list, True):
            ball.speed_y = -ball.speed_y

        if pygame.sprite.collide_rect(ball, paddle):
            if ball.speed_y > 0:
                ball.speed_y = -ball.speed_y

        screen.fill(BLACK)
        all_sprites_list.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    pygame.mixer.quit()  # Pygame의 오디오 출력을 비활성화합니다.
    main()
