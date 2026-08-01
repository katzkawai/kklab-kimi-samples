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
  h3 {{ font-size: 1rem; margin-top: 1.5rem; }}
  ul {{ line-height: 1.7; font-size: .92rem; }}
  li {{ margin-bottom: .4rem; }}
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
<p class="note">出所: 世界銀行 WDI (NY.GNP.MKTP.CN / NY.GNP.MKTP.KN)。実質は2015年基準価格。1967–1993年と2025年の実質はGDPデフレーター(NY.GDP.MKTP.CN/KN)による推計値(備考列に「推計」と記載) / <a href="japan_gnp_yen.csv">CSVをダウンロード</a></p>

<h2>考察</h2>
<ul>
<li><strong>ドル建てでは為替の影響が大きい</strong>: 1967年の約0.13兆ドルから円高を背景に急拡大し、2012年に過去最高の約6.5兆ドルを記録。近年は円安でドル換算が縮小し、2024年は約4.4兆ドル。ドル建ての増減は経済規模そのものより為替レートの変動を強く反映する</li>
<li><strong>近年のドル建てGNP減少はほぼ円安が原因</strong>: 2012年→2024年にドル建てGNPは6.51兆→4.45兆ドルと約32%減少したが、同期間の円建て名目GNPは519兆→673兆円と約30%増加している。乖離の正体は為替で、データから算出した換算レートは80円/ドル(2012年)→151円/ドル(2024年)と約90%円安に振れた。背景には、2022年以降の米FRBの急激な利上げと日本銀行の金融緩和継続による日米金利差の拡大がある。円建てで経済が縮小したわけではないため、ドル建て系列だけで日本経済の実力を評価するのは誤解を招く。なお、この為替要因により2023年にはドル建て名目GDPで日本はドイツに抜かれ、世界4位に後退した(IMFベース)</li>
<li><strong>円建て名目では一貫して増加</strong>: 2025年には約706兆円に達し、ドル建てで見えた近年の「縮小」は為替(円安)によるものだったことがわかる</li>
<li><strong>実質成長は1990年代半ば以降に鈍化</strong>: 推計値では高度成長期に実質GNPは1967年の約150兆円から1990年の約470兆円へ約3倍に拡大。一方、1994年の約491兆円から2024年の約608兆円までの30年間は約1.24倍(年率0.7%程度)にとどまり、「失われた30年」の停滞が確認できる</li>
<li><strong>2020年の落ち込みと回復</strong>: コロナ禍で名目・実質ともに2020年に低下し、その後回復</li>
<li><strong>2022年以降は名目の伸びが実質を大きく上回る</strong>: GDPデフレーターの上昇(インフレ)の定着を反映している</li>
</ul>

<h3>円安が日本経済に与える影響</h3>
<p>近年のドル建てGNP減少の主因である円安は、日本経済にプラスとマイナスの両面の影響を与えている。</p>
<ul>
<li><strong>プラス面</strong>: 輸出産業の収益改善(ドル建て売上・海外子会社利益の円換算増)。海外からの所得収支の拡大(日本は対外純資産世界最大級であり、名目GNPが2022年の約620兆円から2025年の約706兆円へ大きく伸びた一因)。インバウンド需要の拡大。名目成長・税収の押し上げ</li>
<li><strong>マイナス面</strong>: 輸入物価上昇によるコストプッシュ型インフレと実質賃金の低下(2022年以降の名目・実質乖離の正体)。交易条件の悪化による実質所得の海外流出。国内生産回帰が限定的な場合の産業空洞化リスク。ドル建てでの対外的な経済プレゼンスの低下(1人当たり所得の順位低下など)</li>
<li><strong>総合すると</strong>: 受益(輸出・海外展開企業、海外資産保有者)と負担(家計)の分布が大きく偏った構造になっている。日本銀行は2024年にマイナス金利を解除するなど金融政策の正常化を進めており、今後の為替水準と金利差の動向がこの構図を左右する</li>
</ul>
<p class="note">※ この考察は本ページのデータ系列(GNPの水準・名目/実質の乖離)と整合的ですが、実質賃金や交易条件そのものの系列は別データの確認が前提の一般的な経済分析です。必要なら世界銀行やIMFのデータでこれらの裏付け系列も取得してグラフ化できます。</p>

<p class="note">AI生成コンテンツを含みます。投資助言ではありません。</p>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("index.html written")
