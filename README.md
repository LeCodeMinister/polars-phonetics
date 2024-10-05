# Polars-Phonetics: A Polars Plugin for Phonetic Algorithms

## Initial Release: Double-Metaphone Algorithm

Welcome to Polars-Phonetics, a Polars plugin for phonetic algorithms built in Rust for Python users. This initial release includes the Double-Metaphone algorithm only.

## Installation

To use Polars-Phonetics, install the polars-phonetics package using pip:

```bash
pip install polars-phonetics
```

## Example Usage

Here's an example of how to use the double_metaphone function in Python Polars:

```python
import polars as pl
from polars_phonetics import dmetaphone

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


# Apply the double_metaphone function to the 'words' column
result = df.with_columns(dmetaphone=dmetaphone("words"))

print(result)

# shape: (9, 2)
# ┌───────────┬──────────────┐
# │ words     ┆ dmetaphone   │
# │ ---       ┆ ---          │
# │ str       ┆ str          │
# ╞═══════════╪══════════════╡
# │ hello     ┆ [HL, HL]     │
# │ this      ┆ [0S, TS]     │
# │ is        ┆ [AS, AS]     │
# │ the       ┆ [0, T]       │
# │ phonetics ┆ [FNTK, FNTK] │
# │ plugin    ┆ [PLJN, PLKN] │
# │ in        ┆ [AN, AN]     │
# │ polars    ┆ [PLRS, PLRS] │
# │ null      ┆ null         │
# └───────────┴──────────────┘
```

## Acknowledgments

I would like to extend my gratitude to:

- Marco Gorelli for his comprehensive guide on writing [Polars plugins](https://marcogorelli.github.io/polars-plugins-tutorial/).
- The team behind the Rust crate [rphonetic](https://crates.io/crates/rphonetic).

## Future Releases

Future releases of Polars-Phonetics will include additional phonetic algorithms. Stay tuned for updates!

## Contributing

If you'd like to contribute to Polars-Phonetics, please open an issue or pull request on this repository. I welcome any feedback, bug reports, or new algorithm implementations.

## License

Polars-Phonetics is licensed under the MIT License. See the LICENSE file for details.