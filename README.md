# 概要
https://www.irisohyama.co.jp/products/storage-furniture/desk-table/table-free-desk/lift-desk
アイリスオーヤマの電動昇降デスクをアルディーノを通して、操作ができるようにしたものリポジトリです。

# 動作原理
LANの中にある電線の特定のところを繋げると、コントローラー信号として伝わります。
https://youtu.be/v3L8fnPKOB8

```
具体的には
緑- 白オレンジ　->下降
白オレンジ-白青 -> 上昇
という流れになっております。
```

アルディーノにコード繋げて特定のピンのポートを開閉させればいいので、シリアル通信で開閉のコントロール信号を受け付けて操作をできるPython Clientを立てて操作を受け付けるという動作をしています。

# 作り方
コントローラーパネルとの接続部がLANポートなので片側の通常のLANのコードを繋げます。
そしたら残ったもう片方のコードをちょんぎって、分解します。
この時ワイヤーストリッパーがあると便利です。
https://youtu.be/Qmh3hsJoz24?si=jKprl0qmrXYxU3rD


# スペシャルサンクス
[@kurimogo](https://x.com/kurimogo): LANコードの分解などを手伝ってもらいました。

# 動作の動画
https://www.youtube.com/watch?v=koPerV_6UWQ

