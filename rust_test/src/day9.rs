use std::fs::File;
use std::io::{BufRead, BufReader};
// use std::collections::HashMap;


fn get_data() -> Vec<String> {
    let file = File::open("input_data.txt").unwrap();
    
    let lines: Vec<String> = BufReader::new(file)
    .lines()
    .map(|line| line.unwrap())
    .collect();
    lines
}

fn main() {      
    let mut input_data = get_data().first().unwrap().clone().chars().collect::<Vec<char>>();

    let mut idx: usize = 0;
    let mut garbage_started = false;
    let mut garbage_start_idx: usize = 0;
    let mut garbage_score = 0;
    let mut current_score_level = 1;
    let mut total_score = 0;

    while idx < input_data.len() {
        match input_data[idx] {
            '!' => {
                input_data.remove(idx);
                input_data.remove(idx);
            }
            '>' if garbage_started => {
                // Remove garbage = everything from garbage_start_idx to idx inclusive
                let vec = input_data.drain(garbage_start_idx..(idx+1));
                garbage_score += vec.len() - 2;
                garbage_started = false;
                idx = garbage_start_idx;
            }
            '<' if !garbage_started => {
                garbage_started = true;
                garbage_start_idx = idx.clone();
                idx += 1;
            }
            '{' if !garbage_started => {
                total_score += current_score_level;
                current_score_level += 1;
                idx += 1;
            }
            '}' if !garbage_started => {
                current_score_level -= 1;
                idx += 1;
            }
            _ =>
                idx += 1,
        }

    }

    println!("total_score {} garbage_score {}", total_score, garbage_score);
}


