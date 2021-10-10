from api.vibe_api import Vibe
from cloud.make_cloud import wordCloud

def find_id():
  
  singer_name = input("가수 이름: ")
  song = input("노래 이름: ")
  vibe = Vibe()
  lyric = vibe.lyrics(vibe.find(singer_name, song))
  return lyric

if __name__ == "__main__":
  lyric = find_id()
  if lyric:
    wordCloud(lyric)
  