import matplotlib.pyplot as plt
import numpy as np
import os

# Set Chinese font
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False

# Create assets directory
assets_dir = r"c:\Users\26910\OneDrive\Desktop\obsidian\gametheory\Game-Theory-Learning-Repository\03-Dynamic-Games\assets"
os.makedirs(assets_dir, exist_ok=True)

# Chart 1: Folk Theorem Feasible Region
def plot_folk_theorem():
    # Prisoner's Dilemma points: (3,3), (0,5), (5,0), (1,1)
    points = np.array([[3,3], [0,5], [1,1], [5,0], [3,3]])
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Fill feasible region (convex hull)
    ax.fill(points[:,0], points[:,1], color='lightgray', alpha=0.3, label='可行支付集合 $V$')
    
    # Minmax point (1,1)
    ax.axvline(x=1, color='red', linestyle='--', alpha=0.5)
    ax.axhline(y=1, color='red', linestyle='--', alpha=0.5)
    
    # Individually rational region
    rational_poly = np.array([[1,1], [1,4], [4,1], [1,1]]) # simplified
    # Correct individually rational is the subset of V where payoffs >= (1,1)
    ax.fill_between([1, 4], [4, 1], 5, where=([1, 4] >= np.array([1, 1])), color='blue', alpha=0.2, label='无名氏定理可支撑均衡区')
    
    ax.plot(points[:,0], points[:,1], 'ko--')
    ax.scatter([3, 0, 5, 1], [3, 5, 0, 1], color='black', zorder=5)
    
    ax.text(3.1, 3.1, "合作 (3,3)", fontsize=10)
    ax.text(0.1, 5.1, "背叛诱惑 (0,5)", fontsize=10)
    ax.text(5.1, 0.1, "被背叛 (5,0)", fontsize=10)
    ax.text(1.1, 1.1, "博弈原点 (1,1)", fontsize=10, color='red')
    
    ax.set_xlabel("玩家 1 的平均收益", fontsize=12)
    ax.set_ylabel("玩家 2 的平均收益", fontsize=12)
    ax.set_title("图 1：无名氏定理与可行支付空间", fontsize=16)
    ax.legend()
    ax.grid(True, alpha=0.2)
    
    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, '无名氏定理可行区域图.png'), dpi=300)
    plt.close()

# Chart 2: Cooperation Boundary (delta vs T)
def plot_cooperation_boundary():
    R, P = 3, 1
    T = np.linspace(3.1, 8, 100)
    delta_min = (T - R) / (T - P)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(T, delta_min, 'b-', lw=2, label='合作临界线 $\delta^*$')
    ax.fill_between(T, delta_min, 1, color='green', alpha=0.2, label='合作区')
    ax.fill_between(T, 0, delta_min, color='red', alpha=0.1, label='背叛区')
    
    ax.set_xlabel("背叛诱惑收益 $T$", fontsize=12)
    ax.set_ylabel("最低折现因子 $\delta$", fontsize=12)
    ax.set_title("图 2：诱惑程度对合作稳定性的冲击", fontsize=16)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, '重复博弈合作边界图.png'), dpi=300)
    plt.close()

# Chart 3: Tit-for-Tat vs Always Defect
def plot_tft_vs_all_d():
    rounds = 20
    # Payoffs: R=3, T=5, S=0, P=1
    
    # TFT vs TFT (All Coop)
    coop_payoff = np.cumsum([3]*rounds)
    
    # AllD vs AllD (All Defect)
    defect_payoff = np.cumsum([1]*rounds)
    
    # AllD vs TFT
    # R1: AllD(5), TFT(0)
    # R2: AllD(1), TFT(1) ...
    alld_vs_tft = np.zeros(rounds)
    tft_vs_alld = np.zeros(rounds)
    alld_vs_tft[0] = 5
    tft_vs_alld[0] = 0
    alld_vs_tft[1:] = 1
    tft_vs_alld[1:] = 1
    alld_cum = np.cumsum(alld_vs_tft)
    tft_cum = np.cumsum(tft_vs_alld)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(np.arange(1, rounds+1), coop_payoff, 'g-o', label='长期合作 (TFT vs TFT)')
    ax.plot(np.arange(1, rounds+1), defect_payoff, 'r-s', label='长期背叛 (AllD vs AllD)')
    ax.plot(np.arange(1, rounds+1), alld_cum, 'y--^', label='短期投机 (AllD vs TFT)')
    
    ax.set_xlabel("博弈轮次", fontsize=12)
    ax.set_ylabel("累计收益", fontsize=12)
    ax.set_title("图 3：策略演化的长期收益比较", fontsize=16)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, '重复博弈策略收益演化图.png'), dpi=300)
    plt.close()

plot_folk_theorem()
plot_cooperation_boundary()
plot_tft_vs_all_d()
print("Charts for lecture 09 generated.")
