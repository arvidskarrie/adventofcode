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

#[derive(Debug, Clone, Copy)]
enum Comparison {
    Greater,
    Less,
    GreaterEqual,
    LessEqual,
    Equal,
    NotEqual,
}

fn str_to_comparison(s: &str) -> Comparison {
    match s {
        ">" => Comparison::Greater,
        "<" => Comparison::Less,
        ">=" => Comparison::GreaterEqual,
        "<=" => Comparison::LessEqual,
        "==" => Comparison::Equal,
        "!=" => Comparison::NotEqual,
        _ => panic!("Not known Comparison {}", s),
    }
}


#[derive(Debug)]
struct Instruction {
    object: String,
    modifier: i32,
    comp_object: String,
    comp_comparison: Comparison,
    comp_value: i32,
}

fn compare(a: &i32, b: i32, comp: Comparison) -> bool {
    match comp {
        Comparison::Greater => *a > b,
        Comparison::Less => *a < b,
        Comparison::GreaterEqual => *a >= b,
        Comparison::LessEqual => *a <= b,
        Comparison::Equal => *a == b,
        Comparison::NotEqual => *a != b,
    }
}

fn main() {      
    let input_data = get_data();
    let mut instructions: Vec<Instruction> = Vec::new();
    for line in input_data {
        let line_vec = line.split_whitespace().collect::<Vec<&str>>();
        assert!(line_vec.len() == 7);
        let modifier = line_vec[2].parse::<i32>().expect("Modifier string not parsable") * if line_vec[1] == "dec" { -1 } else {1};
        let instruction = Instruction {
            object: line_vec[0].to_string(),
            modifier,
            comp_object: line_vec[4].to_string(),
            comp_comparison: str_to_comparison(&line_vec[5]),
            comp_value: line_vec[6].parse().expect("comparison value string not parsable"),
        };
        instructions.push(instruction);
    }

    // Iterate over all instructions and add values as we go
    let mut hash_map: HashMap<String, i32> = HashMap::new();
    let mut highest_value = 0;
    for instruction in instructions {
        let comp_object_value = hash_map.get(&instruction.comp_object).map(|&value| value).unwrap_or_default();
        
        // If condition is true, make modification
        if compare(&comp_object_value, instruction.comp_value, instruction.comp_comparison) {
            // The pre-existing value should be 0 if it isn't registered already
            let new_value = hash_map.entry(instruction.object.clone()).and_modify(|v| *v += instruction.modifier).or_insert(instruction.modifier);
            // Potentially update the highest saved value
            highest_value = std::cmp::max(highest_value, *new_value)
        }
    }
    
    println!("highest value = {}", highest_value); // 6056
}

