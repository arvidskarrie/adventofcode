use itertools::Itertools;
use regex::Regex;
use std::cell::RefCell;
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::process::exit;
use std::rc::{Rc, Weak};

fn get_data() -> Vec<String> {
    let file = File::open("input_data.txt").unwrap();

    let lines: Vec<String> = BufReader::new(file)
        .lines()
        .map(|line| line.unwrap())
        .collect();
    lines
}

fn get_outlier(towers: &[Rc<RefCell<Tower>>]) -> Option<usize> {
    let correct_weight = if towers[0].borrow_mut().get_iterative_weight()
        == towers[1].borrow_mut().get_iterative_weight()
    {
        towers[0].borrow_mut().get_iterative_weight()
    } else {
        towers[2].borrow_mut().get_iterative_weight()
    };

    match towers.iter().position(|tower| tower.borrow_mut().get_iterative_weight() != correct_weight) {
        Some(wrong_tower_idx) => {
            let tower = towers[wrong_tower_idx].borrow();
            println!(
                "Found an outlier, correct weight should be {}, but {} has weight {}",
                correct_weight,
                tower.name,
                tower.iterative_weight
            );
            println!(
                "To correct this, the iterative weight needs to be increased {}",
                correct_weight - tower.iterative_weight
            );
            println!(
                "This would make {}s weight {}",
                tower.name,
                tower.own_weight + correct_weight - tower.iterative_weight
            );
            Some(wrong_tower_idx)
        }
        None => None
    }
}

#[derive(Clone, Debug)]
struct Tower {
    name: String,
    own_weight: i32,
    iterative_weight: i32,
    children: Vec<Rc<RefCell<Tower>>>,
    parent: Option<Weak<RefCell<Tower>>>,
}

impl Tower {
    fn new(name: String, own_weight: i32) -> Tower {
        Tower {
            name,
            own_weight,
            iterative_weight: 0,
            children: Vec::new(),
            parent: None,
        }
    }

    fn set_own_weight(&mut self, own_weight: i32) {
        self.own_weight = own_weight;
    }

    fn add_child(&mut self, child: Rc<RefCell<Tower>>) {
        self.children.push(child);
    }

    fn set_parent(&mut self, parent: Rc<RefCell<Tower>>) {
        self.parent = Some(Rc::downgrade(&parent));
    }

    fn get_parent(&self) -> Option<Weak<RefCell<Tower>>> {
        self.parent.clone()
    }

    fn get_iterative_weight(&mut self) -> i32 {
        if self.iterative_weight == 0 {
            self.iterative_weight = self.own_weight;
            for child in &self.children {
                let mut child = child.borrow_mut();
                self.iterative_weight += child.get_iterative_weight();
            }
        }
        self.iterative_weight
    }

    fn get_is_balanced(&self) -> bool {
        match self.children.len() {
            0 => true,
            1 => self.children[0].borrow().get_is_balanced(),
            2 => {
                self.children[0].borrow_mut().get_iterative_weight()
                    == self.children[1].borrow_mut().get_iterative_weight()
                    || (self.children[0].borrow().get_is_balanced()
                        && self.children[1].borrow().get_is_balanced())
            }
            _ => {
                if let Some(outlier_idx) = get_outlier(&self.children) {
                    let outlier_tower = self.children[outlier_idx].clone();
                    if outlier_tower.borrow().get_is_balanced() {
                        println!("Found the error in {}", outlier_tower.borrow().name);
                        exit(0);
                    }
                    return false;
                }
                return true;
            }
        }
    }
}

pub fn main() {
    let input_data = get_data();

    let regex_variable = Regex::new(r"^(\w+) \((\d+)\)( -> (.+))?$").unwrap();
    let mut towers: HashMap<String, Rc<RefCell<Tower>>> = HashMap::new();

    for line in input_data.iter() {
        match regex_variable.captures(line) {
            Some(captures) => {
                let own_weight: i32 = (&captures[2]).parse().unwrap();
                let name = (&captures[1]).to_string();

                // If the tower does not exist in the list, add it
                let this_tower_reference = towers
                    .entry(name.clone())
                    .or_insert_with(|| Rc::new(RefCell::new(Tower::new(name.clone(), own_weight))))
                    .clone();

                this_tower_reference.borrow_mut().set_own_weight(own_weight);

                if let Some(children) = captures.get(4) {
                    // If the object has children, create them if needed.
                    let childrens_name = children.as_str().split(", ");

                    for child_name in childrens_name {
                        let child_name = child_name.to_string();
                        let child_tower = towers.entry(child_name.clone()).or_insert_with(|| {
                            Rc::new(RefCell::new(Tower::new(child_name.clone(), 0)))
                        });

                        // Add a reference to the children in this_tower.
                        child_tower
                            .borrow_mut()
                            .set_parent(this_tower_reference.clone());
                        // Add a parent reference to all children
                        this_tower_reference
                            .borrow_mut()
                            .add_child(child_tower.clone());
                    }
                }
            }
            None => panic!(),
        }
    }

    let (top_tower_name, _) = towers
        .iter()
        .filter(|(_, v)| v.borrow().get_parent().is_none())
        .next()
        .unwrap()
        .clone();
    println!("top_tower_name {}", top_tower_name);

    let mut top_tower = towers
        .get(top_tower_name)
        .expect("Top tower should exist")
        .borrow_mut();

    // At this step, at the end of part 1, we have a map with all objects but with wtring references.
    // We will now create a new list starting from the top tower name, and create a proper tree.
    top_tower.get_is_balanced();
    println!("top_tower weight {}", top_tower.iterative_weight);
    // get_is_balanced(&top_tower);
}
