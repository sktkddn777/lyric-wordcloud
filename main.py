from api.vibe_api import Vibe
from cloud.make_cloud import wordCloud
import re

def find_id():
  singer_name = input("가수 이름: ")
  song = input("노래 이름: ")

  vibe = Vibe()
  lyric = vibe.lyrics(vibe.find(singer_name, song))

  if singer_name.encode().isalpha() and song.encode().isalpha():
    return lyric, 'en'
  return lyric, 'ko'


if __name__ == "__main__":
  lyric, language = find_id()

  if lyric:
    wordCloud(lyric, language)
      

