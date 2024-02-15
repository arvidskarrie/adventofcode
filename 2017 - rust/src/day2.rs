use std::fs::File;
use std::io::{BufRead, BufReader};
use std::cmp::Ordering;

fn get_data() -> Vec<String> {
    let file = File::open("input_data.txt").unwrap();

    let lines: Vec<String> = BufReader::new(file)

        .lines()
        .map(|line| line.unwrap())
        .collect();
    lines
}

// fn calculate_line_difference(line: &str) -> i32 {
    // let string_vector: Vec<&str> = line.split_whitespace().collect();
    // let int_vector: Vec<i32> = string_vector.iter().map(|s| s.parse().unwrap()).collect();
    // *int_vector.iter().max().unwrap() - *int_vector.iter().min().unwrap()
// }

fn calculate_line_quotient(line: &str) -> i32 {
    let mut int_vector: Vec<i32> = line.split_whitespace().map(|s| s.parse().unwrap()).collect();
    // int_vector.sort_by(|a, b| a.cmp(b));
    int_vector.sort_by(|a, b| {
        if a < b {Ordering::Greater}
        Ordering::Less
    });

    for (i, &num) in int_vector.iter().enumerate() {
        for &den in &int_vector[i + 1..] {
            if num % den == 0 {
                return num / den;
            }
        }
    }

    panic!("Value not found");
}

// fn main() {
      
//     let input_data = get_data();
//     let total_sum: i32 = input_data.iter().map(|line| calculate_line_difference(&line)).sum();

//     println!("Total sum {}", total_sum);
// }

// fn main() {
//     println!("Total sum {}", get_data().iter().map(|line| calculate_line_difference(&line)).sum::<i32>());
// }

fn main() {
    println!("Total sum {}", get_data().iter().map(|line| calculate_line_quotient(&line)).sum::<i32>());
}
