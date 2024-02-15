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

// fn main() {      
//     let input_data = get_data();
//     let int_input: Vec<usize> = input_data.first().unwrap().split(",").map(|s| s.parse().unwrap()).collect();

//     println!("input {:?}", int_input);
    
//     let data_length = 256 as usize;
//     let mut knot: VecDeque<usize> = (0..data_length).collect();
//     let mut total_rotations = 0;

//     println!("knot {:?}", knot);
//     for (skip, rotate_range) in int_input.iter().enumerate() {
//         // drain a list of elements, reverse them and reinsert them
//         println!("rotate_range {:?}", rotate_range);
//         let mut vec_to_be_reverse: Vec<usize> = knot.drain(0..*rotate_range).collect();
//         vec_to_be_reverse.reverse();
//         let mut reversed_vecdeque: VecDeque<usize> = vec_to_be_reverse.iter().map(|v| *v).collect();
//         knot.append(&mut reversed_vecdeque);
//         println!("\tknot after reverse {:?}", knot);

//         // Rotate knot to reflect the new current position
//         // We have effectively already rotated the range, so only the skip length remains
//         rotate_knot(&mut knot, skip);
//         total_rotations += *rotate_range + skip;
//         total_rotations %= data_length;
//         println!("\tknot after rotate {:?}, total_rotations {}", knot, total_rotations);
//     }

//     // Restore the original rotation
//     rotate_knot(&mut knot, data_length - total_rotations);
//     println!("\tknot after last rotate {:?}", knot);
// }


fn main() {      
    let input_data = get_data();
    let mut ascii_input: Vec<usize> = input_data.first().unwrap().chars().map(|c| c as usize).collect();
    let mut forced_input: Vec<usize> = Vec::from([17, 31, 73, 47, 23]);
    ascii_input.append(&mut forced_input);

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
    println!("\tknot after last rotate {:?}", knot);

    // Go through every 16 numbers and add to the hex_string
    let mut hex_string = String::new();
    while !knot.is_empty() {
        let numbers = knot.drain(0..16);
        let mut dense_hash = 0;
        for num in numbers {
            dense_hash ^= num; 
        }
        hex_string.push_str(&format!("{:02x}", dense_hash));
    }
    println!("hash {}", hex_string);
}


