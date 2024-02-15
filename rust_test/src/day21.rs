use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::{vec, iter};

// use itertools::Itertools;

fn get_data() -> Vec<String> {
    let file = File::open("input_data.txt").unwrap();

    let lines: Vec<String> = BufReader::new(file)
        .lines()
        .map(|line| line.unwrap())
        .collect();
    lines
}

fn flip_vert(art: &str) -> String {
    let art_side_length = (art.len() as f64).sqrt() as usize;
    let mut new_art: Vec<&str> = split_string_every_n_chars(&art, art_side_length);
    new_art.reverse();
    return new_art.join("");
}

fn rotate90(art: &str) -> String {
    let size = (art.len() as f64).sqrt() as usize;
    let rows: Vec<&str> = split_string_every_n_chars(&art, size);
    let mut new_rows = vec![String::new(); size];
    
    for i in 0..size {
        for row in &rows {
            new_rows[i].push(row.chars().nth(size - 1 - i).unwrap());
        }
    }
    
    new_rows.join("")
}

fn evolve_art<'a>(art: &str, conv_map: &'a HashMap<String, String>) -> &'a str {
    let mut art = art.to_string();

    for _ in 0..4 {
        if conv_map.contains_key(&art) {
            return &conv_map[&art];
        }
        art = flip_vert(&art);
        if conv_map.contains_key(&art) {
            return &conv_map[&art];
        }
        art = flip_vert(&art);
        art = rotate90(&art);
    }
    
    panic!("No art conversion found");
}

fn split_string_every_n_chars(s: &str, n: usize) -> Vec<&str> {
    s.as_bytes()
     .chunks(n)
     .map(|chunk| std::str::from_utf8(chunk).unwrap())
     .collect()
}

pub fn main() {
    let input_data = get_data();
    let mut art: String = ".#...####".to_string();
    
    // Create a map for art conversions
    let mut art_conversion: HashMap<String, String> = HashMap::<String, String>::new();
    for line in input_data {
        let split_line = line.split(" => ").collect::<Vec<_>>();
        art_conversion.insert(split_line[0].to_string(), split_line[1].to_string());
    }
    
    for i in 0..18 {
        // art represents a matrix of chars without delimiters
        let base_number = if art.len() % 4 == 0 {2} else {3};
        let new_base = base_number + 1;
        
        let art_side_length = (art.len() as f64).sqrt() as usize;
        let split_art: Vec<&str> = split_string_every_n_chars(&art, art_side_length);
        let no_of_art_squares = art_side_length / base_number;
        let mut new_split_art: Vec<String> = vec!(String::with_capacity(art_side_length * new_base); (base_number + 1) * no_of_art_squares);

        for row in 0..no_of_art_squares {
            for columns in 0..no_of_art_squares {
                let col: usize = columns * base_number;
                
                let row_base = row * base_number;
                let col_end = col + base_number - 1;
                let mut square = String::with_capacity(base_number * (base_number + 1));
                for r in row_base..(row_base + base_number) {
                    square.push_str(&split_art[r][col..=col_end]);
                }                

                let evolved_art: &str = evolve_art(&square, &art_conversion);
                for j in 0..=base_number {
                    new_split_art[row * new_base + j].push_str(&evolved_art[(j * new_base)..((j + 1) * new_base)]);
                }
            }
        }
        art = new_split_art.join("");

        println!("Number of pixels after iteration {} = {}", i, art.chars().filter(|c| *c == '#').count()); // 18: 3389823

    }
}


