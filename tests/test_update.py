import pytest
from pytest import approx
import distogram


def test_update():
    h = distogram.Distogram(bins=3)

    # fill histogram
    h = distogram.update(h, 23)
    assert h.binned_data == [(23, 1)]
    h = distogram.update(h, 28)
    assert h.binned_data == [(23, 1), (28, 1)]
    h = distogram.update(h, 16)
    assert h.binned_data == [(16, 1), (23, 1), (28, 1)]

    # update count on existing value
    h = distogram.update(h, 23)
    assert h.binned_data == [(16, 1), (23, 2), (28, 1)]
    h = distogram.update(h, 28)
    assert h.binned_data == [(16, 1), (23, 2), (28, 2)]
    h = distogram.update(h, 16)
    assert h.binned_data == [(16, 2), (23, 2), (28, 2)]

    # merge values
    h = distogram.update(h, 26)
    assert h.binned_data[0] == (16, 2)
    assert h.binned_data[1] == (23, 2)
    assert h.binned_data[2][0] == approx(27.33333)
    assert h.binned_data[2][1] == 3


def test_update_with_invalid_count():
    h = distogram.Distogram(bins=3)

    with pytest.raises(ValueError):
        distogram.update(h, 23, count=0)