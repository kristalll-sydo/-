import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

# Set style for "Nano banana pro" - clean, professional, academic
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Inter", "Roboto", "Arial"],
    "axes.edgecolor": "#333333",
    "axes.labelcolor": "#333333",
    "xtick.color": "#333333",
    "ytick.color": "#333333",
    "text.color": "#333333",
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "legend.fontsize": 10,
    "figure.figsize": (8, 5),
    "figure.dpi": 300,
    "savefig.bbox": 'tight',
})

# Path for assets
assets_dir = r"c:\Users\26910\OneDrive\Desktop\obsidian\gametheory\Game-Theory-Learning-Repository\10-Assets\lecture_figures"
os.makedirs(assets_dir, exist_ok=True)

def save_fig(name):
    path = os.path.join(assets_dir, f"{name}.png")
    plt.savefig(path, transparent=False, facecolor='white')
    print(f"Saved {name}")
    plt.close()

# Chart 1: Rubinstein Bargaining Model - Payoffs over time
def plot_rubinstein_bargaining():
    delta = 0.8
    rounds = np.arange(1, 11)
    
    # Values at equilibrium
    v1 = 1 / (1 + delta)
    v2 = delta / (1 + delta)
    
    fig, ax = plt.subplots()
    
    # Total pie shrinking
    pie = delta**(rounds-1)
    # A's offer if A proposes: x = v1 * pie
    # B's offer if B proposes: y = v2 * pie (from B's perspective)
    
    p1_vals = []
    p2_vals = []
    for r in rounds:
        if r % 2 != 0: # A proposes
            p1_vals.append(v1 * delta**(r-1))
            p2_vals.append((1-v1) * delta**(r-1))
        else: # B proposes
            p1_vals.append((1-v1) * delta**(r-1))
            p2_vals.append(v1 * delta**(r-1))
            
    ax.fill_between(rounds, pie, color='#F1FAEE', alpha=0.5, label='Total Surplus (Discounted)')
    ax.plot(rounds, p1_vals, marker='o', color='#E76F51', lw=2, label='Player A Payoff (Equilibrium)')
    ax.plot(rounds, p2_vals, marker='s', color='#264653', lw=2, label='Player B Payoff (Equilibrium)')
    
    ax.set_xlabel("Bargaining Round (t)")
    ax.set_ylabel("Present Value of Payoff")
    ax.set_title("Equilibrium Payoff Evolution in Rubinstein Model", fontweight='bold')
    ax.legend()
    ax.set_xticks(rounds)
    sns.despine()
    save_fig("lecture08_rubinstein_path")

# Chart 2: NE vs SPNE Venn Diagram (High Quality)
def plot_ne_spne_hierarchy():
    from matplotlib.patches import Ellipse
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Outer: NE
    ax.add_patch(Ellipse((5, 5), 8, 7, color='#A8DADC', alpha=0.3))
    ax.text(5, 8.2, "Nash Equilibria (NE)", ha='center', fontsize=14, fontweight='bold', color='#1D3557')
    
    # Inner: SPNE
    ax.add_patch(Ellipse((5, 4.5), 4, 3.5, color='#457B9D', alpha=0.6))
    ax.text(5, 4.5, "Subgame Perfect\n(SPNE)", ha='center', va='center', color='white', fontsize=12, fontweight='bold')
    
    # Explanations
    ax.annotate("Non-credible threats\non off-equilibrium paths", xy=(7.5, 6.5), xytext=(8.5, 7.5),
                arrowprops=dict(arrowstyle="->", color='#1D3557'), ha='center')
    
    ax.annotate("Sequential Rationality\nat every subgame", xy=(4, 4), xytext=(1.5, 2),
                arrowprops=dict(arrowstyle="->", color='#1D3557'), ha='center')
    
    plt.title("Refining Rationality: The Hierarchy of Equilibria", fontsize=16, fontweight='bold', pad=20)
    save_fig("lecture08_ne_spne_relation_premium")

# Chart 3: Reputation Collapse (Finite Game)
def plot_reputation_collapse():
    T = 10
    periods = np.arange(1, T + 1)
    fig, ax = plt.subplots()
    
    # Logic: Deterrence incentive is 0 because of backward induction
    # But we visualize the "collapse" from T backwards
    x = periods
    y = np.ones(T)
    
    # Fade out as we go back? No, it's a step function that's 0 everywhere in SPNE
    ax.axhline(0, color='gray', lw=1, alpha=0.5)
    ax.scatter(periods, np.zeros(T), color='#E76F51', s=100, zorder=3)
    
    # Add an arrow showing induction direction
    ax.annotate('', xy=(1, -0.05), xytext=(10, -0.05), 
                arrowprops=dict(arrowstyle="->", color='#264653', lw=2))
    ax.text(5.5, -0.15, "Backward Induction Logic Flow", ha='center', fontweight='bold', color='#264653')
    
    ax.text(10, 0.05, "Last Period:\nNo Future -> Concede", ha='center', fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="#F1FAEE", ec="#E76F51"))
    ax.text(1, 0.05, "Period 1:\nInduction Collapses\nReputation to 0", ha='center', fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="#F1FAEE", ec="#E76F51"))
    
    ax.set_ylim(-0.3, 0.5)
    ax.set_xticks(periods)
    ax.set_xlabel("Period (t)")
    ax.set_ylabel("Strategic Incentive to Fight")
    ax.set_title("The Selten Chain-Store Paradox: Reputation Collapse", fontweight='bold')
    ax.axis('off')
    
    save_fig("lecture08_reputation_collapse_nbp")

if __name__ == "__main__":
    plot_rubinstein_bargaining()
    plot_ne_spne_hierarchy()
    plot_reputation_collapse()
    print("Nano Banana Pro style charts for Lecture 08 generated.")
