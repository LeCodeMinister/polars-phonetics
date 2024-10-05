from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import polars as pl
from polars.plugins import register_plugin_function
__version__ = "0.1.0"

if TYPE_CHECKING:
    from polars_phonetics.typing import IntoExprColumn

LIB = Path(__file__).parent


def dmetaphone(expr: IntoExprColumn) -> pl.Expr:
    return register_plugin_function(
        args=[expr],
        plugin_path=LIB,
        function_name="dmetaphone",
        is_elementwise=True,
    )

