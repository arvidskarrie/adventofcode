use std::fs::File;
use std::io::{BufRead, BufReader};
use num_complex::Complex;


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
    let mut input_chars = input_data.iter().map(|line| line.chars().collect::<Vec<char>>()).collect::<Vec<Vec<char>>>();
    input_chars.reverse(); // To not flip im axis
    let mut word = String::new();
    
    let start_x = input_chars.last().unwrap().iter().position(|c| *c == '|').unwrap();
    let mut curr_pos = Complex::new(start_x as i32, (input_chars.len() - 1) as i32);
    let mut curr_dir = Complex::new(0, -1); // down

    println!("start_x {}, curr_pos {}, curr_dir {}, input len {:?}", start_x, curr_pos, curr_dir, (input_chars.len(), input_chars[0].len()));
    // return;
    
    for step in 1.. {
        let new_pos = curr_dir + curr_pos;
        let new_char = input_chars[new_pos.im as usize][new_pos.re as usize];
        
        match new_char {
            ' ' => {
                println!("End of road at {}, steps taken {}", new_pos, step);
                break;
            },
            '|' | '-' => {
            },
            '+' => {
                // Find if I can turn left, otherwise turn right
                let right_turn_pos = new_pos + Complex::new(0, -1) * curr_dir;
                let left_turn_pos = new_pos + Complex::new(0, 1) * curr_dir;
                if input_chars[right_turn_pos.im as usize][right_turn_pos.re as usize] != ' ' {
                    // Make a right turn
                    curr_dir *= Complex::new(0, -1);
                } else if input_chars[left_turn_pos.im as usize][left_turn_pos.re as usize] != ' ' {
                    // Make a left turn
                    curr_dir *= Complex::new(0, 1);
                } else {
                    println!("No turn found char {} at {}", new_char, new_pos);
                    break;
                }
            },
            'A'..='Z' => {
                // Add letter
                word.push(new_char);
            }
            _ => {
                println!("Unknown char {} at {}", new_char, new_pos);
                break;
            }
        }
        curr_pos = new_pos;

    }

    println!("Word {}", word); // AYRPVMEGQ
}
