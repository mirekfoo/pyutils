from pyutils.config_util import read_config_harg


def test_read_config_harg_adds_defaults():
    cfg = {}

    read_config_harg(cfg, "a.b.c", "X")
    read_config_harg(cfg, "a.b.d", "Y")
    read_config_harg(cfg, "a.e.c", "Z")
    read_config_harg(cfg, "a.f",   "FX")
    read_config_harg(cfg, "a.g.c", "FGY")

    assert cfg == {
        "a": {
            "b": {
                "c": "X",
                "d": "Y",
            },
            "e": {
                "c": "Z",
            },
            "f": "FX",
            "g": {
                "c": "FGY",
            },
        }
    }
