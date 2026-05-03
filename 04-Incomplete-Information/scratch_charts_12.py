import matplotlib.pyplot as plt
import numpy as np
import os

# Set Chinese font
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False

# Create assets directory
assets_dir = r"c:\Users\26910\OneDrive\Desktop\obsidian\gametheory\Game-Theory-Learning-Repository\04-Incomplete-Information\assets"
os.makedirs(assets_dir, exist_ok=True)

# Chart 1: Screening and Menu Choice
def plot_screening_menu():
    # Model: U = theta * sqrt(q) - t.
    # theta_L = 2, theta_H = 4. Cost C = q.
    q = np.linspace(0, 30, 200)
    
    # Indifference curves for Low type (U=0)
    t_L_0 = 2 * np.sqrt(q)
    # Indifference curves for High type (U = R_H)
    # Let's say optimal qL is 4. Then Rent R_H = (4-2)*sqrt(4) = 4.
    t_H_RH = 4 * np.sqrt(q) - 4
    
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.plot(q, t_L_0, 'r-', label='低类型参与约束 ($U_L=0$)')
    ax.plot(q, t_H_RH, 'b-', label='高类型激励约束 ($U_H=Rent$)')
    
    # Profit curves (iso-profit: t - q = const)
    # Just show the points
    qL, tL = 4, 2*np.sqrt(4)
    qH, tH = 16, 4*np.sqrt(16) - 4
    
    ax.scatter([qL], [tL], color='red', s=100, zorder=5)
    ax.scatter([qH], [tH], color='blue', s=100, zorder=5)
    
    ax.annotate(f'低端套餐\n(向下扭曲)', (qL, tL), xytext=(-60, 20), textcoords='offset points', arrowprops=dict(arrowstyle='->'))
    ax.annotate(f'高端套餐\n(一阶有效)', (qH, tH), xytext=(10, -30), textcoords='offset points', arrowprops=dict(arrowstyle='->'))
    
    ax.set_xlabel("质量 / 容量 $q$", fontsize=12)
    ax.set_ylabel("价格 $t$", fontsize=12)
    ax.set_title("图 1：垄断筛选下的最优菜单设计", fontsize=16)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, '筛选菜单设计图.png'), dpi=300)
    plt.close()

# Chart 2: Revelation Principle Concept
def plot_revelation_principle():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')
    
    # Draw boxes
    rect_params = dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1.5)
    ax.text(0.2, 0.8, "复杂博弈 / 间接机制\n(策略, 谎言, 心理战)", ha="center", va="center", bbox=rect_params)
    ax.text(0.8, 0.8, "直接真实机制\n(激励相容, 说真话)", ha="center", va="center", bbox=rect_params)
    
    ax.annotate("", xy=(0.6, 0.8), xytext=(0.4, 0.8), arrowprops=dict(arrowstyle="<->", lw=2, color='red'))
    ax.text(0.5, 0.85, "显示原理 (等价性)", ha="center", color='red', fontweight='bold')
    
    ax.text(0.5, 0.5, "核心结论：\n如果你能通过复杂机制实现某个目标，\n你一定能设计出一个让大家自愿说真话的简单菜单来实现它。", 
            ha="center", va="center", fontsize=14, bbox=dict(boxstyle="sawtooth", fc="yellow", alpha=0.2))
    
    ax.set_title("图 2：显示原理 (Revelation Principle) 逻辑图", fontsize=16)
    
    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, '显示原理逻辑图.png'), dpi=300)
    plt.close()

# Chart 3: Efficiency vs Rent Tradeoff
def plot_rent_efficiency_tradeoff():
    # Efficiency vs Rent for different qL
    qL = np.linspace(0, 16, 100) # Full efficiency at qL=16 (if thetaL=4, but it's 2)
    # Let's say social surplus = (thetaL*sqrt(qL) - qL) + (thetaH*sqrt(qH) - qH)
    # Rent = (thetaH - thetaL)*sqrt(qL)
    
    surplus = 2 * np.sqrt(qL) - qL
    rent = 2 * np.sqrt(qL)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(qL, surplus, 'g-', lw=2, label='低类型社会剩余 (效率指标)')
    ax.plot(qL, rent, 'r--', lw=2, label='高类型获得的信息租金 (成本指标)')
    
    # Point where derivative matches? dS/dqL = dR/dqL?
    # 1/sqrt(qL) - 1 = 1/sqrt(qL)? No. 
    # Max Profit = Surplus - Rent = (thetaL*sqrt(qL) - qL) - (thetaH - thetaL)*sqrt(qL)
    # = (2*thetaL - thetaH)*sqrt(qL) - qL
    # If thetaL=2, thetaH=4, then Profit = (4-4)*sqrt(qL) - qL = -qL. Max at qL=0.
    # Let's use thetaL=3, thetaH=4. Profit = (6-4)*sqrt(qL) - qL = 2*sqrt(qL) - qL. Max at qL=1.
    
    ax.set_xlabel("低端产品质量 $q_L$", fontsize=12)
    ax.set_ylabel("价值", fontsize=12)
    ax.set_title("图 3：效率扭曲与信息租金的权衡", fontsize=16)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, '效率租金权衡图.png'), dpi=300)
    plt.close()

plot_screening_menu()
plot_revelation_principle()
plot_rent_efficiency_tradeoff()
print("Charts for lecture 12 generated.")
