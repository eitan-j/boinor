"""these tests take care of special cases in _math that are not covered by other tests"""

# from collections import OrderedDict
# from functools import partial
# import pickle
# from unittest import mock
#
# from astropy import units as u
# from astropy.coordinates import (
#    ITRS,
#    CartesianDifferential,
#    CartesianRepresentation,
#    SkyCoord,
# )
# from astropy.tests.helper import assert_quantity_allclose
# from astropy.time import Time
# from hypothesis import example, given, settings, strategies as st
import numpy as np
import pytest

from boinor._math.interpolate import sinc_interp


def test_sinc_interp():
    x = [1, 2, 3]
    y = [1, 2, 3, 4, 5]
    u = [1, 2]

    with pytest.raises(ValueError) as excinfo:
        sinc_interp(x, y, u)
    assert excinfo.type is ValueError
    assert excinfo.type is not None


def test_sinc_interp_from_ephem():
    x = np.array([0.0, 0.0, 0.0, 0.0])
    y = np.array([2458910.0, 2458911.0, 2458912.0, 2458913.0])
    u = np.array([2458910.0, 2458912.0])
    expected_result = np.array([0.0, 0.0])
    result = sinc_interp(x, y, u)
    assert np.all(result == expected_result)

    x = np.array([0.0, 0.0, 0.0, 0.0])
    y = np.array([2458910.0, 2458911.0, 2458912.0, 2458913.0])
    u = np.array([2458910.0, 2458911.0, 2458912.0, 2458913.0])
    expected_result = np.array([0.0, 0.0, 0.0, 0.0])
    result = sinc_interp(x, y, u)
    assert np.all(result == expected_result)

    x = np.array([0.0, 0.1, 0.2, 0.3])
    y = np.array([2458910.0, 2458911.0, 2458912.0, 2458913.0])
    u = np.array([2458910.0, 2458911.0, 2458912.0, 2458913.0])
    expected_result = np.array([0.0, 0.1, 0.2, 0.3])
    result = sinc_interp(x, y, u)
    # assert np.all(result == expected_result)
    assert result.all() == expected_result.all()
