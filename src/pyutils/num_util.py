"""Number utilities"""

from typing import Literal


def _format_scaled(
    value: int | float,
    *, # keyword-only arguments below
    base: Literal[1000, 1024] = 1000,
    decimals: int = 2,
    unit: str = "",
) -> str:
    """
    Format number using automatic scale suffix.

    Examples:
        format_scaled(15320) -> '15.32K'
        format_scaled(15320, base=1024, unit = "B") -> '14.96KB'
        format_scaled(7_000_000_000) -> '7B'
    """

    if base not in (1000, 1024):
        raise ValueError("base must be 1000 or 1024")

    suffixes = ["", "K", "M", "B", "T", "P", "E"]

    negative = value < 0
    value = abs(float(value))

    idx = 0
    while value >= base and idx < len(suffixes) - 1:
        value /= base
        idx += 1

    formatted = f"{value:.{decimals}f}".rstrip("0").rstrip(".")

    if negative:
        formatted = "-" + formatted

    return f"{formatted}{suffixes[idx]}{unit}"

def format_dec_scaled(value: int | float, *, decimals: int = 2, unit: str = "") -> str:
    """
    Format number using decimal scale suffix.

    Examples:
        format_dec_scaled(15320) -> '15.32K'
        format_dec_scaled(7_000_000_000) -> '7B'
    """

    return _format_scaled(value, base=1000, decimals=decimals, unit=unit)

def format_bin_scaled(value: int | float, *, decimals: int = 2, unit: str = "") -> str:
    """
    Format number using binary scale suffix.

    Examples:
        format_bin_scaled(15320, unit="B") -> '14.96KB'
        format_bin_scaled(7_000_000_000, unit="B") -> '6.52GB'
    """

    return _format_scaled(value, base=1024, decimals=decimals, unit=unit)

def format_bytes_scaled(value: int | float, *, decimals: int = 2) -> str:
    """
    Format number of bytes using binary scale suffix.

    Examples:
        format_bytes_scaled(15320) -> '14.96KB'
        format_bytes_scaled(7_000_000_000) -> '6.52GB'
    """

    return format_bin_scaled(value, decimals=decimals, unit="B")
