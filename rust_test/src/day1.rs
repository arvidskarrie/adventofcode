use std::fs::File;
use std::io::{BufRead, BufReader};

fn get_data() -> Vec<String> {
    let file = File::open("input_data.txt").unwrap();

    let lines: Vec<String> = BufReader::new(file)

        .lines()
        .map(|line| line.unwrap())
        .collect();
    lines
}

fn main() {
      
    let input_data = get_data();
    let input_int_vector: Vec<u32> = input_data[0].chars().map(|c|  c.to_digit(10).unwrap()).collect();

    let mut total_sum = 0;

    // part a
    // for i in 0..input_int_vector.len() {
    //     if input_int_vector[i] == input_int_vector[(i + 1) % input_int_vector.len()] {
    //         total_sum += input_int_vector[i];
    //     }
    // }

    // part b
    let no_of_integers = input_int_vector.len();
    for i in 0..no_of_integers {
        
        if input_int_vector[i] == input_int_vector[(i + no_of_integers / 2) % no_of_integers] {
            total_sum += input_int_vector[i];
        }
    }

    println!("Total sum {}", total_sum);
}
