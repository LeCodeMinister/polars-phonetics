import polars as pl
from polars_phonetics import soundex
from polars.testing import assert_frame_equal


def test_soundex():
    df = pl.DataFrame(
        {
            "words": ["hello", "this", "is", "the", "phonetics", "plugin", "in", "polars", None],
        }
    )
    result = df.with_columns(soundex=soundex("words"))

    expected_df = pl.DataFrame(
        {
            "words": ["hello", "this", "is", "the", "phonetics", "plugin", "in", "polars", None],
            "soundex": ['H400', 'T200', 'I200', 'T000', 'P532', 'P425', 'I500', 'P462', None],
        }
    )

    assert_frame_equal(result, expected_df)