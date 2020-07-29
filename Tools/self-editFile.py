highscores = [90, 70, 70, 50, 30]

print (highscores)



def savescore_aux(scores, score):  
  for i,s in enumerate(scores):
    if score > s:
      scores.insert(i,score)
      break;
  if len(scores) == 6:
    scores.pop(-1)

def savescore(score): 
  import ast 
  print("saving ", score)
  with open(__file__, 'r') as f:
      lines = f.read().split('\n')
      scores_string = (lines[0].split(' = ')[-1])
      scores_list = ast.literal_eval(scores_string) 
      print(scores_list,type(scores_list))
      savescore_aux(scores_list, score)
      print(scores_list,type(scores_list))
      new_line = 'highscores = {}'.format(scores_list)
      new_file = '\n'.join([new_line] + lines[1:])

  with open(__file__, 'w') as f:
      f.write('\n'.join([new_line] + lines[1:]))

from random import randrange
savescore(randrange(10)*10)