use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;

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
    let mut no_of_valids = 0;

    for line in input_data {
        // let string_vector: Vec<_> = line.split_whitespace().map(|s| s.chars().collect::<Vec<char>>().sort_unstable().into_iter().collect()).collect();
        let mut string_vector: Vec<String> = line.split_whitespace().map(|s| s.to_string()).collect();
        for s in &mut string_vector {
            let mut chars: Vec<char> = s.chars().collect();
            chars.sort_unstable();
            *s = chars.into_iter().collect::<String>();
        }
        

        let string_set: HashSet<_> = string_vector.iter().cloned().collect();
        if string_vector.len() == string_set.len() {no_of_valids += 1;}
    }

    println!("{}", no_of_valids);
}