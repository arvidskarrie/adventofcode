use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::{HashMap, HashSet};
use std::time::Instant;

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
    let start = Instant::now();
    let input_data = get_data();
    let mut hash_map: HashMap<i32, i32> = HashMap::new();
    for line in input_data {
        let vec = line.split(": ").map(|v| v.parse().unwrap()).collect::<Vec<i32>>();
        let period = 2 * (vec[1] - 1);
        hash_map.insert(vec[0], period);
    }

    for waiting_time in 0.. {
        // Severity points needs to be added if the scanner is at the top level when we enter.
        // The scanner will be at the top at the beginning of every 2 * (depth - 1) ps.
        // The packet will enter its layer at ps layer.
        let mut detected = false;
        for (layer, period) in &hash_map {
            let total_time_passed = waiting_time + layer;
            if total_time_passed % period == 0 {
                detected = true;
                break;
            }
        }

        if !detected {
            println!("waiting time {}, detected = {}", waiting_time, detected); // 3923436
            break;
        }
    }

    let duration = start.elapsed();
    println!("Time elapsed: {:?}", duration);
}
    



