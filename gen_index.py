import pandas as pd

usd = pd.read_csv("japan_gnp.csv")
yen = pd.read_csv("japan_gnp_yen.csv")

def table_html(df):
    rows = "\n".join(
        "<tr>" + "".join(
            f"<td>{'' if pd.isna(v) else (int(v) if isinstance(v, float) and v == int(v) else v)}</td>"
            for v in row
        ) + "</tr>"
        for row in df.itertuples(index=False)
    )
    head = "".join(f"<th>{c}</th>" for c in df.columns)
    return f"<table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>"

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>日本のGNP(GNI)の推移</title>
<style>
  body {{ font-family: "Hiragino Sans", "Noto Sans CJK JP", sans-serif;
         max-width: 960px; margin: 2rem auto; padding: 0 1rem; color: #222; }}
  h1 {{ font-size: 1.5rem; border-bottom: 2px solid #1f77b4; padding-bottom: .4rem; }}
  h2 {{ font-size: 1.15rem; margin-top: 2.5rem; }}
  img {{ max-width: 100%; border: 1px solid #ddd; border-radius: 4px; }}
  table {{ border-collapse: collapse; font-size: .85rem; margin-top: 1rem; }}
  th, td {{ border: 1px solid #ccc; padding: .3rem .8rem; text-align: right; }}
  th {{ background: #f0f4f8; }}
  tr:nth-child(even) {{ background: #fafafa; }}
  .table-wrap {{ max-height: 480px; overflow-y: auto; }}
  .note {{ color: #666; font-size: .8rem; }}
</style>
</head>
<body>
<h1>日本のGNP(GNI)の推移(1967–2025年)</h1>
<p>世界銀行 World Development Indicators のデータに基づく、日本のGNP(国民総所得 = GNI)の推移です。</p>

<h2>ドル建て(当年価格)</h2>
<img src="japan_gnp.png" alt="日本のGNP(ドル建て)の推移">
<div class="table-wrap">{table_html(usd)}</div>
<p class="note">出所: 世界銀行 WDI (NY.GNP.MKTP.CD) / <a href="japan_gnp.csv">CSVをダウンロード</a></p>

<h2>円建て(名目・実質)</h2>
<img src="japan_gnp_yen.png" alt="日本のGNP(円建て・名目 vs 実質)の推移">
<div class="table-wrap">{table_html(yen)}</div>
<p class="note">出所: 世界銀行 WDI (NY.GNP.MKTP.CN / NY.GNP.MKTP.KN)。実質は2015年基準価格 / <a href="japan_gnp_yen.csv">CSVをダウンロード</a></p>

<p class="note">AI生成コンテンツを含みます。投資助言ではありません。</p>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("index.html written")
