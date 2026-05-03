import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

# Set Chinese font
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False

# Create assets directory
assets_dir = r"c:\Users\26910\OneDrive\Desktop\obsidian\gametheory\Game-Theory-Learning-Repository\03-Dynamic-Games\assets"
os.makedirs(assets_dir, exist_ok=True)

# Chart 1: Game Tree for Entry Deterrence
def plot_game_tree():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')
    
    # Nodes (x, y)
    E_node = (0.2, 0.5)
    I_node = (0.5, 0.7)
    Out_end = (0.5, 0.3)
    A_end = (0.8, 0.85)
    F_end = (0.8, 0.55)
    
    # Draw edges
    ax.plot([E_node[0], I_node[0]], [E_node[1], I_node[1]], 'k-', lw=2)
    ax.plot([E_node[0], Out_end[0]], [E_node[1], Out_end[1]], 'k-', lw=2)
    ax.plot([I_node[0], A_end[0]], [I_node[1], A_end[1]], 'k-', lw=2)
    ax.plot([I_node[0], F_end[0]], [I_node[1], F_end[1]], 'k--', lw=2, color='red') # Incredible threat
    
    # Draw nodes
    ax.plot(E_node[0], E_node[1], 'ko', markersize=10)
    ax.plot(I_node[0], I_node[1], 'ko', markersize=10)
    ax.plot(Out_end[0], Out_end[1], 'ks', markersize=8)
    ax.plot(A_end[0], A_end[1], 'ks', markersize=8)
    ax.plot(F_end[0], F_end[1], 'ks', markersize=8)
    
    # Add text
    ax.text(E_node[0] - 0.05, E_node[1], "进入者 (E)", fontsize=14, ha='right', va='center')
    ax.text(I_node[0], I_node[1] + 0.05, "在位者 (I)", fontsize=14, ha='center', va='bottom')
    
    ax.text(0.35, 0.65, "进入 (In)", fontsize=12, ha='right', va='bottom')
    ax.text(0.35, 0.35, "不进入 (Out)", fontsize=12, ha='right', va='top')
    
    ax.text(0.65, 0.8, "容纳 (A)", fontsize=12, ha='right', va='bottom')
    ax.text(0.65, 0.6, "打击 (F)", fontsize=12, ha='right', va='top', color='red')
    
    # Payoffs
    ax.text(Out_end[0] + 0.02, Out_end[1], "(0, 3)", fontsize=12, ha='left', va='center')
    ax.text(A_end[0] + 0.02, A_end[1], "(2, 2)\n[逆向归纳均衡]", fontsize=12, ha='left', va='center', color='blue', fontweight='bold')
    ax.text(F_end[0] + 0.02, F_end[1], "(-1, -1)\n[不可信威胁]", fontsize=12, ha='left', va='center', color='red')
    
    plt.title("图 1：进入威慑与逆向归纳博弈树", fontsize=16, pad=20)
    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, '进入威慑与逆向归纳博弈树图.png'), dpi=300, bbox_inches='tight')
    plt.close()

# Chart 2: Commitment Cost Threshold
def plot_commitment_cost():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    C = np.linspace(0, 3, 100)
    # Benefit of deterrence = Payoff(Out) - Payoff(In, A) = 3 - 2 = 1.
    # Net payoff of commitment = 3 - C
    # Payoff without commitment = 2
    
    net_payoff = 3 - C
    no_commitment_payoff = np.full_like(C, 2)
    
    ax.plot(C, net_payoff, 'b-', lw=2, label="承诺后的威慑净收益 $V_I = 3 - C(K)$")
    ax.plot(C, no_commitment_payoff, 'r--', lw=2, label="不承诺的容纳收益 $V_I = 2$")
    
    ax.fill_between(C, net_payoff, no_commitment_payoff, where=(net_payoff >= no_commitment_payoff), alpha=0.3, color='green', label="承诺有效且有利区间")
    ax.fill_between(C, net_payoff, no_commitment_payoff, where=(net_payoff < no_commitment_payoff), alpha=0.3, color='gray', label="承诺无效或不划算区间")
    
    ax.set_xlabel("承诺成本 $C(K)$", fontsize=14)
    ax.set_ylabel("在位者均衡收益 $V_I$", fontsize=14)
    ax.axvline(x=1, color='k', linestyle=':', lw=1.5)
    ax.text(1.05, 1.5, "临界成本 $C^* = 1$", fontsize=12, rotation=90)
    
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3.5)
    ax.legend(fontsize=12, loc='upper right')
    ax.grid(True, alpha=0.3)
    
    plt.title("图 2：承诺成本与威慑有效性的比较静态分析", fontsize=16, pad=20)
    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, '承诺成本比较静态图.png'), dpi=300, bbox_inches='tight')
    plt.close()

plot_game_tree()
plot_commitment_cost()
print("Charts generated successfully.")
