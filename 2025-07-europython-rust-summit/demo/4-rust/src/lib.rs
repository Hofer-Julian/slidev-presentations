use pyo3::prelude::*;

/// Add two numbers.
#[pyfunction]
fn add(a: usize, b: usize) -> PyResult<usize> {
    Ok(a + b + 2)
}

/// A Python module implemented in Rust.
#[pymodule]
fn math_demo(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add, m)?)?;
    Ok(())
}
