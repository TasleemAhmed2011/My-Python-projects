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
bullet_sound = pygame.mixer.Sound("bullet.wav")
bomb_sound = pygame.mixer.Sound("bomb.wav")
gameover_sound = pygame.mixer.Sound("gameover.wav")
hit_sound = pygame.mixer.Sound("hit.wav")
lose_life_sound = pygame.mixer.Sound("bomb.wav")
win_sound = pygame.mixer.Sound("hit.wav")
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
bomb_img = pygame.transform.scale(load_image("bomb.png"), (64, 64))
bombs = []  # List to store active bombs
bomb_speed = 5
bomb_chance = 0.003  # chance per frame per enemy

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
  {"num_enemies": 3, "enemy_speed": 3, "bomb_chance": 0.002, "bomb_speed": 3},
  {"num_enemies": 4, "enemy_speed": 4, "bomb_chance": 0.0025, "bomb_speed": 4},
  {"num_enemies": 4, "enemy_speed": 4.5, "bomb_chance": 0.003, "bomb_speed": 4.7},
  {"num_enemies": 6, "enemy_speed": 5, "bomb_chance": 0.0045, "bomb_speed": 5.5},
  {"num_enemies": 7, "enemy_speed": 6, "bomb_chance": 0.006, "bomb_speed": 6.5},
]
level_complete = False
win = False

def generate_level_thresholds():
  steps = [10, 13, 15, 18, 20]
  thresholds = []
  last = 0
  for step in steps:
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

def win_text():
  win_font = pygame.font.Font("freesansbold.ttf", 64)
  win_text = win_font.render("YOU WIN!", True, (0, 255, 0))
  screen.blit(win_text, (220, 200))
  restart_text = restart_font.render("Press R to Play Again", True, (255, 255, 0))
  screen.blit(restart_text, (220, 300))

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

def show_instructions():
  screen.fill((0, 0, 0))
  screen.blit(background_img, (0, 0))
  title_font = pygame.font.Font("freesansbold.ttf", 30)
  text_font = pygame.font.Font("freesansbold.ttf", 24)
  y = 40
  lines = [
    "SPACE INVADERS POWER-UPS (Levels 4 & 5):",
    "",
    "1. Double Bullet: Fires two bullets at once for 7 seconds.",
    "2. Double Speed: Player moves twice as fast for 7 seconds.",
    "3. Slow Aliens: Aliens move slower for 10 seconds.",
    "4. Slow Bombs: Bombs fall slower for 10 seconds.",
    "5. Bomb Freeze: Bombs stop falling for 10 seconds.",
    "",
    "Collect power-ups by touching them with your jet!",
    "",
    "Press SPACE to start the game."
  ]
  for line in lines:
    if line == "":
      y += 18
      continue
    if y == 40:
      surf = title_font.render(line, True, (255, 255, 0))
    else:
      surf = text_font.render(line, True, (255, 255, 255))
    screen.blit(surf, (screen_width // 2 - surf.get_width() // 2, y))
    y += surf.get_height() + 8
  pygame.display.update()
  waiting = True
  while waiting:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        waiting = False

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

def fire_double_bullet(x, y):
  global bullet_state
  bullet_state = "fire"
  if not game_over:
    bullet_sound.play()
  screen.blit(bullet_img, (x + 6, y + 10))
  screen.blit(bullet_img, (x + 26, y + 10))

def isCollision(x1, y1, x2, y2, dist=27):
  distance = math.hypot(x1 - x2, y1 - y2)
  return distance < dist

def reset_game():
  global PlayerX, playerX_change, bulletX, bulletY, bullet_state, score_value, lives, game_over, invincible, bombs, level, level_score_thresholds, enemyX, enemyY, win
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
  win = False
  level_score_thresholds = generate_level_thresholds()
  set_level(level)
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

# --- POWER-UP LOGIC ---
powerup_types = [
  {"name": "Double Bullet", "color": (0, 255, 255), "duration": 420},  # 7s
  {"name": "Double Speed", "color": (255, 255, 0), "duration": 420},   # 7s
  {"name": "Slow Aliens", "color": (0, 255, 0), "duration": 600},      # 10s
  {"name": "Slow Bombs", "color": (255, 0, 255), "duration": 600},     # 10s
  {"name": "Bomb Freeze", "color": (255, 128, 0), "duration": 600},    # 10s
]
powerup_img = pygame.Surface((32, 32), pygame.SRCALPHA)
pygame.draw.circle(powerup_img, (255, 255, 255), (16, 16), 16)
powerups = []  # [x, y, type_index]
active_powerups = {}  # type_index: frames_left

def spawn_powerup():
  # Only spawn in level 4 or 5, and max 4-5 per level
  if level < 4:
    return
  if len(powerups) >= 5:
    return
  if random.random() < 0.003:  # chance per frame
    px = random.randint(32, screen_width - 64)
    py = -32
    t = random.randint(0, len(powerup_types) - 1)
    powerups.append([px, py, t])

def draw_powerup(x, y, t):
  color = powerup_types[t]["color"]
  pygame.draw.circle(screen, color, (int(x) + 16, int(y) + 16), 16)
  # Draw first letter of powerup
  label = pygame.font.Font("freesansbold.ttf", 18).render(powerup_types[t]["name"][0], True, (0, 0, 0))
  screen.blit(label, (x + 8, y + 6))

def apply_powerup(t):
  active_powerups[t] = powerup_types[t]["duration"]

def update_powerups():
  global bulletY_change, bomb_speed, bomb_chance, playerX_change, enemyX_change
  # Double Bullet: handled in bullet firing
  # Double Speed: handled in movement
  # Slow Aliens: halve enemyX_change
  # Slow Bombs: halve bomb_speed
  # Bomb Freeze: set bomb_chance to 0
  # Reset all to normal first
  for i in range(num_of_enemies):
    enemyX_change[i] = level_settings[level - 1]["enemy_speed"]
  bs = level_settings[level - 1]["bomb_speed"]
  bc = level_settings[level - 1]["bomb_chance"]
  global bomb_speed, bomb_chance
  bomb_speed = bs
  bomb_chance = bc
  # Apply active powerups
  if 2 in active_powerups:  # Slow Aliens
    for i in range(num_of_enemies):
      enemyX_change[i] = level_settings[level - 1]["enemy_speed"] * 0.5
  if 3 in active_powerups:  # Slow Bombs
    bomb_speed = bs * 0.4
  if 4 in active_powerups:  # Bomb Freeze
    bomb_chance = 0

def tick_powerups():
  expired = []
  for t in list(active_powerups):
    active_powerups[t] -= 1
    if active_powerups[t] <= 0:
      expired.append(t)
  for t in expired:
    del active_powerups[t]

def show_active_powerups():
  y = 60
  for t in active_powerups:
    name = powerup_types[t]["name"]
    time_left = int(active_powerups[t] / 60) + 1
    surf = pygame.font.Font("freesansbold.ttf", 20).render(f"{name}: {time_left}s", True, powerup_types[t]["color"])
    screen.blit(surf, (screen_width - 220, y))
    y += 28

# --- END POWER-UP LOGIC ---

running = True
clock = pygame.time.Clock()

show_instructions()
set_level(level)
show_level(level)

while running:
  screen.fill((0, 0, 0))
  screen.blit(background_img, (0, 0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if not game_over and not win:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
          playerX_change = -5
          if 1 in active_powerups:  # Double Speed
            playerX_change *= 2
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
          playerX_change = 5
          if 1 in active_powerups:
            playerX_change *= 2
        if event.key == pygame.K_SPACE and bullet_state == "ready":
          bulletX = PlayerX
          if 0 in active_powerups:
            fire_double_bullet(bulletX, bulletY)
          else:
            fire_bullet(bulletX, bulletY)
      if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a, pygame.K_d]:
        playerX_change = 0
    else:
      if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
        reset_game()
        show_level(level)

  if not game_over and not win:
    # Player Movement
    move_speed = playerX_change
    if 1 in active_powerups and move_speed != 0:
      move_speed = 10 if move_speed > 0 else -10
    PlayerX += move_speed
    PlayerX = max(0, min(PlayerX, screen_width - 64))

    # Enemy Movement and Difficulty Scaling
    enemies_killed = 0
    for i in range(num_of_enemies):
      enemyX[i] += enemyX_change[i]
      if enemyX[i] <= 0 or enemyX[i] >= screen_width - 64:
        enemyX_change[i] *= -1
        enemyY[i] += enemyY_change[i]

      # Draw the enemy
      enemy(enemyX[i], enemyY[i], i)

      # Drop bombs randomly
      if random.random() < bomb_chance:
        bombs.append([enemyX[i] + 32, enemyY[i] + 64])
        if not game_over:
          bomb_sound.play()  # Play bomb sound when dropped

      # Enemy reaches bottom: lose 2 lives, reset enemy
      if enemyY[i] > 340:
        lives -= 2
        if lives <= 0:
          lives = 0
          game_over = True
          pygame.mixer.music.stop()
          bullet_sound.stop()
          bomb_sound.stop()
          hit_sound.stop()
          gameover_sound.play()
          break
        else:
          lose_life_sound.play()
          # Reset enemy position
          enemyX[i] = random.randint(0, screen_width - 64)
          enemyY[i] = random.randint(enemy_start_Y_min, enemy_start_Y_max)
          pygame.display.update()
          pygame.time.delay(600)
          continue

      # Collision Check and Score Update
      if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
        bulletY = player_start_Y
        bullet_state = "ready"
        score_value += 1
        if not game_over:
          hit_sound.play()
        enemyX[i] = random.randint(0, screen_width - 64)
        enemyY[i] = random.randint(enemy_start_Y_min, enemy_start_Y_max)
        enemies_killed += 1

    # Level up if enough score (using thresholds)
    if level < max_level and score_value >= level_score_thresholds[level]:
      level += 1
      set_level(level)
      lives += 2  # Give one revive
      show_level(level)

    # Win condition: beat final level threshold
    if level == max_level and score_value >= level_score_thresholds[-1]:
      win = True
      pygame.mixer.music.stop()
      win_sound.play()

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
          bomb_sound.play()
        invincible = invincible_time
        if lives <= 0:
          game_over = True
          pygame.mixer.music.stop()
          bullet_sound.stop()
          bomb_sound.stop()
          hit_sound.stop()
          gameover_sound.play()
          break

    # Bullet Movement
    if bulletY <= 0:
      bulletY = player_start_Y
      bullet_state = "ready"
    elif bullet_state == "fire":
      if 0 in active_powerups:
        fire_double_bullet(bulletX, bulletY)
      else:
        fire_bullet(bulletX, bulletY)
      bulletY -= bulletY_change

    # Player hit by enemy (touch)
    if invincible == 0:
      for i in range(num_of_enemies):
        if isCollision(enemyX[i], enemyY[i], PlayerX, PlayerY, 40):
          lives -= 1
          invincible = invincible_time
          if not game_over:
            bomb_sound.play()
          if lives <= 0:
            game_over = True
            pygame.mixer.music.stop()
            bullet_sound.stop()
            bomb_sound.stop()
            hit_sound.stop()
            gameover_sound.play()
            break

    # Invincibility frames
    if invincible > 0:
      invincible -= 1

    # --- POWER-UP SPAWN AND HANDLING ---
    if level >= 4:
      spawn_powerup()
      for p in powerups[:]:
        p[1] += 3
        draw_powerup(p[0], p[1], p[2])
        if p[1] > screen_height:
          powerups.remove(p)
        elif isCollision(p[0], p[1], PlayerX + 16, PlayerY + 16, 32):
          if not game_over and not win:
            apply_powerup(p[2])
          powerups.remove(p)

    # Update and tick powerups
    if active_powerups:
      update_powerups()
      tick_powerups()
      show_active_powerups()

    # Drawing Player, Score, Lives
    player(PlayerX, PlayerY, visible=(invincible % 10 < 5))
    show_score(textX, textY)
    show_lives(screen_width - 120, 10, lives)
  elif win:
    win_text()
  else:
    game_over_text()

  pygame.display.update()
  clock.tick(60)
