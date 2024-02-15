
// part a
// fn main() {
//     let numbers: Vec<i32> = vec![1, 12, 23, 1024, 325489];
//     // let numbers = 2..40;

//     for i in numbers {
//         if i == 1 {continue;}
//         let mut rad: i32 = (i as f64).sqrt().ceil() as i32;
//         if rad % 2 == 0 {rad += 1;}

//         let rad_max = rad * rad;
//         let min_val = (rad - 1) / 2;
//         let mod_val = rad - 1;

//         let x = rad_max - (rad_max - i) % mod_val;        
//         let diff_from_min = (rad_max - mod_val / 2 - x).abs();
//         let min_distance = min_val + diff_from_min;
        
//         println!("{} min_distance {}", i, min_distance);
//     }
// }

use std::collections::HashMap;

fn get_neighbours(coord: (i32, i32)) -> Vec<(i32, i32)> {
    let (x, y) = coord;
    let mut neighbours = Vec::new();

    for dx in -1..=1 {
        for dy in -1..=1 {
            if dx == 0 && dy == 0 {
                continue; // Skip the input cell itself
            }
            neighbours.push((x + dx, y + dy));
        }
    }

    neighbours
}

fn get_next_coord(current_coord: (i32, i32), coordinates: &HashMap<(i32, i32), i32>) -> (i32, i32) {
    let (x, y) = current_coord;
    if coordinates.contains_key(&(x-1, y)) && !coordinates.contains_key(&(x, y+1)) {
        return (x, y+1);
    }
    if coordinates.contains_key(&(x, y-1)) && !coordinates.contains_key(&(x-1, y)) {
        return (x-1, y);
    }
    if coordinates.contains_key(&(x+1, y)) && !coordinates.contains_key(&(x, y-1)) {
        return (x, y-1);
    }
    if coordinates.contains_key(&(x, y+1)) && !coordinates.contains_key(&(x+1, y)) {
        return (x+1, y);
    }

    panic!("No direction available");
}

// part b
// fn main() {
//     let target = 325489;
//     let mut coordinates: HashMap<(i32, i32), i32> = HashMap::new();

//     coordinates.insert((0, 0), 1);
//     coordinates.insert((1, 0), 1);

//     let mut current_coord = (1, 0);
    
//     for i in 3..  {
//         current_coord = get_next_coord(current_coord, &coordinates);
        
//         let mut neighbours_sum = 0;
        
//         for nb in get_neighbours(current_coord) {
//             if let Some(value) = coordinates.get(&nb) {
//                 neighbours_sum += value
//             }
//         }

//         println!("i {} current coord {:?} sum {}", i, current_coord, neighbours_sum);

//         if neighbours_sum > target {break;}
//         coordinates.insert(current_coord, neighbours_sum);
//     }
// }

// part a 2
fn main() {
    let target = 325489;
    let mut coordinates: HashMap<(i32, i32), i32> = HashMap::new();

    coordinates.insert((0, 0), 1);
    coordinates.insert((1, 0), 1);

    let mut current_coord = (1, 0);
    
    for i in 3..(330785 + 1)  {
        current_coord = get_next_coord(current_coord, &coordinates);

        if i > target {break;}
        coordinates.insert(current_coord, i);
    }
    let (x, y) = current_coord;
    println!("sum {}", x.abs() + y.abs())
}
