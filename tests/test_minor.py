from src.modules import minor


def test_minor_rsf():
    assert minor.rsf(7.95e14, 3.32) == 2.394578313253012e+21

def test_minor_hmr(self):
    assert minor.hmr(30.973762, 30.9816203) == 3941.5346830745675

