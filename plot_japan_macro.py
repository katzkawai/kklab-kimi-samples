import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "Noto Sans CJK JP"

fx = pd.read_csv("/tmp/japan_fx.csv").sort_values("date")
tot = pd.read_csv("/tmp/japan_tot.csv").sort_values("date")
cpi = pd.read_csv("/tmp/japan_cpi.csv").sort_values("date")

fig, axes = plt.subplots(3, 1, figsize=(11, 10), sharex=True)

axes[0].plot(fx["date"], fx["value"], marker="o", markersize=3, linewidth=1.8, color="#1f77b4")
axes[0].set_ylabel("円/ドル")
axes[0].set_title("為替レート(円/ドル、期間平均)")
axes[0].axhline(100, color="gray", linewidth=0.8, linestyle=":")
axes[0].annotate("上に行くほど円安", xy=(1968, 270), fontsize=9, color="gray")

axes[1].plot(tot["date"], tot["value"], marker="s", markersize=3, linewidth=1.8, color="#d62728")
axes[1].axhline(100, color="gray", linewidth=0.8, linestyle=":")
axes[1].set_ylabel("指数(2015年=100)")
axes[1].set_title("交易条件指数(純物物交易条件、2015年=100)")

axes[2].plot(cpi["date"], cpi["value"], marker="^", markersize=3, linewidth=1.8, color="#2ca02c")
axes[2].axhline(0, color="gray", linewidth=0.8, linestyle=":")
axes[2].axhline(2, color="gray", linewidth=0.8, linestyle="--")
axes[2].set_ylabel("%(前年比)")
axes[2].set_title("消費者物価上昇率(前年比%)")
axes[2].set_xlabel("年")

for ax in axes:
    ax.grid(True, alpha=0.3)

fig.suptitle("円安の影響の裏付け系列:日本(1967–2025年)", fontsize=14)
fig.text(0.99, 0.005, "出所: 世界銀行 WDI (PA.NUS.FCRF / TT.PRI.MRCH.XD.WD / FP.CPI.TOTL.ZG)",
         ha="right", fontsize=8, color="gray")

plt.tight_layout(rect=[0, 0.02, 1, 0.98])
plt.savefig("/home/katzkawai/kklab-kimi-samples/japan_macro.png", dpi=150)

out = pd.DataFrame({"年": fx["date"], "為替レート(円/ドル)": fx["value"].round(1)})
out = out.merge(
    pd.DataFrame({"年": tot["date"], "交易条件指数(2015=100)": tot["value"].round(1)}),
    on="年", how="outer")
out = out.merge(
    pd.DataFrame({"年": cpi["date"], "消費者物価上昇率(%)": cpi["value"].round(2)}),
    on="年", how="outer").sort_values("年")
out.to_csv("/home/katzkawai/kklab-kimi-samples/japan_macro.csv", index=False)
print("saved")
