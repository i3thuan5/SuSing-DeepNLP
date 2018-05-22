# Sû-sìng deepnlp
詞性標記模型


## 愛調整的檔案
```
data/tw.conf
data/tw/train.txt
data/tw/dev.txt
data/tw/test.txt
```

## 訓練kah執行
```
time docker build -t su5-sing3_deepnlp .
time docker run -ti --rm su5-sing3_deepnlp gunicorn -w 2 -b 0.0.0.0:5000 標詞性:app
```
