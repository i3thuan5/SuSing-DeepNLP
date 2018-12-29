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
time docker run -e VIRTUAL_HOST=xn--s-sng-vsa6h.xn--v0qr21b.xn--kpry57d -e VIRTUAL_PORT=5000 --expose=5000 --rm su5-sing3_deepnlp
```

