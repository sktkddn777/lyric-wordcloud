import requests
import json
import xmltodict


class Vibe:
  
  def __init__(self):
    self.url = 'https://apis.naver.com/vibeWeb/musicapiweb/v4/searchall'
    self.lyric_url = 'https://apis.naver.com/vibeWeb/musicapiweb/track/{}/info'
    self.query = '?query='

  def find(self, singer_name, song):
    self.query += (singer_name+' '+song)
    response = requests.get(self.url + self.query)
    if response.status_code == 200:
      try:
        # xml로 api값이 제공되기에 json으로 변환.
        response = json.loads(json.dumps(xmltodict.parse(response.text), ensure_ascii=False))

        track = response['response']['result']['trackResult']['tracks']['track']

        if type(track) is dict:
          title = track['trackTitle'].replace(' ','')
          if title == song:
            track_id = track['trackId']
            return track_id
        else:
          for t in track:
            title = t['trackTitle'].replace(' ','')
            if title == song:
              track_id = t['trackId']
              return track_id
      except:
        print("가수이름이나 노래제목을 다시 확인하세요")
  
  def lyrics(self, track_id):
    response = requests.get(self.lyric_url.format(track_id))
    if response.status_code == 200:
      # xml로 api값이 제공되기에 json으로 변환.
      response = json.loads(json.dumps(xmltodict.parse(response.text), ensure_ascii=False))

      try:
        lyric_lst = list(response['response']['result']['trackInformation']['lyric'])
        lyric = []

        word = ''
        for l in lyric_lst:
          if l == ' ' or l == '\n':
            lyric.append(word)
            word = ''
          else:
            word += l
    
        return lyric
      except:
        print("NO lyric")

