use regex::Regex;
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::vec;

fn get_data() -> Vec<String> {
    let file = File::open("input_data.txt").unwrap();

    let lines: Vec<String> = BufReader::new(file)
        .lines()
        .map(|line| line.unwrap())
        .collect();
    lines
}

type Matrix = Vec<Vec<bool>>;

fn flip_vertical(matrix: &Matrix) -> Matrix {
    matrix.iter().rev().cloned().collect()
}

fn rotate_90(matrix: &Matrix) -> Matrix {
    let size = matrix.len();
    (0..size).map(|i| matrix.iter().rev().map(|row| row[i]).collect()).collect()
}

fn store_transformations(start_matrix: &Matrix, end_matrix: &Matrix, map: &mut HashMap<Matrix, Matrix>) {
    let mut current = start_matrix.clone();
    
    // Store all rotations
    for _ in 0..4 {
        map.insert(current.clone(), end_matrix.clone());
        current = rotate_90(&current);
    }
    
    // Flip and store all rotations of the flipped matrix
    let flipped = flip_vertical(start_matrix);
    current = flipped.clone();
    for _ in 0..4 {
        map.insert(current.clone(), end_matrix.clone());
        current = rotate_90(&current);
    }
}

fn extract_quadrants(matrix: Matrix) -> Vec<Matrix> {
    assert!(matrix.len() == 4);
    let start_points: Vec<(usize, usize)> = vec![(0, 0), (2, 0), (0, 2), (2, 2)];
    let mut return_vector = Vec::<Matrix>::new();

    for sp in start_points {
        let new_matrix: Matrix = vec!(
            vec!(matrix[0 + sp.0][0 + sp.1], matrix[0 + sp.0][1 + sp.1]),
            vec!(matrix[1 + sp.0][0 + sp.1], matrix[1 + sp.0][1 + sp.1]),
        );
        return_vector.push(new_matrix);
    }

    return return_vector;
}

fn iterate_and_count(art: Matrix, art_conversion: &HashMap<Matrix, Matrix>, transformations_left: i32) -> usize {
    if transformations_left == 0 {
        return art.into_iter().flatten().filter(|p| *p).collect::<Vec<_>>().len();
    }

    // Our alternatives are these
    // 1. We have a 2*2 that can be converted to a 3*3 and we reduce transformations_left
    // 2. We have a 3*3 that can be converted to a 4*4 and we reduce transformations_left
    // 3. We have a 4*4 that can be converted to 4 2*2s. We should iterate over these instead but not decrease transformations_left
    
    match art.len() {
        2 => {
            iterate_and_count(art_conversion.get(&art).unwrap().clone(), art_conversion, transformations_left - 1)
        },
        3 => {
            iterate_and_count(art_conversion.get(&art).unwrap().clone(), art_conversion, transformations_left - 1)
        },
        4 => {
            let mut total_sum = 0 as usize;
            for quad in extract_quadrants(art) {
                total_sum += iterate_and_count(quad, &art_conversion, transformations_left);
            }
            total_sum
        },
        _ => panic!("Art {:?} not supported", art),
    }
}

pub fn main() {
    let input_data = get_data();
    let large_regex = Regex::new(r"^(.*)/(.*)/(.*) => (.*)/(.*)/(.*)/(.*)$").unwrap();
    let small_regex = Regex::new(r"^(.*)/(.*) => (.*)/(.*)/(.*)$").unwrap();
        
    let start_art: Matrix = vec![
        vec![false, true, false],
        vec![false, false, true],
        vec![true, true, true],
    ];
    
    // Create a map for art conversion
    let mut art_conversion = HashMap::<Matrix, Matrix>::new();
    for line in input_data {
        if let Some(captures) = large_regex.captures(&line) {
            let initial_matrix: Matrix = vec![
                captures[1].chars().map(|c| c == '#').collect(),
                captures[2].chars().map(|c| c == '#').collect(),
                captures[3].chars().map(|c| c == '#').collect(),
            ];
            let result_matrix: Matrix = vec![
                captures[4].chars().map(|c| c == '#').collect(),
                captures[5].chars().map(|c| c == '#').collect(),
                captures[6].chars().map(|c| c == '#').collect(),
                captures[7].chars().map(|c| c == '#').collect(),
            ];

            store_transformations(&initial_matrix, &result_matrix, &mut art_conversion);
        } else if let Some(captures) = small_regex.captures(&line) {
                let initial_matrix: Matrix = vec![
                    captures[1].chars().map(|c| c == '#').collect(),
                    captures[2].chars().map(|c| c == '#').collect(),
                    ];
                    let result_matrix: Matrix = vec![
                    captures[3].chars().map(|c| c == '#').collect(),
                    captures[4].chars().map(|c| c == '#').collect(),
                    captures[5].chars().map(|c| c == '#').collect(),
                ];
    
                store_transformations(&initial_matrix, &result_matrix, &mut art_conversion);
        } else {
            panic!("No line match");
        }
    }
    println!("Number of trues = {}", iterate_and_count(start_art, &art_conversion, 5));
    
}