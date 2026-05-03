import matplotlib.pyplot as plt
import numpy as np
import os

# Set Chinese font
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False

# Create assets directory
assets_dir = r"c:\Users\26910\OneDrive\Desktop\obsidian\gametheory\Game-Theory-Learning-Repository\04-Incomplete-Information\assets"
os.makedirs(assets_dir, exist_ok=True)

# Chart 1: Spence Signaling - Single Crossing Condition
def plot_spence_signaling():
    # Wage = 100 if e >= e*, else 50
    # Utility = Wage - Cost(e, type)
    # Cost_L = e^2 / 40, Cost_H = e^2 / 100 (H cost is lower)
    
    e = np.linspace(0, 80, 200)
    
    # Indifference curves for Wage = 100
    # 100 - e^2/k = U_target -> e = sqrt(k*(100-U_target))
    # Let's just plot the cost functions to show single crossing
    cost_l = e**2 / 40
    cost_h = e**2 / 100
    
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(e, cost_l, 'r-', lw=2, label='低能力者成本 $c_L(e)$')
    ax.plot(e, cost_h, 'b-', lw=2, label='高能力者成本 $c_H(e)$')
    
    # Wage differential Delta_W = 50
    ax.axhline(y=50, color='gray', linestyle='--', alpha=0.5, label='工资溢价 $\Delta W$')
    
    # Critical e* points
    # For L: e^2/40 = 50 -> e = sqrt(2000) approx 44.7
    # For H: e^2/100 = 50 -> e = sqrt(5000) approx 70.7
    e_star_min = np.sqrt(2000)
    e_star_max = np.sqrt(5000)
    
    ax.fill_between(e, 0, 100, where=(e >= e_star_min) & (e <= e_star_max), color='green', alpha=0.1, label='分离均衡区间')
    
    ax.scatter([e_star_min], [50], color='red', zorder=5)
    ax.scatter([e_star_max], [50], color='blue', zorder=5)
    
    ax.annotate('低能力者临界点', (e_star_min, 50), xytext=(-80, 20), textcoords='offset points', arrowprops=dict(arrowstyle='->'))
    ax.annotate('高能力者临界点', (e_star_max, 50), xytext=(10, 20), textcoords='offset points', arrowprops=dict(arrowstyle='->'))
    
    ax.set_xlabel("教育水平 $e$", fontsize=12)
    ax.set_ylabel("成本 / 效用损失", fontsize=12)
    ax.set_title("图 1：斯宾塞信号模型与单交点条件", fontsize=16)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, '信号传递单交点图.png'), dpi=300)
    plt.close()

# Chart 2: Adverse Selection - Market Collapse (Lemon Market)
def plot_lemon_market():
    # Quality q uniform in [0, 100]
    # Seller value = q. Buyer value = 1.5 * q.
    # But buyer only sees average quality of cars put on market.
    # If price is P, sellers with q <= P will sell.
    # Average quality E[q | q <= P] = P/2.
    # Buyers' WTP = 1.5 * (P/2) = 0.75P.
    # Since 0.75P < P, no one buys at price P > 0.
    
    p = np.linspace(0, 100, 100)
    wtp = 0.75 * p
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(p, p, 'r--', label='卖家的要价 (保底价值)')
    ax.plot(p, wtp, 'b-', lw=2, label='买家的最高出价 (基于平均质量)')
    
    ax.fill_between(p, wtp, p, color='red', alpha=0.1, label='市场无法成交区')
    
    ax.set_xlabel("市场价格 $P$", fontsize=12)
    ax.set_ylabel("价值评估", fontsize=12)
    ax.set_title("图 2：柠檬市场中的价格-质量负反馈", fontsize=16)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, '柠檬市场崩塌示意图.png'), dpi=300)
    plt.close()

# Chart 3: Payoff Comparison
def plot_equilibrium_comparison():
    labels = ['完全信息', '分离均衡', '混同均衡', '市场崩塌']
    # Total Welfare (Conceptual values)
    welfare = [100, 85, 70, 0] 
    
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['#2ecc71', '#3498db', '#f1c40f', '#e74c3c']
    bars = ax.bar(labels, welfare, color=colors, alpha=0.8)
    
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval}%', ha='center', va='bottom')
        
    ax.set_ylabel("社会总福利水平 (%)", fontsize=12)
    ax.set_title("图 3：不同信息结构下的社会效率比较", fontsize=16)
    ax.set_ylim(0, 115)
    
    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, '信号均衡效率对比图.png'), dpi=300)
    plt.close()

plot_spence_signaling()
plot_lemon_market()
plot_equilibrium_comparison()
print("Charts for lecture 11 generated.")
