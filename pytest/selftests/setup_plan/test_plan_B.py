import pytest


def test_xdp_b(feature) -> None:
    if feature != "xdp":
        pytest.skip("Required feature missing")


def test_gpu_b(feature) -> None:
    if feature != "gpu":
        pytest.skip("Required feature missing")


def test_rdma_b(feature) -> None:
    if feature != "rdma":
        pytest.skip("Required feature missing")