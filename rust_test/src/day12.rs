use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::{HashMap, HashSet};
use regex::Regex;


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
    let input_data = get_data();
    let regex_variable = Regex::new(r"^(\d+) <-> (.*)$").unwrap();
    let mut hash_map: HashMap<i32, Vec<i32>> = HashMap::new();

    for line in input_data {
        match regex_variable.captures(line.as_str()) {
            Some(captures) => {
                let key = captures.get(1).unwrap().as_str().parse().unwrap();
                // expect("Not possible to parse key");
                let vec = captures.get(2).unwrap().as_str().split(", ").map(|v| v.parse().expect("Not possible to parse value")).collect::<Vec<i32>>();
                hash_map.insert(key, vec);
            },
            None => panic!()
        }
    }
   
    let mut no_of_groups = 0;
    while !hash_map.is_empty()
    {
        let mut program_stack: Vec<i32> = Vec::new();

        // Start the process with a random entry
        let start_entry = hash_map.keys().next().unwrap();
        program_stack.push(*start_entry);
        let mut stack_idx = 0;

        while stack_idx < program_stack.len() {
            let this_program = program_stack.get(stack_idx).unwrap();
            let relatives = hash_map.remove(this_program).unwrap();
            for relative in relatives {
                if !program_stack.contains(&relative) {
                    program_stack.push(relative.clone());
                }
            }
            // println!("hash_map {:?}", hash_map);
            stack_idx += 1;
        }
        no_of_groups += 1;
    }

    println!("program_stack no_of_groups {:?}", no_of_groups);
    

}
    



