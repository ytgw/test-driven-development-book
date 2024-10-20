# テスト駆動開発
テスト駆動開発の本の写経


## 第1部 多国通貨

### テスト方法
コマンドラインでのテスト実行は以下で行う。
```bash
cd part1
gradle test  # 初回のみ数秒かかる
```

### TODOリスト
- $5 + 10 CHF = $10 (レートが2:1の場合)
- ~~$5 * 2 = $10~~
- ~~amountをprivateにする~~
- ~~Dollarの副作用をどうする?~~
- Moneyの丸め処理どうする?
- ~~equals()~~
- hashCode()
- nullとの等価性比較
- 他のオブジェクトとの等価性比較
- ~~5CHF * 2 = 10CHF~~
- DollarとFrancの重複
- ~~equalsの一般化~~
- timesの一般化
- ~~FrancとDollarを比較する~~
- ~~通貨の概念~~
- testFrancMultiplicationを削除する?
