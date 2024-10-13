# Polars-Phonetics: A Polars Plugin for Phonetic Algorithms

## v0.2.0 Release: Metaphone, Soundex & Nysiis Algorithms added!

Welcome to Polars-Phonetics, a Polars plugin for phonetic algorithms built in Rust for Python users. This second release includes the Metaphone, Soundex & Nysiis algorithms, in addition to the Double-Metaphone algorithm in the initial release.

With the current algorithms, Polars-Phonetics can replace the 'phonetics' Python module, no need for `map_elements(soundex)` from now on!

## Installation

To use Polars-Phonetics, install the polars-phonetics package using pip:

```bash
pip install polars-phonetics
```

## Example Usage

Here's an example of how to use the double_metaphone, metaphone, soundex & nysiis functions in Polars Phonetics:

```python
import polars as pl
from polars_phonetics import dmetaphone, soundex, metaphone, nysiis

# Create a sample dataframe
df = pl.DataFrame(
    {
        "words": ["hello", "this", "is", "the", "phonetics", "plugin", "in", "polars", None],
    }
)

print(df)

# This would output:
# shape: (9, 1)
# ┌───────────┐
# │ words     │
# │ ---       │
# │ str       │
# ╞═══════════╡
# │ hello     │
# │ this      │
# │ is        │
# │ the       │
# │ phonetics │
# │ plugin    │
# │ in        │
# │ polars    │
# │ null      │
# └───────────┘


# Apply the double_metaphone, soundex, metaphone & nysiis functions to the 'words' column
result = df.with_columns(
    dmetaphone=dmetaphone("words"),
    soundex=soundex("words"),
    metaphone=metaphone("words"),
    nysiis=nysiis("words"),
)

print(result)

# shape: (9, 5)
# ┌───────────┬──────────────┬─────────┬───────────┬────────┐
# │ words     ┆ dmetaphone   ┆ soundex ┆ metaphone ┆ nysiis │
# │ ---       ┆ ---          ┆ ---     ┆ ---       ┆ ---    │
# │ str       ┆ str          ┆ str     ┆ str       ┆ str    │
# ╞═══════════╪══════════════╪═════════╪═══════════╪════════╡
# │ hello     ┆ [HL, HL]     ┆ H400    ┆ HL        ┆ HAL    │
# │ this      ┆ [0S, TS]     ┆ T200    ┆ 0S        ┆ T      │
# │ is        ┆ [AS, AS]     ┆ I200    ┆ IS        ┆ I      │
# │ the       ┆ [0, T]       ┆ T000    ┆ 0         ┆ T      │
# │ phonetics ┆ [FNTK, FNTK] ┆ P532    ┆ FNTK      ┆ FANATA │
# │ plugin    ┆ [PLJN, PLKN] ┆ P425    ┆ PLJN      ┆ PLAGAN │
# │ in        ┆ [AN, AN]     ┆ I500    ┆ IN        ┆ IN     │
# │ polars    ┆ [PLRS, PLRS] ┆ P462    ┆ PLRS      ┆ PALAR  │
# │ null      ┆ null         ┆ null    ┆ null      ┆ null   │
# └───────────┴──────────────┴─────────┴───────────┴────────┘
```

## Acknowledgments

I would like to extend my gratitude to:

- Marco Gorelli for his comprehensive guide on writing [Polars Plugins](https://marcogorelli.github.io/polars-plugins-tutorial/).
- The team behind the Rust crate [rphonetic](https://crates.io/crates/rphonetic).
- The Discord server for Polars, especially the [plugins channel](https://discord.com/channels/908022250106667068/1174049891794812998).

## Future Releases

Future releases of Polars-Phonetics will include additional phonetic algorithms with options to customise outputs through arguments. Stay tuned for updates!

## Contributing

If you'd like to contribute to Polars-Phonetics, please open an issue or pull request on this repository. I welcome any feedback, bug reports, or new algorithm implementations.

## License

Polars-Phonetics is licensed under the MIT License. See the LICENSE file for details.