import polars as pl
from polars_phonetics import dmetaphone
from polars.testing import assert_frame_equal


def test_dmetaphone():
    df = pl.DataFrame(
        {
            "words": ["hello", "this", "is", "the", "phonetics", "plugin", "in", "polars", None],
        }
    )
    result = df.with_columns(dmetaphone=dmetaphone("words"))

    expected_df = pl.DataFrame(
        {
            "words": ["hello", "this", "is", "the", "phonetics", "plugin", "in", "polars", None],
            "dmetaphone": ["[HL, HL]", "[0S, TS]", "[AS, AS]", "[0, T]", "[FNTK, FNTK]", "[PLJN, PLKN]", "[AN, AN]", "[PLRS, PLRS]", None],
        }
    )

    assert_frame_equal(result, expected_df)