use geos::{Error, Geom, Geometry};

fn main() -> Result<(), Error> {
    // Create square with length of 5
    let square = Geometry::new_from_wkt(
        "POLYGON ((0 0, 0 5, 5 5, 5 0, 0 0))",
    )?;
    // 5 x 5 should be 25!
    println!("Area : {}", square.area()?);
    Ok(())
}
