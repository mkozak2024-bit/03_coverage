from app import get_angles


def test_triangle():
    assert get_angles("трикутник") == 180


def test_square():
    assert get_angles("квадрат") == 360


def test_rectangle():
    assert get_angles("прямокутник") == 360


def test_unknown_figure():
    assert get_angles("коло") is None


def test_main():
    import runpy
    runpy.run_module("app", run_name="__main__")