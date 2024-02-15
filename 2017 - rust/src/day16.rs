use std::fs::File;
use std::io::{BufRead, BufReader};
// use std::collections::HashMap;
use std::collections::VecDeque;
use regex::Regex;

fn get_data() -> Vec<String> {
    let file = File::open("input_data.txt").unwrap();
    
    let lines: Vec<String> = BufReader::new(file)
    .lines()
    .map(|line| line.unwrap())
    .collect();
    lines
}

pub fn main() {      
    let input_data = get_data();
    let dance_moves = input_data.first().unwrap().split(",");

    let spin_regex = Regex::new(r"^s(\d+)$").unwrap();
    let exchange_regex = Regex::new(r"^x(\d+)\/(\d+)$").unwrap();
    let partner_regex = Regex::new(r"^p(.)\/(.)$").unwrap();
    
    // let mut programs: VecDeque<char> = ('a'..='e').collect();
    let mut programs: VecDeque<char> = ('a'..='p').collect();
    println!("programs {:?}", programs);

    for _i in 0..(1_000_000_000 % 30) {

        println!("{}. Program {}", _i, programs.iter().collect::<String>());
        for dance_move in dance_moves.clone() {
            if let Some(captures) = spin_regex.captures(dance_move) {
                let rotation: usize = captures[1].to_string().parse().unwrap();
                programs.rotate_right(rotation);
            } else if let Some(captures) = exchange_regex.captures(dance_move) {
                let first_idx: usize = captures[1].parse::<usize>().unwrap();
                let second_idx: usize = captures[2].parse::<usize>().unwrap();
                programs.swap(first_idx, second_idx);
                // } else if let Some(captures) = partner_regex.captures(dance_move) {
                    //     let first_idx: usize = programs.iter().position(|c| *c == captures[1].parse::<char>().unwrap()).unwrap();
                    //     let second_idx: usize = programs.iter().position(|c| *c == captures[2].parse::<char>().unwrap()).unwrap();
                    //     programs.swap(first_idx, second_idx);
                }
            }
            if programs.iter().collect::<String>() == "abcdefghijklmnop" {println!("Original state");}
    }
    println!("{}. Program {}", (1_000_000_000 % 30), programs.iter().collect::<String>());

}
