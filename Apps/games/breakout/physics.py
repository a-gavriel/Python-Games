
import pygame
from constants import *

sign = lambda x: (1, -1)[x < 0]




def Collide(GameObjectA, GameObjectB):
  """
  Collide(GameObjectA, GameObjectB)

  Determines if GameObjectA collides with GameObjectB.


  Parameters
  ----------
  GameObjectA : GameObject
      First rectangle
  GameObjectB : GameObject
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


def collide_list(GameObjectA, GameObjectList):
  for i,cur in enumerate(GameObjectList):
    if Collide(GameObjectA, cur):
      return i
  return -1


def ball_brick_collision(ball, brickRect):
  if ball.speed_x == 0:
    ball.speed_y = -ball.speed_y
  else:
    if abs(ball.bottom - brickRect.top) < COLLISION_TOL or \
      abs(ball.top - brickRect.bottom) < COLLISION_TOL:
      ball.speed_y = -ball.speed_y
    elif abs(ball.left - brickRect.right) < COLLISION_TOL or \
      abs(ball.right - brickRect.left) < COLLISION_TOL:
      ball.speed_x = -ball.speed_x
    
  