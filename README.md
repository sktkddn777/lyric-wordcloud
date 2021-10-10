# wordcloud
 - 노래를 듣다가 심심해서 노래 가사에 대한 워드 클라우드를 만들어봤습니다.

 - 노래 가사는 [Naver VIBE](https://vibe.naver.com/today) 사이트를 통해 얻었습니다.

## Requirements
 - konlpy 설치해야한다.
    1. JAVA 설치 필요   
      1-1. 버전에 맞는 [자바](https://www.oracle.com/technetwork/java/javase/downloads/index.html) 설치  
      1-2. 환경변수-> 시스템변수에 "JAVA_HOME" 이름으로 자바 경로 입력  
    2. JPype 설치  
      - 파이썬과 자바를 연동하기 위해 [JPype](https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype)가 필요 파이썬 버전에 맞게 설치해야한다. 
      - python 3.9를 사용하고 있기에 JPype1-1.1.2-cp39-cp39-win_amd64.whl를 다운받았다.
      - 다운 받은 후  ``` pip install JPype1-1.1.2-cp39-cp39-win_amd64.whl ```
    3. konlpy 설치
    - ``` pip install konlpy ```

  ```
python3 -m venv (가상환경 이름)
python3 -m pip install -r requirements.txt
  ```

## 실행
  - ``` python3 main.py ```
  - 가수이름:
  - 노래제목: 
  
  

## 결과   
가수이름: 아이유  
노래제목: 스물셋

![IU(twentythree)](/cloud/img/스물셋.PNG)

## 불용어 사이트 참고
https://www.ranks.nl/stopwords/korean
