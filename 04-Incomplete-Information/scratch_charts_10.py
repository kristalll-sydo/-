# -*- coding: utf-8 -*-
"""
脚本: scratch_charts_10.py
功能: 为《不完全信息与贝叶斯博弈》 (讲义10) 生成三张学术图表，采用 Nano Banana Pro 风格（柔和渐变、光晕、中文标签）。
所有图表保存至仓库根目录下的 `10-Assets/`，文件名使用中文。
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# ---------- Nano Banana Pro 主题设置 ----------
def set_nano_banana_style():
    """配置 Matplotlib 为 Nano Banana Pro 风格。"""
    # 背景渐变颜色（深蓝 → 靛蓝）
    plt.rcParams.update({
        "figure.facecolor": "#1a1a2e",
        "axes.facecolor": "#16213e",
        "axes.edgecolor": "#ffffff",
        "axes.labelcolor": "#ffffff",
        "xtick.color": "#dddddd",
        "ytick.color": "#dddddd",
        "text.color": "#ffffff",
        "grid.color": "#444455",
        "grid.linestyle": "--",
        "grid.alpha": 0.3,
        "font.size": 12,
        "font.family": "sans-serif",
        "font.sans-serif": ["Microsoft YaHei", "Arial", "Helvetica"],
    })
    # 使用轻微透明的光晕效果
    rcParams["lines.linewidth"] = 2.5
    rcParams["lines.solid_capstyle"] = "round"

# ---------- 图表 1: 贝叶斯古诺竞争均衡 ----------
def plot_bayesian_cournot():
    set_nano_banana_style()
    # 参数示例
    alpha = 10  # 市场需求截距
    cL, cH = 2, 5  # 两种成本类型（低/高）
    # 期望成本
    p_low = 0.6
    c_exp = p_low * cL + (1 - p_low) * cH
    # 反应函数（线性）
    q = np.linspace(0, 5, 200)
    # Player 2 低成本反应
    r2_low = (alpha - cL - q) / 2
    # Player 2 高成本反应
    r2_high = (alpha - cH - q) / 2
    # Player 1 期望反应（面对成本分布）
    r1 = (alpha - c_exp - q) / 2
    plt.figure(figsize=(6,6))
    plt.plot(q, r2_low, "g--", label="玩家2（低成本）")
    plt.plot(q, r2_high, "r--", label="玩家2（高成本）")
    plt.plot(q, r1, "b-", label="玩家1（期望）")
    # 坐标轴
    plt.xlabel("玩家1 产量 q₁")
    plt.ylabel("玩家2 产量 q₂")
    plt.title("贝叶斯古诺竞争均衡", fontsize=14, fontweight="bold")
    plt.grid(True, which="both", linestyle="--", alpha=0.3)
    plt.legend(loc="upper right")
    # 保存
    out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "10-Assets"))
    os.makedirs(out_dir, exist_ok=True)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "讲义10贝叶斯古诺均衡图.png"), dpi=300, transparent=False)
    plt.close()

# ---------- 图表 2: 拍卖出价策略 ----------
def plot_auction_bids():
    set_nano_banana_style()
    # 假设第一价格密封拍卖，买家估值服从均匀分布 [0, V]
    V = 10
    v = np.linspace(0, V, 200)
    # 风险中性买家最优投标函数 b(v) = (n-1)/n * v，取 n=3
    n = 3
    b = (n-1)/n * v
    plt.figure(figsize=(6,4))
    plt.plot(v, b, "#ff7f0e", label="最优投标函数 b(v)")
    plt.plot([0, V], [0, V], "#888888", linestyle="--")
    plt.xlabel("估值 v")
    plt.ylabel("投标 b(v)")
    plt.title("密封第一价格拍卖投标策略", fontsize=14, fontweight="bold")
    plt.grid(True, alpha=0.3)
    plt.legend()
    out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "10-Assets"))
    os.makedirs(out_dir, exist_ok=True)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "讲义10拍卖出价策略图.png"), dpi=300)
    plt.close()

# ---------- 图表 3: 信念决策边界 ----------
def plot_belief_threshold():
    set_nano_banana_style()
    # 参数示例：先验信念 p ∈ [0,1]
    p = np.linspace(0, 1, 200)
    # 当 p > p* 时玩家选择合作行动 C，否则选择背叛 D
    # 假设阈值 p* = 0.4（由模型推导得）
    p_star = 0.4
    action = np.where(p > p_star, 1, 0)  # 1=合作, 0=背叛
    plt.figure(figsize=(6,4))
    plt.plot(p, action, "m-", label="最优行动")
    plt.axvline(p_star, color="#ff0000", linestyle="--", label="阈值 p*")
    plt.ylim(-0.1, 1.1)
    plt.xlabel("先验信念 p")
    plt.ylabel("最优行动（1=合作，0=背叛）")
    plt.title("信念决策阈值图", fontsize=14, fontweight="bold")
    plt.grid(True, alpha=0.3)
    plt.legend()
    out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "10-Assets"))
    os.makedirs(out_dir, exist_ok=True)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "讲义10信念决策边界图.png"), dpi=300)
    plt.close()

# ---------- 主函数 ----------
if __name__ == "__main__":
    plot_bayesian_cournot()
    plot_auction_bids()
    plot_belief_threshold()
    print("Lecture 10 charts generated and saved to 10-Assets directory.")
