from src.modules import minor


def test_minor_rsf():
    assert minor.rsf(7.95e14, 3.32) == 2.39e21
