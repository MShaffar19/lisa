import pytest


@pytest.mark.feature("xdp")
def test_xdp_b() -> None:
    pass


@pytest.mark.feature("gpu")
def test_gpu_b() -> None:
    pass


@pytest.mark.feature("rdma")
def test_rdma_b() -> None:
    pass
