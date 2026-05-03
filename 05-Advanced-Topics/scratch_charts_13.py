import matplotlib.pyplot as plt
import numpy as np
import os

# Set Chinese font
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False

# Create assets directory
assets_dir = r"c:\Users\26910\OneDrive\Desktop\obsidian\gametheory\Game-Theory-Learning-Repository\05-Advanced-Topics\assets"
os.makedirs(assets_dir, exist_ok=True)

# Chart 1: Hawk-Dove Payoffs
def plot_hawk_dove_payoffs():
    V = 4
    C = 10
    x = np.linspace(0, 1, 100)
    
    # f_H(x) = x * (V-C)/2 + (1-x) * V
    # f_D(x) = x * 0 + (1-x) * V/2
    f_H = x * (V - C) / 2 + (1 - x) * V
    f_D = (1 - x) * V / 2
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, f_H, 'b-', lw=2, label='鹰策略的适应度 $f_H(x)$')
    ax.plot(x, f_D, 'r-', lw=2, label='鸽策略的适应度 $f_D(x)$')
    
    # Equilibrium x* = V/C
    x_star = V / C
    ax.axvline(x_star, color='gray', linestyle='--', alpha=0.7)
    ax.plot(x_star, (1-x_star)*V/2, 'ko')
    ax.text(x_star + 0.02, 0.5, f'稳定均衡 $x^* = V/C = {x_star}$', fontsize=12)
    
    ax.set_xlabel('鹰策略在群体中的比例 $x$', fontsize=12)
    ax.set_ylabel('适应度 (Fitness)', fontsize=12)
    ax.set_title(f'图 1：鹰鸽博弈中的适应度函数 ($V={V}, C={C}$)', fontsize=16)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, '鹰鸽博弈适应度对比图.png'), dpi=300)
    plt.close()

# Chart 2: Replicator Dynamics Trajectory
def plot_replicator_dynamics():
    V = 4
    C = 10
    x_star = V / C
    
    def dx(x):
        f_H = x * (V - C) / 2 + (1 - x) * V
        f_D = (1 - x) * V / 2
        f_avg = x * f_H + (1 - x) * f_D
        return x * (f_H - f_avg)
    
    x_vals = np.linspace(0, 1, 20)
    v_vals = [dx(x) for x in x_vals]
    
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.quiver(x_vals, np.zeros_like(x_vals), v_vals, np.zeros_like(x_vals), 
              angles='xy', scale_units='xy', scale=1, color='teal', alpha=0.6)
    
    ax.plot([0, 1], [0, 0], 'k-', alpha=0.3)
    ax.plot(x_star, 0, 'ro', markersize=10, label=f'ESS (x={x_star})')
    ax.plot(0, 0, 'go', markersize=8, alpha=0.5)
    ax.plot(1, 0, 'go', markersize=8, alpha=0.5)
    
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.1, 0.1)
    ax.set_yticks([])
    ax.set_xlabel('群体中鹰策略比例 $x$', fontsize=12)
    ax.set_title('图 2：鹰鸽博弈的复制动态相图 ($\dot{x}$ 方向)', fontsize=16)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, '复制动态相图.png'), dpi=300)
    plt.close()

# Chart 3: Altruism vs Selfishness (Clustering Effect)
def plot_altruism_clustering():
    labels = ['混合随机 (Random Mixing)', '聚簇居住 (Clustering)']
    selfish_payoffs = [15, 0] # Example values
    altruist_payoffs = [5, 10]
    
    x = np.arange(len(labels))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width/2, selfish_payoffs, width, label='自私型 (Selfish)', color='gray')
    rects2 = ax.bar(x + width/2, altruist_payoffs, width, label='利他型 (Altruist)', color='gold')
    
    ax.set_ylabel('平均收益 / 适应度', fontsize=12)
    ax.set_title('图 3：社会结构对利他主义演化的影响', fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    
    # Add a horizontal line to show survival threshold
    ax.axhline(0, color='black', lw=1)
    
    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, '利他主义演化结构影响图.png'), dpi=300)
    plt.close()

plot_hawk_dove_payoffs()
plot_replicator_dynamics()
plot_altruism_clustering()
print("Charts for lecture 13 generated successfully.")
