import pytest
from app.views import mul


@pytest.mark.parametrize(
    ["a", "b", "out"],
    [
        (2, 3, 6),
        (3, 3, 9),
        (4, 3, 12),
    ]
)
def test_mul(a, b, out):
    assert mul(a, b) == out