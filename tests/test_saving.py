# INF601 - Advanced Programming in Python
# Chase Coble
# Mini Project 2

import matplotlib.pyplot as plt
from src.saving import save_chart

def test_save_chart_writes_png_file(tmp_path):
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 2, 3])

    output_path = save_chart(fig, "AAPL", output_dir=str(tmp_path))

    assert output_path.endswith("AAPL.png")
    assert (tmp_path / "AAPL.png").exists()
    assert (tmp_path / "AAPL.png").stat().st_size > 0
