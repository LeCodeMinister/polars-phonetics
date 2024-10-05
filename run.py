import polars as pl
from polars_phonetics import dmetaphone


df = pl.DataFrame(
    {
        "words": ["this", "is", "polars", "phonetics", "python"],
    }
)
result = df.with_columns(dmetaphone=dmetaphone("words"))

with pl.Config() as cfg:
    cfg.set_tbl_cols(-1)
    cfg.set_tbl_rows(100)
    print(result)