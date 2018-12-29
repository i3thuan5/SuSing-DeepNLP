# Sû-sìng deepnlp
詞性標記模型


## 愛調整的檔案
```
data/tw.conf
data/tw/train.txt
data/tw/dev.txt
data/tw/test.txt
```

## 用便的模型
```
time docker run --name taigi_susing -d \
  --network nginx-bridge -e VIRTUAL_HOST=xn--s-sng-vsa6h.xn--v0qr21b.xn--kpry57d -e VIRTUAL_PORT=5000 --expose=5000 \
  i3thuan5/taigi_susing \
  gunicorn -w 2 -b 0.0.0.0:5000 --log-level debug 標詞性:app
```

## 訓練kah執行
```
time docker build -t su5-sing3_deepnlp .
time docker run -e VIRTUAL_HOST=xn--s-sng-vsa6h.xn--v0qr21b.xn--kpry57d -e VIRTUAL_PORT=5000 --expose=5000 --rm su5-sing3_deepnlp
```

