use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;
use regex::Regex;

fn get_data() -> Vec<String> {
    let file = File::open("input_data.txt").unwrap();
    
    let lines: Vec<String> = BufReader::new(file)
    .lines()
    .map(|line| line.unwrap())
    .collect();
    lines
}

struct SoundMachine {
    program_id: i64,
    operations: Vec<String>,
    sound_map: HashMap<char, i64>,
    idx: i64,
}

impl SoundMachine {
    fn new(program_id: i64, operations: Vec<String>) -> SoundMachine {
        SoundMachine {
            program_id,
            operations,
            sound_map: HashMap::from([('p', program_id)]),
            idx: 0,
        }
    }
    
    fn continue_operations(&mut self, mut received_values: Vec<i64>) -> Vec<i64> {
        let mut sent_values: Vec<i64> = Vec::new();

        let snd_regex = Regex::new(r"^snd (.*)$").unwrap();
        let set_regex = Regex::new(r"^set (.) (.*)$").unwrap();
        let add_regex = Regex::new(r"^add (.) (.*)$").unwrap();
        let mul_regex = Regex::new(r"^mul (.) (.*)$").unwrap();
        let mod_regex = Regex::new(r"^mod (.) (.*)$").unwrap();
        let rcv_regex = Regex::new(r"^rcv (.)$").unwrap();
        let jgz_regex = Regex::new(r"^jgz (.) (.*)$").unwrap();
        
        while self.idx < self.operations.len() as i64 {
            let op = &self.operations[self.idx as usize];
            // println!("This op '{}'", op);
            if let Some(captures) = snd_regex.captures(&op) {
                if let Ok(int_value) = captures[1].parse::<i64>() {
                    sent_values.push(int_value);
                } else if let Ok(char_value) = captures[1].parse::<char>() {
                    sent_values.push(*self.sound_map.entry(char_value).or_default());
                }
            } else if let Some(captures) = set_regex.captures(&op) {
                let char_idx_value = captures[1].chars().next().expect("Capture group 1 is empty");
                let value = if let Ok(int_value) = captures[2].parse::<i64>() {
                    int_value
                } else if let Some(&existing_value) = captures[2].chars().next().and_then(|c| self.sound_map.get(&c)) {
                    existing_value
                } else {
                    0
                };
                self.sound_map.insert(char_idx_value, value);       
            } else if let Some(captures) = add_regex.captures(&op) {
                let char_idx_value = captures[1].chars().next().expect("Capture group 1 is empty");
                let value = if let Ok(int_value) = captures[2].parse::<i64>() {
                    int_value
                } else if let Some(&value) = captures[2].chars().next().and_then(|c| self.sound_map.get(&c)) {
                    value
                } else {
                    continue;
                };
                *self.sound_map.entry(char_idx_value).or_default() += value;        
            } else if let Some(captures) = mul_regex.captures(&op) {
                let char_idx_value = captures[1].chars().next().expect("Capture group 1 is empty");
                if let Ok(int_value) = captures[2].parse::<i64>() {
                    *self.sound_map.entry(char_idx_value).or_default() *= int_value;
                } else if let Ok(char_value) = captures[2].parse::<char>() {
                    let value = self.sound_map.entry(char_value).or_default().clone();
                    *self.sound_map.entry(char_idx_value).or_default() *= value;
                }
            } else if let Some(captures) = mod_regex.captures(&op) {
                let char_idx_value = captures[1].chars().next().expect("Capture group 1 is empty");
                if let Ok(int_value) = captures[2].parse::<i64>() {
                    *self.sound_map.entry(char_idx_value).or_default() %= int_value;
                } else if let Ok(char_value) = captures[2].parse::<char>() {
                    let value = self.sound_map.entry(char_value).or_default().clone();
                    *self.sound_map.entry(char_idx_value).or_default() %= value;
                }
            } else if let Some(captures) = rcv_regex.captures(&op) {
                // println!("Triggered receive with idx {}, received {:?}, id {}", self.idx, received_values, self.program_id);
                if received_values.is_empty()
                {
                    // We require more values from other generator
                    return sent_values;
                } else {
                    let next_received_value = received_values.remove(0);

                    // use like set
                    let char_idx_value = captures[1].chars().next().expect("Capture group 1 is empty");
                    self.sound_map.insert(char_idx_value, next_received_value);       
                }
            } else if let Some(captures) = jgz_regex.captures(&op) {
                let decider_value = if let Ok(int_decider_value) = captures[1].parse::<i64>() {
                    int_decider_value
                } else if let Ok(char_idx_value) = captures[1].parse::<char>() {
                    *self.sound_map.entry(char_idx_value).or_default()
                } else {
                    panic!("Fail to interpret jnz");
                };

                // let char_idx_value = captures[1].chars().next().expect("Capture group 1 is empty");
                // if *self.sound_map.entry(char_idx_value).or_default() <= 0 {} else {
                if decider_value > 0 {
                    if let Ok(int_value) = captures[2].parse::<i64>() {
                        self.idx += int_value;
                    } else if let Ok(char_value) = captures[2].parse::<char>() {
                        let value = self.sound_map.entry(char_value).or_default().clone();
                        self.idx += value;
                    }
                    self.idx -= 1 // compensate for +1 later
                }
            } else {
                println!("Doesn't recognize op '{}'", op);
            }
            // println!("id {}, received {:?}, sent_values {:?}", self.program_id, received_values, sent_values);
            // println!("self.sound_map {:?}, sent_values {:?}", self.sound_map, sent_values);
        
            self.idx += 1;
        }

        panic!("No more operations");
    }
}

// Grundiden är att låta sm a köra på tills den behöver ett värde från sm b. Då triggar den sm_b.continue_processing(värden från a); eller liknande.
// När b sen behöver fler värden från a än den har så returnerar den. Nästa gång a triggar b så är det viktigt att b kör om den rad som inte kördes sist,
// men det kan nog göras genom att inte räkna upp indexet. Programmen slutar när b behöver ett värde från a utan att själv ha skapat något, eller tvärtom.

pub fn main() {      
    let input_data = get_data();
    
    let mut sm_a = SoundMachine::new(0, input_data.clone());
    let mut sm_b = SoundMachine::new(1, input_data);

    let mut values_from_b: Vec<i64> = Vec::new();
    let mut values_from_a: Vec<i64> = Vec::new();

    let mut total_sent_from_b = 0;
    
    loop {
        values_from_a = sm_a.continue_operations(values_from_b);
        println!("values_from_a {:?}", values_from_a.len());
        if values_from_a.len() == 0 {break;}
        values_from_b = sm_b.continue_operations(values_from_a);
        println!("values_from_b {:?}", values_from_b.len());
        total_sent_from_b += values_from_b.len();
        if values_from_b.len() == 0 {break;}
    }
    println!("total_sent_from_b {}", total_sent_from_b);
}
