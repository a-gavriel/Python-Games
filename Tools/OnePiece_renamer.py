import os
import sys
import random
import shutil
import string


def episode_conv(num) -> tuple:
  
  num = int(num)

  seasons_episodes = { #TVDB Air
    1:8,
    2:22,
    3:17,
    4:13,
    5:9,
    6:22,
    7:39,
    8:13,
    9:52,
    10:31,
    11:99,
    12:56,
    13:100,
    14:35,
    15:62,
    16:49,
    17:118,
    18:33,
    19:98,
    20:14,
    21:999
  }
  """

  seasons_episodes = {
    1 : 61,
    2 : 16,
    3 : 15,
    4 : 51,
    5 : 30,
    6 : 33,
    7 : 22,
    8 : 35,
    9 : 21,
    10 : 22,
    11 : 30,
    12 : 45,
    13 : 26,
    14 : 14,
    15 : 37,
    16 : 58,
    17 : 62,
    18 : 50,
    19 : 122,
    20 : 32,
    21 : 95,
    22 : 999
  }"""

  carriage = 0
  for season_n, episodes_total in seasons_episodes.items():
    added = episodes_total + carriage
    if num <= added:
      return (zpad(season_n,2), zpad(num - carriage, 3))
    carriage = added

  raise Exception(f"Error in episode:{num}.")

def zpad(n, digits: int) -> str:
  n = str(int(n))
  while len(n) < digits:
    n = "0" + n
  return n

def iterating(rootdir):
    for subdir, dirs, files in os.walk(rootdir):
        foldername = subdir[ len(rootdir) + 1: ]
        if ("missing" in foldername.lower() ):
          for filename in files:      
              extension = filename[ filename.index(".") + 1 :]
              abs_num = get_num_from_name(filename[ :filename.index(".") ])
              if len(abs_num) == 4:
                season_s, new_number_s = episode_conv(int(abs_num))
                fullname = str( os.path.join(subdir, filename))
                new_name = f'One Piece - s{season_s}e{new_number_s} - [{zpad(abs_num,4)}].{extension}'
                new_fullname = f'{rootdir}\\Season {season_s}\\{new_name}'
                print(f"--\n<-:{fullname}\n->:{new_fullname}")
                try:
                  shutil.move(fullname, new_fullname)
                except:
                  print("Error in try, ", filename)
              else:
                print(f"Error in episode {filename}")
                len_nums = len(abs_num) //2
                a,b = abs_num[:len_nums] , abs_num[len_nums:]
                a_season, a_new_num = episode_conv(int(a))
                b_season, b_new_num = episode_conv(int(b))
                print(f"Absolute number is {abs_num}, divided in 2 corresponds to:\n\t{a} -> {a_season, a_new_num}" + \
                  f"\n\t{b} -> {b_season, b_new_num}")
                
                fullname = str( os.path.join(subdir, filename))
                new_name = f'One Piece - s{a_season}e{a_new_num}-e{b_new_num} - [{zpad(a,4)} - {zpad(b,4)}].{extension}'
                new_fullname = f'{rootdir}\\Season {a_season}\\{new_name}'
                try:
                  shutil.move(fullname, new_fullname)
                except:
                  print("Error in try, ", filename)

def get_num_from_name(name : str) -> str :  
  #name = name[ name.index("[") + 1 :]
  filtered_name = ""
  for letter in name:
    if letter in string.digits:
      filtered_name += letter
  return filtered_name
  

def main():
  iterating("D:\\Videos\\PLEX\\Plex One Piece\\One Piece")

if __name__ == "__main__":
  main()