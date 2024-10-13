import polars as pl
from polars_phonetics import dmetaphone, soundex, metaphone, nysiis


df = pl.DataFrame(
    {
        "words": ["hello", "this", "is", "the", "phonetics", "plugin", "in", "polars", None],
    }
)
result = df.with_columns(
    dmetaphone=dmetaphone("words"),
    soundex=soundex("words"),
    metaphone=metaphone("words"),
    nysiis=nysiis("words"),
)

with pl.Config() as cfg:
    cfg.set_tbl_cols(-1)
    cfg.set_tbl_rows(100)
    print(result)