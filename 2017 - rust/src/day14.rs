use std::fs::File;
use std::io::{BufRead, BufReader};
// use std::collections::HashMap;
use std::collections::VecDeque;

fn get_data() -> Vec<String> {
    let file = File::open("input_data.txt").unwrap();
    
    let lines: Vec<String> = BufReader::new(file)
    .lines()
    .map(|line| line.unwrap())
    .collect();
lines
}

fn rotate_knot(knot: &mut VecDeque<usize>, n: usize) {
    for _ in 0..n {
        if let Some(item) = knot
        .pop_front() {
            knot
            .push_back(item);
    }
}
}

fn get_neighbours(coord: (usize, usize)) -> Vec<(usize, usize)> {
    let (x, y) = coord;
    let mut neighbours = Vec::new();

    neighbours.push((x + 1, y));
    neighbours.push((x.wrapping_sub(1), y));
    neighbours.push((x, y + 1));
    neighbours.push((x, y.wrapping_sub(1)));
    
    neighbours
}

fn find_first_true(matrix: &[Vec<bool>]) -> Option<(usize, usize)> {
    for (row_index, row) in matrix.iter().enumerate() {
        if let Some(col_index) = row.iter().position(|&val| val) {
            return Some((col_index, row_index));
        }
    }
    None
}

fn main() {      
    let word_input = get_data().first().unwrap().clone();
    let forced_input: &[usize] = &[17, 31, 73, 47, 23];

    let mut no_of_ones = 0;
    let mut matrix: Vec<Vec<bool>> = Vec::new();

    // Create 128 hash knots with a slight addition to the seed string every time
    for i in 0..128 {
        let this_word_input = format!("{}-{}", word_input, i);
        let mut ascii_input: Vec<usize> = this_word_input.chars().map(|c| c as usize).collect();
        ascii_input.extend(forced_input);

        let data_length = 256 as usize;
        let mut knot: VecDeque<usize> = (0..data_length).collect();
        let mut total_rotations = 0;
        let mut skip = 0;

        for _round in 0..64 {
            for rotate_range in ascii_input.clone() {
                // drain a list of elements, reverse them and reinsert them
                let mut vec_to_be_reverse: Vec<usize> = knot.drain(0..rotate_range).collect();
                vec_to_be_reverse.reverse();
                let mut reversed_vecdeque: VecDeque<usize> = vec_to_be_reverse.iter().map(|v| *v).collect();
                knot.append(&mut reversed_vecdeque);

                // Rotate knot to reflect the new current position
                // We have effectively already rotated the range, so only the skip length remains
                rotate_knot(&mut knot, skip);
                total_rotations += rotate_range + skip;
                total_rotations %= data_length;
                skip += 1;
            }
        }

        // Restore the original rotation
        rotate_knot(&mut knot, data_length - total_rotations);
        
        // Convert the new values not to a hash but to binary string
        let mut binary_string = String::new();
        while !knot.is_empty() {
            let numbers = knot.drain(0..16);
            let mut dense_hash = 0;
            for num in numbers {
                dense_hash ^= num; 
            }
            binary_string.push_str(&format!("{:08b}", dense_hash));
        }
        // println!("hash {}", binary_string);
        assert!(binary_string.len() == 128);
        // Count the number of 1's in the string
        no_of_ones += binary_string.chars().filter(|c| *c == '1').collect::<String>().len();
        matrix.push(binary_string.chars().map(|c| c == '1').collect::<Vec<bool>>());
    }

    println!("Number of ones {}", no_of_ones);

    assert!(matrix.len() == 128);
    assert!(matrix[0].len() == 128);

    let mut no_of_groups = 0;

    while let Some(seed_coord) = find_first_true(&matrix)
    {
        let mut this_region = Vec::from([seed_coord]);
        let mut stack_idx = 0;

        while stack_idx < this_region.len() {
            for (x_n, y_n) in get_neighbours(this_region[stack_idx]) {
                // get_neighbours will do the filtering needed
                if let Some(line) = matrix.get(y_n) {
                    if let Some(true) = line.get(x_n) {
                        if !this_region.contains(&(x_n, y_n)) {
                            this_region.push((x_n, y_n));
                        }
                    }
                }
            }

            stack_idx += 1;
        }
        no_of_groups += 1;
        
        // Remove the region from the matrix
        for (x, y) in this_region {
            matrix[y][x] = false;
        }
    }

    println!("No of groups {}", no_of_groups); // 1069
}

