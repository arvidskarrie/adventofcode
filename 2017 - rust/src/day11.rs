use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;
// use std::collections::VecDeque;
use num_complex::Complex;

fn get_data() -> Vec<String> {
    let file = File::open("input_data.txt").unwrap();
    
    let lines: Vec<String> = BufReader::new(file)
    .lines()
    .map(|line| line.unwrap())
    .collect();
    lines
}

// Simulate this hexagonal grid with a quadratic grid. That means ne and sw will be a diagonal move, while se and nw will be right/left move

pub fn main() {      
    let dir_to_complex: HashMap<String, Complex<i32>> = HashMap::from([
        ("n".to_string(), Complex::new(1, 0)),
        ("ne".to_string(), Complex::new(1, 1)),
        ("se".to_string(), Complex::new(0, 1)),
        ("s".to_string(), Complex::new(-1, 0)),
        ("sw".to_string(), Complex::new(-1, -1)),
        ("nw".to_string(), Complex::new(0, -1)),
    ]);

    let input_data = get_data();
    let dir_input: Vec<_> = input_data.first().unwrap().split(",").collect();
    let complex_input: Vec<_> = dir_input.iter().map(|dir| dir_to_complex[*dir]).collect();

    let mut current_pos = Complex::new(0, 0);
    let mut maximum_distance = 0;
    for step in complex_input {
        current_pos += step;

        // Find the minimum steps to get back to origo
        // We are allowed to move diagonally in +/+ or -/- direction
        let this_distance = if current_pos.re.signum() == current_pos.im.signum() {
            std::cmp::max(current_pos.re.abs(), current_pos.im.abs())
        } else {
            current_pos.re.abs() + current_pos.im.abs()
        };
        maximum_distance = std::cmp::max(maximum_distance, this_distance);
    }
    println!("Maximum steps needed {}", maximum_distance);
}
    



