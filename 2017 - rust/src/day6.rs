use std::fs::File;
use std::io::{BufRead, BufReader};
// use std::collections::HashMap;
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

    let mut memory_banks: Vec<i32> = Vec::new();
    for int_as_string in input_data.iter() {
        match int_as_string.parse::<i32>() {
            Ok(num) => { memory_banks.push(num); },
            Err(e) => { eprintln!("Error parsing string to number: {}", e); return; },
        }
    }

    let no_of_banks = memory_banks.len();
    let mut hash_set = HashSet::new();
    
    for i in 0.. {
        // Add it to set if not already in it
        if memory_banks == target_banks {
            println!("i {} banks {:?}", i, memory_banks);
        }
        if !hash_set.insert(memory_banks.clone()) {
            println!("iterations until escape {}", i);
            break;
        }        
        
        // find max value and index
        let (index, &max) = memory_banks.iter().enumerate().max_by(|&(i1, v1), &(i2, v2)| v1.cmp(&v2).then_with(|| i2.cmp(&i1))).unwrap();
        // println!("index {} max {}", index, max);
        
        // empty it
        *memory_banks.get_mut(index).unwrap() = 0;
        
        // Loop over the other banks and add blocks in order
        let start = (index + 1) as usize;
        let stop = start + max as usize;
        for bank in start..stop {
            *memory_banks.get_mut(bank % no_of_banks).unwrap() += 1;
        }
        // println!("i {} banks {:?}", i, memory_banks);
    }
}
