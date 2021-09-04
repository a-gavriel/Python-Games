
import pygame


sign = lambda x: (1, -1)[x < 0]


def Collide(RectA, RectB):
  """
  Collide(RectA, RectB)

  Determines if RectA collides with RectB.


  Parameters
  ----------
  RectA : pygame.Rect
      First rectangle
  RectB : pygame.Rect
      Second rectangle

  Returns
  -------
  Bool
      If both rectangles collide.

  """
  if (RectA.left < RectB.right) and (RectA.right > RectB.left) and \
      (RectA.top < RectB.bottom) and (RectA.bottom > RectB.top):
    return True
  else:
    return False


def ball_player_collision(ball, player):
  """
  Determines if the ball collides with the player and updates the speed_x of the ball accordingly depending on the collision offset
  """
  ball.speed_y = - abs(ball.speed_y)
  temp_rect = pygame.Rect( player.Rect.left - ball.Rect.width, player.Rect.top, \
      player.Rect.width + 2* ball.Rect.width, player.Rect.height )
  offset = ball.Rect.centerx - temp_rect.centerx
  offset_normalized = offset / temp_rect.width
  ball.speed_x = round(offset_normalized * ball.MAX_SPEED,0)

def ball_brick_collision(ball, brickRect):
  if ball.speed_x == 0:
    ball.speed_y = -ball.speed_y
  else:
    if ball.Rect.centerx <= brickRect.right or \
      ball.Rect.centerx >= brickRect.left:
      ball.speed_x = -ball.speed_x
    if ball.Rect.centery <= brickRect.top or \
      ball.Rect.centery >= brickRect.bottom:
      ball.speed_y = -ball.speed_y
    else:
      ball.speed_y = -ball.speed_y
  