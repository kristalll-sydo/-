import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

# Set style for "Nano banana pro"
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

# Chart 1: Entry Deterrence Game Tree (Premium Visualization)
def plot_entry_deterrence_premium():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 6)
    ax.axis('off')
    
    # Define Nodes
    # Root: Entrant (E)
    # Branches: In (to Incumbent I), Out (Terminal)
    
    # Lines
    ax.plot([0, 4], [3, 5], color='#333333', lw=2) # E -> I
    ax.plot([0, 4], [3, 1], color='#333333', lw=2) # E -> Out
    
    ax.plot([4, 9], [5, 6], color='#333333', lw=2) # I -> Accommodate
    ax.plot([4, 9], [5, 4], color='#E76F51', lw=2, linestyle='--') # I -> Fight (Non-credible)
    
    # Nodes
    ax.scatter([0, 4], [3, 5], color='#264653', s=150, zorder=5) # Decision nodes
    ax.scatter([4, 9, 9], [1, 6, 4], color='#333333', marker='s', s=100, zorder=5) # Terminal nodes
    
    # Labels
    ax.text(-0.5, 3, "Entrant (E)", ha='right', va='center', fontweight='bold')
    ax.text(4, 5.3, "Incumbent (I)", ha='center', fontweight='bold')
    
    ax.text(2, 4.5, "In", ha='center', style='italic')
    ax.text(2, 1.5, "Out", ha='center', style='italic')
    ax.text(6.5, 6, "Accommodate (A)", ha='center', style='italic')
    ax.text(6.5, 4, "Fight (F)", ha='center', style='italic', color='#E76F51')
    
    # Payoffs
    ax.text(4.2, 1, "(0, 3)", va='center')
    ax.text(9.2, 6, "(2, 2)", va='center', fontweight='bold', color='#2A9D8F') # Equilibrium
    ax.text(9.2, 4, "(-1, -1)", va='center', color='#E76F51')
    
    # Annotation for Non-credible threat
    ax.annotate("Non-credible Threat:\nI prefers 2 > -1", xy=(7, 4.5), xytext=(8, 3),
                arrowprops=dict(arrowstyle="->", color='#E76F51'), color='#E76F51', fontsize=10)
    
    plt.title("Strategic Analysis: The Logic of Entry Deterrence", fontsize=16, fontweight='bold')
    save_fig("lecture07_entry_deterrence_nbp")

# Chart 2: Commitment Cost vs Utility
def plot_commitment_logic():
    x = np.linspace(0, 5, 100)
    # Payoff with commitment vs without
    # Without: 2 (Accommodate)
    # With commitment K: 3 - c*K (Monopoly minus cost)
    # Deterrence threshold: If K > K_min, Entrant stays out.
    
    y_no_commit = np.full_like(x, 2)
    y_commit = 4 - 0.8*x # Sinking cost
    
    fig, ax = plt.subplots()
    ax.plot(x, y_no_commit, label="Accommodate Profit (Passive)", color='#264653', linestyle='--')
    ax.plot(x, y_commit, label="Monopoly Profit minus Commitment Cost", color='#E76F51', lw=2)
    
    # Fill region where commitment is better
    ax.fill_between(x, y_no_commit, y_commit, where=(y_commit > y_no_commit), 
                    color='#2A9D8F', alpha=0.2, label='Strategic Advantage Zone')
    
    ax.axvline(2.5, color='#333333', linestyle=':', alpha=0.5)
    ax.text(2.6, 3, "Threshold: Cost too high\nfor Deterrence", fontsize=10)
    
    ax.set_xlabel("Commitment Investment (K)")
    ax.set_ylabel("Expected Payoff to Incumbent")
    ax.set_title("The Calculus of Commitment: When to 'Tie One's Hands'", fontweight='bold')
    ax.legend()
    sns.despine()
    save_fig("lecture07_commitment_logic_nbp")

if __name__ == "__main__":
    plot_entry_deterrence_premium()
    plot_commitment_logic()
    print("Nano Banana Pro style charts for Lecture 07 generated.")
