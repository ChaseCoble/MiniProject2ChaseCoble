import numpy as np
import pandas as pd
from src.transform import to_price_array

def test_to_price_array_converts_series_to_np():
    fake_series = pd.Series([100, 101, 102, 103, 104, 105, 106, 107, 108, 109])
    result = to_price_array(fake_series)

    assert isinstance(result, np.ndarray)
    assert len(result) == 10
    assert result.dtype == np.float64
    assert result[0] == 100
    assert result[-1] == 109
