use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;

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

    let mut hash_map = HashMap::new();
    for (i, int_as_string) in input_data.iter().enumerate() {
        match int_as_string.parse::<i32>() {
            Ok(num) => { hash_map.insert(i as i32, num); },
            Err(e) => { eprintln!("Error parsing string to number: {}", e); return; },
        }
    }

    let mut position: i32 = 0;
    for i in 0.. {
        if let Some(&offset) = hash_map.get(&position) {
            let new_position = position + offset;
            *hash_map.get_mut(&position).unwrap() += if offset >= 3 {-1} else {1};
            position = new_position;
        } else {
            println!("iterations until escape {}", i);
            break;
        }
    }
}
