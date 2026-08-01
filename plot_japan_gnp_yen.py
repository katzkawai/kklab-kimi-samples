import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "Noto Sans CJK JP"

df = pd.read_csv("/tmp/japan_gni_yen.csv")
nom = df[df["indicator"] == "NY.GNP.MKTP.CN"].sort_values("date")
real = df[df["indicator"] == "NY.GNP.MKTP.KN"].sort_values("date")

fig, ax = plt.subplots(figsize=(11, 6))
ax.plot(nom["date"], nom["value"] / 1e12, marker="o", markersize=3,
        linewidth=1.8, color="#1f77b4", label="名目GNP(当年価格、1967–2025)")
ax.plot(real["date"], real["value"] / 1e12, marker="s", markersize=3,
        linewidth=1.8, color="#d62728", label="実質GNP(2015年基準価格、1994–2024)")

ax.set_title("日本のGNP(GNI)の推移:円建て・名目 vs 実質", fontsize=14)
ax.set_xlabel("年")
ax.set_ylabel("GNP(兆円)")
ax.grid(True, alpha=0.3)
ax.legend()

fig.text(0.99, 0.01, "出所: 世界銀行 WDI (NY.GNP.MKTP.CN / NY.GNP.MKTP.KN)",
         ha="right", fontsize=8, color="gray")

plt.tight_layout()
plt.savefig("/home/katzkawai/kklab-kimi-samples/japan_gnp_yen.png", dpi=150)

nom_out = pd.DataFrame({"年": nom["date"], "名目GNP(兆円)": (nom["value"] / 1e12).round(1)})
real_out = pd.DataFrame({"年": real["date"], "実質GNP(兆円、2015年価格)": (real["value"] / 1e12).round(1)})
merged = pd.merge(nom_out, real_out, on="年", how="outer").sort_values("年")
merged.to_csv("/home/katzkawai/kklab-kimi-samples/japan_gnp_yen.csv", index=False)
print("saved")
