use core::panic;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;

fn get_data() -> Vec<String> {
    let file = File::open("input_data.txt").unwrap();
    
    let lines: Vec<String> = BufReader::new(file)
    .lines()
    .map(|line| line.unwrap())
    .collect();
    lines
}

struct SoundMachine {
    operations: Vec<String>,
    sound_map: HashMap<char, i64>,
    idx: i64,
}

impl SoundMachine {
    fn new(operations: Vec<String>) -> SoundMachine {
        SoundMachine {
            operations,
            sound_map: HashMap::new(),
            idx: 0,
        }
    }
    
    fn continue_operations(&mut self) -> i64 {

        let set_regex = Regex::new(r"^set (.) (.*)$").unwrap();
        let sub_regex = Regex::new(r"^sub (.) (.*)$").unwrap();
        let mul_regex = Regex::new(r"^mul (.) (.*)$").unwrap();
        let jnz_regex = Regex::new(r"^jnz (.) (.*)$").unwrap();

        self.sound_map.insert('a', 1);
        self.sound_map.insert('b', 0);
        self.sound_map.insert('c', 0);
        self.sound_map.insert('d', 0);
        self.sound_map.insert('e', 0);
        self.sound_map.insert('f', 0);
        self.sound_map.insert('g', 0);
        self.sound_map.insert('h', 0);
        
        while self.idx < self.operations.len() as i64  && self.idx >= 0 {
            let op = &self.operations[self.idx as usize];
            // println!("This op {}: {}", self.idx, op);

            // We need to make som shortcuts:
            // if we have jumped to idx 11 = set g d and e is neither b/2 or b-1, the only thing happening is that e increases.
            // Therefore make a shortcut to that point
            if self.idx == 11 {
                let b_entry = self.sound_map.entry('b').or_insert(0).clone();
                let e_entry = self.sound_map.entry('e').or_insert(0);
                
                if b_entry != 108400 {
                    println!("State when idx {}: {:?}", self.idx, self.sound_map);

                    panic!("b value changed")
                }
                if *e_entry < b_entry / 2 && b_entry % 2 == 0{
                    *e_entry = b_entry / 2;
                } else if *e_entry < b_entry  - 1 {
                    *e_entry = b_entry - 1;
                }
            }

            // if we have jumped to idx 20 = sub d -1 and d is not just below b, we will just do the same thing again. Shortcut to d = b-1
            if self.idx == 20 {
                let b_entry = self.sound_map.entry('b').or_insert(0).clone();
                let d_entry = self.sound_map.entry('d').or_insert(0);
                
                if *d_entry < b_entry - 1 {
                    *d_entry = b_entry - 1;
                }
            }

            if self.idx >= 20 {
                let mut output = String::new();
                for key in 'a'..='h' {
                    let value = self.sound_map.get(&key).unwrap();
                    output.push_str(&format!("{}: {:>10}\t", key, value));
                }
                println!("State when idx {}: {}", self.idx, output.trim_end());
            }

            if let Some(captures) = set_regex.captures(&op) {
                let char_idx_value = captures[1].chars().next().expect("Capture group 1 is empty");
                let value = if let Ok(int_value) = captures[2].parse::<i64>() {
                    int_value
                } else if let Some(&existing_value) = captures[2].chars().next().and_then(|c| self.sound_map.get(&c)) {
                    existing_value
                } else {
                    0
                };
                self.sound_map.insert(char_idx_value, value);    
            } else if let Some(captures) = sub_regex.captures(&op) {
                let char_idx_value = captures[1].chars().next().expect("Capture group 1 is empty");
                let value = if let Ok(int_value) = captures[2].parse::<i64>() {
                    int_value
                } else if let Some(&value) = captures[2].chars().next().and_then(|c| self.sound_map.get(&c)) {
                    value
                } else {
                    continue;
                };
                *self.sound_map.entry(char_idx_value).or_default() -= value;        
            } else if let Some(captures) = mul_regex.captures(&op) {
                let char_idx_value = captures[1].chars().next().expect("Capture group 1 is empty");
                if let Ok(int_value) = captures[2].parse::<i64>() {
                    *self.sound_map.entry(char_idx_value).or_default() *= int_value;
                } else if let Ok(char_value) = captures[2].parse::<char>() {
                    let value = self.sound_map.entry(char_value).or_default().clone();
                    *self.sound_map.entry(char_idx_value).or_default() *= value;
                }
            } else if let Some(captures) = jnz_regex.captures(&op) {
                // The first value can be either a char or an index
                let decider_value = if let Ok(int_decider_value) = captures[1].parse::<i64>() {
                    int_decider_value
                } else if let Ok(char_idx_value) = captures[1].parse::<char>() {
                    *self.sound_map.entry(char_idx_value).or_default()
                } else {
                    panic!("Fail to interpret jnz");
                };

                if decider_value != 0 {
                    if let Ok(int_value) = captures[2].parse::<i64>() {
                        self.idx += int_value;
                    } else if let Ok(char_value) = captures[2].parse::<char>() {
                        let value = self.sound_map.entry(char_value).or_default().clone();
                        self.idx += value;
                    }
                    self.idx -= 1 // comppensate for +1 later
                }
            } else {
                println!("Doesn't recognize op '{}'", op);
            }
        
            self.idx += 1;
        }

        return self.sound_map[&'h'];
    }
}

// Grundiden är att låta sm a köra på tills den behöver ett värde från sm b. Då triggar den sm_b.continue_processing(värden från a); eller liknande.
// När b sen behöver fler värden från a än den har så returnerar den. Nästa gång a triggar b så är det viktigt att b kör om den rad som inte kördes sist,
// men det kan nog göras genom att inte räkna upp indexet. Programmen slutar när b behöver ett värde från a utan att själv ha skapat något, eller tvärtom.

pub fn main() {      
    let input_data = get_data();
    let mut sm_a = SoundMachine::new(input_data);

    println!("Value in register h {}", sm_a.continue_operations()); // 6724
}
