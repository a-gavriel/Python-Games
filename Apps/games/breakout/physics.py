
sign = lambda x: (1, -1)[x < 0]


# TODO: verify offset
## shoueld call RecA = ball for correct offset
def colission(RectA, RectB):
  playerx = RectB.get_xpos()    
  if (RectA.left() <= RectB.right() and RectA.right() >= RectB.left() and
     RectA.top() <= RectB.bottom() and RectA.bottom() >= RectB.top() ):
     RectA.pong.play(0)
     offset = RectA.xpos - playerx #unknown error if replaced with RectB.xpos or RectB.get_xpos()
     offsetF = offset / RectB.width
     side = sign(offset)
     offsetF = abs(offsetF)     
     if offsetF > 0.7:
       offset = side * 7
     elif offsetF > 0.3:
       offset = side * 6
     else:
       offset = side * 5
     return (1,offset)
  else:
    return (0,0) 
  