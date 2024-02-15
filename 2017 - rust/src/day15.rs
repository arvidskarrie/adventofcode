// use std::fs::File;
// use std::io::{BufRead, BufReader};
// use std::collections::{HashMap, HashSet};

const GEN_A_START: i64 = 116;
const GEN_A_FACTOR: i64 = 16807;
const GEN_B_START: i64 = 299;
const GEN_B_FACTOR: i64 = 48271;
const MOD_VALUE: i64 = (1 << 31) - 1;

#[derive(Clone, Debug)]
struct Generator {
    current_value: i64,
    factor: i64,
    mod_value_var: i64,
    acceptable_multiple: i64,
}

impl Generator {
    fn new(current_value: i64, factor: i64, mod_value_var: i64, acceptable_multiple: i64) -> Generator {
        Generator {
            current_value,
            factor,
            mod_value_var,
            acceptable_multiple,
        }
    }

    fn update_current_value(&mut self) -> i64 {
        loop {
            self.current_value = (self.current_value * self.factor) % self.mod_value_var;
            if self.current_value % self.acceptable_multiple == 0 {break;}
        }
        self.current_value
    }

    fn get_lowest_16_digits(&self) -> i64 {
        self.current_value & ((1 << 16) - 1)
    }
}

pub fn main() {
    let mut generator_a = Generator::new(GEN_A_START, GEN_A_FACTOR, MOD_VALUE, 4);
    let mut generator_b = Generator::new(GEN_B_START, GEN_B_FACTOR, MOD_VALUE, 8);

    let mut total_no_of_matches = 0;
    let upper_limit: i32 = 5000000;
    for _i in 0..upper_limit {
        generator_a.update_current_value();
        generator_b.update_current_value();
        if generator_a.get_lowest_16_digits() == generator_b.get_lowest_16_digits() {
            total_no_of_matches += 1;
        }
    }
    println!("total_no_of_matches {}", total_no_of_matches);
}
