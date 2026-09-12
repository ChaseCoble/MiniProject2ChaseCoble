# INF601 - Advanced Programming in Python
# Chase Coble
# Mini Project 2

import os
import matplotlib.pyplot as plt


def save_chart(fig, symbol, output_dir="."):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{symbol}.png")
    fig.savefig(output_path)
    plt.close(fig)
    return output_path
