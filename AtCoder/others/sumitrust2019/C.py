X = int(input())
# とりあえず 100 で構成しようとして、余剰分を 100 を置換することで構成できないか調べる
q, r = X//100, X%100
if r <= 5 * q:
    print(1)
else:
    print(0)
