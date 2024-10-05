#![allow(clippy::unused_unit)]
use polars::prelude::*;
use pyo3_polars::derive::polars_expr;
use rphonetic::{ DoubleMetaphone, Encoder };

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