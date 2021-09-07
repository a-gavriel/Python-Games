
import pygame


sign = lambda x: (1, -1)[x < 0]




def Collide(GameObjectA, GameObjectB):
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
  if (GameObjectA.left < GameObjectB.right) and (GameObjectA.right > GameObjectB.left) and \
      (GameObjectA.top < GameObjectB.bottom) and (GameObjectA.bottom > GameObjectB.top):
    return True
  else:
    return False


def ball_player_collision(ball, player):
  """
  Determines if the ball collides with the player and updates the speed_x of the ball accordingly depending on the collision offset
  """
  ball.speed_y = - abs(ball.speed_y)
  temp_rect = ( player.left - ball.width, player.top, \
      player.width + 2* ball.width, player.height )
  offset = ball.get_center()[0] - (temp_rect[0] + temp_rect[2]/2)
  offset_normalized = offset / temp_rect[2]
  ball.speed_x = (offset_normalized * ball.MAX_SPEED)

def ball_brick_collision(ball, brickRect):
  if ball.speed_x == 0:
    ball.speed_y = -ball.speed_y
  else:
    if ball.left >= brickRect.right or \
      ball.right <= brickRect.left:
      ball.speed_x = -ball.speed_x
    if ball.bottom >= brickRect.top or \
      ball.top <= brickRect.bottom:
      ball.speed_y = -ball.speed_y
    
  