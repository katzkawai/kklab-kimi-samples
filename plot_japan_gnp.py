import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "Noto Sans CJK JP"

df = pd.read_csv("/tmp/japan_gni_full.csv")
df = df.sort_values("date")

fig, ax = plt.subplots(figsize=(11, 6))
ax.plot(df["date"], df["value"] / 1e12, marker="o", markersize=3,
        linewidth=1.8, color="#1f77b4")
ax.fill_between(df["date"], df["value"] / 1e12, alpha=0.15, color="#1f77b4")

ax.set_title("日本のGNP(GNI)の推移(1967–2025年)", fontsize=14)
ax.set_xlabel("年")
ax.set_ylabel("GNP(兆米ドル、当年価格)")
ax.grid(True, alpha=0.3)
ax.set_xlim(df["date"].min(), df["date"].max())

fig.text(0.99, 0.01, "出所: 世界銀行 World Development Indicators (NY.GNP.MKTP.CD)",
         ha="right", fontsize=8, color="gray")

plt.tight_layout()
plt.savefig("/home/katzkawai/kklab-kimi-samples/japan_gnp.png", dpi=150)
print("saved")
