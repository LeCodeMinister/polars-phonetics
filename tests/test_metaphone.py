import polars as pl
from polars_phonetics import metaphone
from polars.testing import assert_frame_equal


def test_metaphone():
    df = pl.DataFrame(
        {
            "words": ["hello", "this", "is", "the", "phonetics", "plugin", "in", "polars", None],
        }
    )
    result = df.with_columns(metaphone=metaphone("words"))

    expected_df = pl.DataFrame(
        {
            "words": ["hello", "this", "is", "the", "phonetics", "plugin", "in", "polars", None],
            "metaphone": ['HL', '0S', 'IS', '0', 'FNTK', 'PLJN', 'IN', 'PLRS', None],
        }
    )

    assert_frame_equal(result, expected_df)