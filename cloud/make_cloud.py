from typing import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

import jpype
from konlpy.tag import Okt 

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

def tokenizer_konlpy(text):
  okt = Okt()
  return [word for word in okt.nouns(text) if len(word) >1]


def wordCloud(lyric_lst, language):
  if language == 'en':
    stopword = stopwords.words('english')
  else:
    stopword = []
    with open('cloud/stopwords.txt', 'r', encoding='UTF8') as file:
      for text in file:
        stopword.append(text.strip('\n'))

  # 불용어에 없는 단어들만 추출.
  normalized_lyric = []
  for lyric in lyric_lst:
    if lyric not in stopword:
      normalized_lyric.append(lyric)

  normalized_lyric = " ".join(normalized_lyric)

  # tokenize
  if language == 'ko':
    word = tokenizer_konlpy(normalized_lyric)
  else:
    word = word_tokenize(normalized_lyric)

  count = Counter(word)
  word_list = count.most_common(100)

  wordcloud = WordCloud(font_path='cloud/font/NanumGothic-Regular.ttf', 
                        background_color = 'white',
                        width=512, height=512,
                        max_font_size=500,
                        max_words=100)
  wordcloud.generate_from_frequencies(dict(word_list))


  plt.figure(figsize=(22,22)) #이미지 사이즈 지정
  plt.imshow(wordcloud, interpolation='lanczos') #이미지의 부드럽기 정도
  plt.axis('off') #x y 축 숫자 제거
  plt.show() 
