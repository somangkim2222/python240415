import pygame
import sys

# 게임 설정
WIDTH = 800
HEIGHT = 600
FPS = 60

# 색깔 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 게임 초기화 및 창 설정
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블록 깨기")
clock = pygame.time.Clock()

# 블록 클래스
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

# 플레이어 클래스
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# 공 클래스
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 30
        self.speedx = 5
        self.speedy = -5

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speedx = -self.speedx
        if self.rect.top <= 0:
            self.speedy = -self.speedy
        if self.rect.bottom >= HEIGHT:
            # 공이 바닥에 닿으면 게임 종료
            pygame.quit()
            sys.exit()

# 모든 스프라이트 그룹 설정
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()
player = Player()
ball = Ball()
all_sprites.add(player, ball)

# 블록 생성
for i in range(10):
    block = Block(WHITE, 70, 20)
    block.rect.x = i * 80 + 20
    block.rect.y = 150
    all_sprites.add(block)
    blocks.add(block)

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 게임 업데이트
    all_sprites.update()

    # 공과 패들 충돌 검사
    if pygame.sprite.collide_rect(ball, player):
        ball.speedy = -ball.speedy

    # 공과 블록 충돌 검사
    block_hits = pygame.sprite.spritecollide(ball, blocks, True)
    if block_hits:
        ball.speedy = -ball.speedy

    # 화면 그리기
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 설정
    clock.tick(FPS)

pygame.quit()
sys.exit()
