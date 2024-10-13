import polars as pl
from polars_phonetics import nysiis
from polars.testing import assert_frame_equal


def test_nysiis():
    df = pl.DataFrame(
        {
            "words": ["hello", "this", "is", "the", "phonetics", "plugin", "in", "polars", None],
        }
    )
    result = df.with_columns(nysiis=nysiis("words"))

    expected_df = pl.DataFrame(
        {
            "words": ["hello", "this", "is", "the", "phonetics", "plugin", "in", "polars", None],
            "nysiis": ['HAL', 'T', 'I', 'T', 'FANATA', 'PLAGAN', 'IN', 'PALAR', None],
        }
    )

    assert_frame_equal(result, expected_df)