import math
import random
import pygame
import os

# Screen and Sprites
screen_width = 800
screen_height = 500
player_start_X = 370
player_start_Y = 380
enemy_start_Y_min = 50
enemy_start_Y_max = 150
enemy_speed_X = 4
enemy_speed_Y = 40
bullet_speed = 10
hit_dist = 27
player_lives = 3
invincible_time = 60  # frames

pygame.init()
pygame.mixer.init()  # Initialize the mixer for sound

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

def load_image(filename, size=None):
  if not os.path.exists(filename):
    print(f"Error: Image file '{filename}' not found in {os.getcwd()}")
    pygame.quit()
    exit(1)
  img = pygame.image.load(filename)
  if size:
    img = pygame.transform.scale(img, size)
  return img

icon = load_image("ufo.png")
pygame.display.set_icon(icon)

# --- SOUND EFFECTS AND MUSIC ---
# Place these files in your project directory
bullet_sound = pygame.mixer.Sound("bullet.wav")
bomb_sound = pygame.mixer.Sound("bomb.wav")
gameover_sound = pygame.mixer.Sound("gameover.wav")
hit_sound = pygame.mixer.Sound("hit.wav")
pygame.mixer.music.load("background.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # Loop background music

# PLAYER
player_img = load_image("player.png")
PlayerX = player_start_X
PlayerY = player_start_Y
playerX_change = 0

# ENEMY
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 4

for i in range(num_of_enemies):
  enemy_img.append(load_image("enemy.png"))
  enemyX.append(random.randint(0, screen_width - 64))
  enemyY.append(random.randint(enemy_start_Y_min, enemy_start_Y_max))
  enemyX_change.append(enemy_speed_X)
  enemyY_change.append(enemy_speed_Y)
# BULLET
bullet_img = load_image("bullet.png")
bulletX = 0
bulletY = player_start_Y
bulletX_change = 0
bulletY_change = bullet_speed
bullet_state = "ready"

# BOMB (enemy drops)
# BOMB (enemy drops)
bomb_img = pygame.transform.scale(load_image("bomb.png"), (67, 67))
bombs = []  # List to store active bombs
bomb_speed = 5
bomb_chance = 0.005  # chance per frame per enemy

# LIVES
heart_img = load_image("heart.png", (24, 24))  # Resize heart to 24x24
lives = player_lives
invincible = 0

# SCORE
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# GAME OVER
over_font = pygame.font.Font("freesansbold.ttf", 64)
restart_font = pygame.font.Font("freesansbold.ttf", 32)
game_over = False

# BACKGROUND IMAGE (load once globally)
background_img = load_image("background.png")

# LEVEL SETTINGS
level = 1
max_level = 5
level_settings = [
  {"num_enemies": 3, "enemy_speed": 3, "bomb_chance": 0.003, "bomb_speed": 3},
  {"num_enemies": 4, "enemy_speed": 4, "bomb_chance": 0.005, "bomb_speed": 4},
  {"num_enemies": 5, "enemy_speed": 5, "bomb_chance": 0.007, "bomb_speed": 5},
  {"num_enemies": 6, "enemy_speed": 6, "bomb_chance": 0.009, "bomb_speed": 6},
  {"num_enemies": 7, "enemy_speed": 8, "bomb_chance": 0.012, "bomb_speed": 8},
]
level_complete = False
win = False

# LEVEL SCORE THRESHOLDS (fixed at 15 per level)
def generate_level_thresholds():
  thresholds = []
  last = 0
  for _ in range(max_level):
    step = 15  # Make it easier: always 15 to next level
    last += step
    thresholds.append(last)
  return thresholds

level_score_thresholds = generate_level_thresholds()
def show_score(x, y):
  score = font.render("Score : " + str(score_value), True, (255, 255, 255))
  screen.blit(score, (x, y))

def show_lives(x, y, lives):
  screen.blit(heart_img, (x, y))
  lives_text = font.render(f"x {lives}", True, (255, 255, 255))
  screen.blit(lives_text, (x + 30, y - 2))

def game_over_text():
  over_text = over_font.render("GAME OVER", True, (255, 255, 255))
  screen.blit(over_text, (200, 200))
  restart_text = restart_font.render("Press R to Restart", True, (255, 255, 0))
  screen.blit(restart_text, (250, 300))

def show_level(level):
  level_font = pygame.font.Font("freesansbold.ttf", 48)
  level_text = level_font.render(f"Level {level}", True, (255, 255, 0))
  rule_font = pygame.font.Font("freesansbold.ttf", 28)
  if level < max_level:
    next_score = level_score_thresholds[level]
    rule_text = rule_font.render(f"Reach {next_score} score to unlock next level!", True, (255, 255, 255))
  else:
    rule_text = rule_font.render("This is the final level!", True, (255, 255, 255))
  screen.fill((0, 0, 0))
  screen.blit(background_img, (0, 0))
  screen.blit(level_text, (screen_width // 2 - level_text.get_width() // 2, screen_height // 2 - 60))
  screen.blit(rule_text, (screen_width // 2 - rule_text.get_width() // 2, screen_height // 2 + 10))
  pygame.display.update()
  pygame.time.delay(2200)  # Show for 2.2 seconds

def player(x, y, visible=True):
  if visible:
    screen.blit(player_img, (x, y))

def enemy(x, y, i):
  screen.blit(enemy_img[i], (x, y))

def fire_bullet(x, y):
  global bullet_state
  bullet_state = "fire"
  if not game_over:
    bullet_sound.play()  # Play bullet sound
  screen.blit(bullet_img, (x + 16, y + 10))

def isCollision(x1, y1, x2, y2, dist=27):
  distance = math.hypot(x1 - x2, y1 - y2)
  return distance < dist

def reset_game():
  global PlayerX, playerX_change, bulletX, bulletY, bullet_state, score_value, lives, game_over, invincible, bombs, level, level_score_thresholds, enemyX, enemyY
  PlayerX = player_start_X
  playerX_change = 0
  bulletX = 0
  bulletY = player_start_Y
  bullet_state = "ready"
  score_value = 0
  lives = player_lives
  game_over = False
  invincible = 0
  bombs = []
  level = 1
  level_score_thresholds = generate_level_thresholds()
  set_level(level)
  # Re-initialize enemy positions to match the new num_of_enemies
  enemyX = [random.randint(0, screen_width - 64) for _ in range(num_of_enemies)]
  enemyY = [random.randint(enemy_start_Y_min, enemy_start_Y_max) for _ in range(num_of_enemies)]
  screen.fill((0, 0, 0))
  screen.blit(background_img, (0, 0))
  pygame.mixer.music.play(-1)  # Resume background music

def set_level(lvl):
  global num_of_enemies, enemy_img, enemyX, enemyY, enemyX_change, enemyY_change, bomb_chance, bomb_speed
  settings = level_settings[lvl - 1]
  num_of_enemies = settings["num_enemies"]
  bomb_chance = settings["bomb_chance"]
  bomb_speed = settings["bomb_speed"]
  enemy_img.clear()
  enemyX.clear()
  enemyY.clear()
  enemyX_change.clear()
  enemyY_change.clear()
  for i in range(num_of_enemies):
    enemy_img.append(load_image("enemy.png"))
    enemyX.append(random.randint(0, screen_width - 64))
    enemyY.append(random.randint(enemy_start_Y_min, enemy_start_Y_max))
    enemyX_change.append(settings["enemy_speed"])
    enemyY_change.append(enemy_speed_Y)

running = True
clock = pygame.time.Clock()

set_level(level)
show_level(level)

while running:
  screen.fill((0, 0, 0))
  screen.blit(background_img, (0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if not game_over:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
          playerX_change = -5
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
          playerX_change = 5
        if event.key == pygame.K_SPACE and bullet_state == "ready":
          bulletX = PlayerX
          fire_bullet(bulletX, bulletY)
      if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a, pygame.K_d]:
        playerX_change = 0
    else:
      if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
        reset_game()
        show_level(level)

  if not game_over:
    # Player Movement
    PlayerX += playerX_change
    PlayerX = max(0, min(PlayerX, screen_width - 64))

    # Enemy Movement and Difficulty Scaling
    enemies_killed = 0
    for i in range(num_of_enemies):
      speed_scale = 1 + score_value // 10
      enemyX[i] += enemyX_change[i] * speed_scale
      if enemyX[i] <= 0 or enemyX[i] >= screen_width - 64:
        enemyX_change[i] *= -1
        enemyY[i] += enemyY_change[i]

      # Draw the enemy
      enemy(enemyX[i], enemyY[i], i)

      # Drop bombs randomly
      if random.random() < bomb_chance + 0.001 * score_value:
        bombs.append([enemyX[i] + 32, enemyY[i] + 64])
        if not game_over:
          bomb_sound.play()  # Play bomb sound when dropped

      # Game Over Condition
      if enemyY[i] > 340:
        game_over = True
        pygame.mixer.music.stop()  # Stop all music
        bullet_sound.stop()
        bomb_sound.stop()
        hit_sound.stop()
        gameover_sound.play()  # Play game over sound
        break

      # Collision Check and Score Update
      if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
        bulletY = player_start_Y
        bullet_state = "ready"
        score_value += 1
        if not game_over:
          hit_sound.play()  # Play hit sound
        enemyX[i] = random.randint(0, screen_width - 64)
        enemyY[i] = random.randint(enemy_start_Y_min, enemy_start_Y_max)
        enemies_killed += 1

    # Level up if enough score (using thresholds)
    if level < max_level and score_value >= level_score_thresholds[level]:
      level += 1
      set_level(level)
      lives += 1  # Give one revive
      show_level(level)

    # Bomb Movement and Collision
    for bomb in bombs[:]:
      bomb[1] += bomb_speed
      screen.blit(bomb_img, (bomb[0], bomb[1]))
      if bomb[1] > screen_height:
        bombs.remove(bomb)
      elif invincible == 0 and isCollision(bomb[0], bomb[1], PlayerX + 32, PlayerY + 32, 32):
        bombs.remove(bomb)
        lives -= 1
        if not game_over:
          bomb_sound.play()  # Play bomb sound on hit
        invincible = invincible_time
        if lives <= 0:
          game_over = True
          pygame.mixer.music.stop()  # Stop all music
          bullet_sound.stop()
          bomb_sound.stop()
          hit_sound.stop()
          gameover_sound.play()  # Play game over sound
          break

    # Bullet Movement
    if bulletY <= 0:
      bulletY = player_start_Y
      bullet_state = "ready"
    elif bullet_state == "fire":
      fire_bullet(bulletX, bulletY)
      bulletY -= bulletY_change

    # Player hit by enemy (touch)
    if invincible == 0:
      for i in range(num_of_enemies):
        if isCollision(enemyX[i], enemyY[i], PlayerX, PlayerY, 40):
          lives -= 1
          invincible = invincible_time
          if not game_over:
            bomb_sound.play()  # Play bomb sound on collision
          if lives <= 0:
            game_over = True
            pygame.mixer.music.stop()  # Stop all music
            bullet_sound.stop()
            bomb_sound.stop()
            hit_sound.stop()
            gameover_sound.play()  # Play game over sound
            break

    # Invincibility frames
    if invincible > 0:
      invincible -= 1

    # Drawing Player, Score, Lives
    player(PlayerX, PlayerY, visible=(invincible % 10 < 5))
    show_score(textX, textY)
    show_lives(screen_width - 120, 10, lives)
  else:
    game_over_text()

  pygame.display.update()
  clock.tick(60)
