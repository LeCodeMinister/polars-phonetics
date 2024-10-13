#![allow(clippy::unused_unit)]
use polars::prelude::*;
use pyo3_polars::derive::polars_expr;
use rphonetic::{ DoubleMetaphone, Soundex, Metaphone, Nysiis, Encoder };

#[polars_expr(output_type=String)]
fn dmetaphone(inputs: &[Series]) -> PolarsResult<Series> {
    let ca: &StringChunked = inputs[0].str()?;
    let dm = DoubleMetaphone::default();
   
    let out: StringChunked = ca.apply_into_string_amortized(|value: &str, output: &mut String| {
        let primary = dm.encode(value);
        let secondary = dm.encode_alternate(value);
        output.push_str(&format!("[{}, {}]", primary, secondary));
    });

    Ok(out.into_series())
}

#[polars_expr(output_type=String)]
fn soundex(inputs: &[Series]) -> PolarsResult<Series> {
    let ca: &StringChunked = inputs[0].str()?;
    let soundex: Soundex = Soundex::default();
   
    let out: StringChunked = ca.apply_into_string_amortized(|value: &str, output: &mut String| {
        let value = soundex.encode(value);
        output.push_str(&format!("{}", value));
    });

    Ok(out.into_series())
}

#[polars_expr(output_type=String)]
fn metaphone(inputs: &[Series]) -> PolarsResult<Series> {
    let ca: &StringChunked = inputs[0].str()?;
    let metaphone: Metaphone = Metaphone::default();
   
    let out: StringChunked = ca.apply_into_string_amortized(|value: &str, output: &mut String| {
        let value = metaphone.encode(value);
        output.push_str(&format!("{}", value));
    });

    Ok(out.into_series())
}

#[polars_expr(output_type=String)]
fn nysiis(inputs: &[Series]) -> PolarsResult<Series> {
    let ca: &StringChunked = inputs[0].str()?;
    let nysiis: Nysiis = Nysiis::default();
   
    let out: StringChunked = ca.apply_into_string_amortized(|value: &str, output: &mut String| {
        let value = nysiis.encode(value);
        output.push_str(&format!("{}", value));
    });

    Ok(out.into_series())
}