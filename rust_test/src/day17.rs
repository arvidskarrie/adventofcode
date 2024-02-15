use std::collections::VecDeque;

pub fn main() {      
    // let input_data = 3; //test
    let input_data = 303;

    let mut spinlock: VecDeque<i32> = VecDeque::new();
    spinlock.push_front(0);

    for i in 1..=2017 {
        spinlock.rotate_left((input_data + 1) % spinlock.len());
        spinlock.push_front(i);
    }
    println!("{}. spinlock {:?}", 2017, spinlock[1]);

    for i in 2017..=50_000_000 {
        spinlock.rotate_left((input_data + 1) % spinlock.len());
        spinlock.push_front(i);
    }

    let zeroth_idx: usize = spinlock.iter().position(|c| *c == 0).unwrap();
    println!("Index for 0 = {}, value after it = {}", zeroth_idx, spinlock[zeroth_idx + 1]);

}

// not 1222153