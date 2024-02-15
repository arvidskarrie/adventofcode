use core::panic;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;

use regex::Regex;

fn get_data() -> Vec<String> {
    let file = File::open("input_data.txt").unwrap();
    
    let lines: Vec<String> = BufReader::new(file)
    .lines()
    .map(|line| line.unwrap())
    .collect();
    lines
}

fn get_start_state(line: String) -> char {
    if let Some(captures) = Regex::new(r"Begin in state (.).").unwrap().captures(&line) {
        return captures[1].chars().next().expect("Start state should be one char");
    }

    panic!("No start state found");
}

fn get_no_of_steps(line: String) -> i32 {
    if let Some(captures) = Regex::new(r"Perform a diagnostic checksum after (\d+) steps.").unwrap().captures(&line) {
        let value_i64 = captures[1].parse::<i64>().expect("steps should be parsable");
        if value_i64 > i32::MAX as i64 {panic!("Steps is to large for i32");}
        return value_i64 as i32;
    }
    panic!("No start state found");
}

#[derive(Debug, Clone, Copy)]
struct State {
    if_0_write: i32,
    if_0_step_right: bool,
    if_0_go_to: char,
    if_1_write: i32,
    if_1_step_right: bool,
    if_1_go_to: char,
}

impl State {
    fn new(data_vec: Vec<&str>) -> State {
        let first_step_char = data_vec[3].chars().next().expect("expect first char");
        let second_step_char = data_vec[7].chars().next().expect("expect first char");
        assert!(first_step_char == 'r' || first_step_char == 'l');
        assert!(second_step_char == 'r' || second_step_char == 'l');

        State {
            if_0_write: data_vec[2].parse::<i32>().expect("expect i32"),
            if_0_step_right: first_step_char == 'r',
            if_0_go_to: data_vec[4].chars().next().expect("expect char"),
            if_1_write: data_vec[6].parse::<i32>().expect("expect i32"),
            if_1_step_right: second_step_char == 'r',
            if_1_go_to: data_vec[8].chars().next().expect("expect char"),
        }
    }
    
}
pub fn main() {      
    let mut input_data = get_data();
    let start_state = get_start_state(input_data.remove(0));
    let required_steps = get_no_of_steps(input_data.remove(0));
    assert!(input_data.remove(0).is_empty());
    // Extract all info from the data

    let mut state_map = HashMap::<char, State>::new();
    for line in input_data
    {
        let split_line = line.split_whitespace().collect::<Vec<_>>();
        println!("line {}", line);
        assert!(split_line[1] == "0");
        assert!(split_line[5] == "1");
        let name = split_line[0].chars().next().expect("state name");
        let state = State::new(split_line);

        state_map.insert(name, state);
    }

    let mut data_map = HashMap::<i32, i32>::new();
    let mut current_idx = 0;
    let mut current_state: State = state_map.get(&start_state).expect("Start state should exist").clone();
    for _ in 0..required_steps {
        let curr_data = data_map.entry(current_idx).or_default();
        if *curr_data == 0 {
            *curr_data = current_state.if_0_write;
            current_idx += if current_state.if_0_step_right {1} else {-1};
            current_state = state_map.get(&current_state.if_0_go_to).expect("new state should exist").clone();
        } else {
            *curr_data = current_state.if_1_write;
            current_idx += if current_state.if_1_step_right {1} else {-1};
            current_state = state_map.get(&current_state.if_1_go_to).expect("new state should exist").clone();
        }
    }

    println!("{:?}", data_map);
    println!("Number of 1s = {}", data_map.iter().filter(|(k, v)| **v == 1).collect::<Vec<_>>().len());
}