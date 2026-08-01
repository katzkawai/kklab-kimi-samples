import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "Noto Sans CJK JP"

gni = pd.read_csv("/tmp/japan_gni_yen.csv")
gdp = pd.read_csv("/tmp/japan_gdp_deflator.csv")

nom = gni[gni["indicator"] == "NY.GNP.MKTP.CN"][["date", "value"]].rename(columns={"value": "nom"})
real = gni[gni["indicator"] == "NY.GNP.MKTP.KN"][["date", "value"]].rename(columns={"value": "real"})
gdp_nom = gdp[gdp["indicator"] == "NY.GDP.MKTP.CN"][["date", "value"]].rename(columns={"value": "gdp_nom"})
gdp_real = gdp[gdp["indicator"] == "NY.GDP.MKTP.KN"][["date", "value"]].rename(columns={"value": "gdp_real"})

df = nom.merge(real, on="date", how="outer").merge(gdp_nom, on="date").merge(gdp_real, on="date")
df = df.sort_values("date").reset_index(drop=True)

# GDPデフレーターによる実質GNPの推計(実質GNP = 名目GNP / デフレーター)
df["deflator"] = df["gdp_nom"] / df["gdp_real"]
df["real_est"] = df["nom"] / df["deflator"]

# 1994年の公式値に接続するよう推計値をスプライス(比率調整)
splice = df.loc[df["date"] == 1994, "real"].iloc[0] / df.loc[df["date"] == 1994, "real_est"].iloc[0]
df["real_filled"] = df["real"].fillna(df["real_est"] * splice)
df["estimated"] = df["real"].isna()

est = df[df["estimated"]]
off = df[~df["estimated"]]

fig, ax = plt.subplots(figsize=(11, 6))
ax.plot(df["date"], df["nom"] / 1e12, marker="o", markersize=3,
        linewidth=1.8, color="#1f77b4", label="名目GNP(当年価格、1967–2025)")
ax.plot(off["date"], off["real"] / 1e12, marker="s", markersize=3,
        linewidth=1.8, color="#d62728", label="実質GNP(2015年基準価格、1994–2024)")
# 推計区間は公式系列とつながるよう1994年の点も含めて破線で描く(2025年の推計値は線に含めない)
est_line = pd.concat([est[est["date"] <= 1993], off.head(1)]).sort_values("date")
ax.plot(est_line["date"], est_line["real_filled"] / 1e12, marker="s", markersize=3,
        linewidth=1.8, linestyle="--", color="#ff9896",
        label="実質GNP(GDPデフレーター推計、1967–1993)")

ax.set_title("日本のGNP(GNI)の推移:円建て・名目 vs 実質", fontsize=14)
ax.set_xlabel("年")
ax.set_ylabel("GNP(兆円)")
ax.grid(True, alpha=0.3)
ax.legend()

fig.text(0.99, 0.01, "出所: 世界銀行 WDI (NY.GNP.MKTP.CN / NY.GNP.MKTP.KN、推計は NY.GDP.MKTP.CN/KN より算出)",
         ha="right", fontsize=8, color="gray")

plt.tight_layout()
plt.savefig("/home/katzkawai/kklab-kimi-samples/japan_gnp_yen.png", dpi=150)

out = pd.DataFrame({
    "年": df["date"],
    "名目GNP(兆円)": (df["nom"] / 1e12).round(1),
    "実質GNP(兆円、2015年価格)": (df["real_filled"] / 1e12).round(1),
    "備考": df["estimated"].map({True: "推計", False: ""}),
})
out.to_csv("/home/katzkawai/kklab-kimi-samples/japan_gnp_yen.csv", index=False)
print(out.head(30).to_string(index=False))
print("saved")
