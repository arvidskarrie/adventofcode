use std::collections::HashMap;
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

#[derive(PartialEq, Clone, Copy)]
enum Status {
    Clean,
    Weakened,
    Infected,
    Flagged    
}

impl Status {
    fn next(self) -> Status {
        match self {
            Status::Clean => Status::Weakened,
            Status::Weakened => Status::Infected,
            Status::Infected => Status::Flagged,
            Status::Flagged => Status::Clean,
        }
    }
}

struct Virus {
    position: Complex<i32>,
    dir: Complex<i32>,
}

impl Virus {
    fn new() -> Virus {
        Virus {
            position: Complex { re: 0, im: 0},
            dir:  Complex { re: 0, im: 1},
        }
    }

    fn turn_right(&mut self) {
        self.dir *= Complex {re: 0, im: -1};
    }

    fn turn_left(&mut self) {
        self.dir *= Complex {re: 0, im: 1};
    }

    fn turn_around(&mut self) {
        self.dir *= Complex {re: -1, im: 0};
    }

    fn step(&mut self) {
        self.position += self.dir;
    }
    
}

fn get_start_set(data: Vec<String>) -> HashMap<Complex<i32>, Status> {
    let size = data.len() as i32;
    assert_eq!(size, data[0].len() as i32, "Data is not square");

    let mut coord_set = HashMap::new();
    let center_offset = (size - 1) / 2;

    for (y_idx, line) in data.iter().enumerate() {
        for (x_idx, _) in line.chars().enumerate().filter(|(_, c)| *c == '#') {
            let x_coord = x_idx as i32 - center_offset;
            let y_coord = center_offset - y_idx as i32;
            coord_set.insert(Complex { re: x_coord, im: y_coord }, Status::Infected);
        }
    }

    coord_set
}

pub fn main() {
    let input_data = get_data();
    let mut infected_nodes = get_start_set(input_data);

    let mut virus = Virus::new();
    let mut no_of_infections_caused = 0;

    for _i in 0..10_000_000 {
        let entry = infected_nodes.entry(virus.position.clone()).or_insert(Status::Clean);

        match *entry {
            Status::Clean => virus.turn_left(),
            Status::Weakened => no_of_infections_caused += 1,
            Status::Infected => virus.turn_right(),
            Status::Flagged => virus.turn_around(),
        }
       *entry = entry.next();
        virus.step();
    }

    println!("no_of_infections_caused {}", no_of_infections_caused); // 5565
}