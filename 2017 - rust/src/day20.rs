use regex::{Captures, Regex};
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn get_data() -> Vec<String> {
    let file = File::open("input_data.txt").unwrap();

    let lines: Vec<String> = BufReader::new(file)
        .lines()
        .map(|line| line.unwrap())
        .collect();
    lines
}

#[derive(Debug, Eq, Hash, PartialEq, Clone, Copy)]
struct Vector3D {
    x: i32,
    y: i32,
    z: i32,
}

impl Vector3D {
    fn new(x: i32, y: i32, z: i32) -> Self {
        Vector3D { x, y, z }
    }

    fn add(&self, other: &Vector3D) -> Vector3D {
        Vector3D {
            x: self.x + other.x,
            y: self.y + other.y,
            z: self.z + other.z,
        }
    }
}

#[derive(Debug)]
struct Particle {
    position: Vector3D,
    velocity: Vector3D,
    acceleration: Vector3D,
}

impl Particle {
    fn new(position: Vector3D, velocity: Vector3D, acceleration: Vector3D) -> Self {
        Particle {
            position,
            velocity,
            acceleration,
        }
    }

    fn update_velocity(&mut self) {
        self.velocity = self.velocity.add(&self.acceleration);
    }

    fn update_position(&mut self) {
        self.position = self.position.add(&self.velocity);
    }

    fn get_position(&self) -> i32 {
        self.position.x.abs() + self.position.y.abs() + self.position.z.abs()
    }

    fn get_velocity(&self) -> i32 {
        self.velocity.x.abs() + self.velocity.y.abs() + self.velocity.z.abs()
    }

    fn get_acceleration(&self) -> i32 {
        self.acceleration.x.abs() + self.acceleration.y.abs() + self.acceleration.z.abs()
    }
}

fn Create_particle(captures: Captures) -> Particle {
    let position = Vector3D::new(
        captures[1].parse::<i32>().unwrap(),
        captures[2].parse::<i32>().unwrap(),
        captures[3].parse::<i32>().unwrap(),
    );
    let velocity = Vector3D::new(
        captures[4].parse::<i32>().unwrap(),
        captures[5].parse::<i32>().unwrap(),
        captures[6].parse::<i32>().unwrap(),
    );
    let acceleration = Vector3D::new(
        captures[7].parse::<i32>().unwrap(),
        captures[8].parse::<i32>().unwrap(),
        captures[9].parse::<i32>().unwrap(),
    );

    Particle {
        position,
        velocity,
        acceleration,
    }
}

pub fn main() {
    let input_data = get_data();
    let regex_variable =
        Regex::new(r"^p=<(.*),(.*),(.*)>, v=<(.*),(.*),(.*)>. a=<(.*),(.*),(.*)>$").unwrap();

    let mut particles = Vec::<Particle>::new();
    let mut total_removed = 0;

    for (i, line) in input_data.iter().enumerate() {
        if let Some(captures) = regex_variable.captures(&line) {
            particles.push(Create_particle(captures));
        } else {
            println!("No match for line {}", line)
        }
    }
    assert!(particles.len() == 1000);

    
    for _i in 0..1000 {
        // Find if any particles collides. This is done be adding all of them to a hashmap and if any duplicates are detected, their index is removed from the particle list.
        let mut map = HashMap::<Vector3D, usize>::new();
        let mut idx_to_remove = Vec::<usize>::new();
        for (i, part) in particles.iter().enumerate() {
            if let Some(val) = map.insert(part.position.clone(), i) {
                idx_to_remove.push(i);
                if !idx_to_remove.contains(&val) {
                    idx_to_remove.push(val);
                }
            }
        }
        
        // Remove every particle in the list
        idx_to_remove.sort_by(|a, b| b.cmp(a));
        for idx in idx_to_remove {
            particles.remove(idx);
        }
        
        for part in &mut particles {
            part.update_velocity();
            part.update_position();
        }
    }
    println!("Remaining particles {}", particles.len());
}
