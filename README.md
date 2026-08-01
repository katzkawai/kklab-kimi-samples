# kklab-kimi-samples

日本のGNP(国民総所得 = GNI)の推移を可視化し、GitHub Pagesで公開しているリポジトリです。

- **公開ページ**: https://katzkawai.org/kklab-kimi-samples/
- **データ出所**: 世界銀行 World Development Indicators (WDI)
  - `NY.GNP.MKTP.CD` — GNI(当年価格・米ドル)
  - `NY.GNP.MKTP.CN` — GNI(当年価格・円)
  - `NY.GNP.MKTP.KN` — GNI(2015年基準の実質・円、1994年以降のみ公表)

## ファイル構成

| ファイル | 内容 |
|---|---|
| `index.html` | GitHub Pagesのトップページ(グラフ + データ表) |
| `japan_gnp.png` | ドル建てGNPの推移グラフ(1967–2025年) |
| `japan_gnp_yen.png` | 円建て・名目/実質GNPの推移グラフ |
| `japan_gnp.csv` | ドル建てGNPデータ(年・兆米ドル・米ドル) |
| `japan_gnp_yen.csv` | 円建てGNPデータ(年・名目・実質、兆円) |
| `plot_japan_gnp.py` | ドル建てグラフの描画スクリプト |
| `plot_japan_gnp_yen.py` | 円建てグラフの描画スクリプト |
| `gen_index.py` | CSVから `index.html` を生成するスクリプト |

## 更新方法

1. データ取得(世界銀行API経由)で `/tmp/japan_gni_full.csv` / `/tmp/japan_gni_yen.csv` を更新
2. `python3 plot_japan_gnp.py` / `python3 plot_japan_gnp_yen.py` でグラフ再生成
3. `python3 gen_index.py` で `index.html` 再生成
4. コミットして `main` に push すると GitHub Pages が自動で再デプロイされる

## 更新履歴

### 2026-08-01

- 初回公開
- 世界銀行WDIから日本のGNP(GNI)データ(1967–2025年)を取得
- ドル建て(当年価格)グラフとデータ表を作成・公開
- 円建て・名目/実質グラフとデータ表を追加
- GitHub Pages として公開
