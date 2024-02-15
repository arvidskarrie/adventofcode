use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;
// use std::collections::HashSet;
use std::fmt;
use std::process::exit;
use regex::Regex;

#[derive(Clone, Debug)]
struct Tower {
    name: String,
    own_weight: i32,
    children: Vec<String>,
    parent: Option<String>,
}

impl Tower {
    fn new(name: String, own_weight: i32) -> Tower {
        Tower {
            name,
            own_weight,
            children: Vec::new(),
            parent: None,
        }
    }
    
    fn set_own_weight(&mut self, own_weight: i32) {
        self.own_weight = own_weight;
    }

    fn get_own_weight(&self) -> i32 {
        self.own_weight
    }
    
    fn set_children(&mut self, children: Vec<String>) {
        self.children = children;
    }
    
    fn get_children(&self) -> Vec<String> {
        self.children.clone()
    }

    fn set_parent(&mut self, parent: String) {
        self.parent = Some(parent);
    }
    
    fn get_parent(&self) -> Option<String> {
        self.parent.clone()
    }
}

#[derive(Clone)]
struct TowerWithRef{
    tower: Tower,
    child_references: Vec<TowerWithRef>,
    iterative_weight: i32,
}

impl TowerWithRef {
    fn new(tower: Tower) -> TowerWithRef {
        TowerWithRef {
            tower,
            child_references: Vec::new(),
            iterative_weight: 0,
        }
    }

    fn add_child(&mut self, child: TowerWithRef) {
        self.child_references.push(child);
    }
}

impl TowerWithRef {
    fn fmt_with_depth(&self, f: &mut fmt::Formatter<'_>, depth: usize) -> fmt::Result {
        write!(f, "{}TowerWithRef {{\n", " ".repeat(depth * 4))?;
        write!(f, "{}tower: {:?},\n", " ".repeat(depth * 4), self.tower)?;
        write!(f, "{}iterative_weight: {:?},\n", " ".repeat(depth * 4), self.iterative_weight)?;
        write!(f, "{}child_references: [\n", " ".repeat(depth * 4))?;
        for child in &self.child_references {
            child.fmt_with_depth(f, depth + 1)?; // Increase depth for each recursion
        }
        write!(f, "{}}}\n", " ".repeat(depth * 4)) // Adjust indentation
    }
}

impl fmt::Debug for TowerWithRef {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        self.fmt_with_depth(f, 0) // Start with depth 0
    }
}

fn get_data() -> Vec<String> {
    let file = File::open("input_data.txt").unwrap();

    let lines: Vec<String> = BufReader::new(file)
        .lines()
        .map(|line| line.unwrap())
        .collect();
    lines
}

fn create_tower(tower_name: & str, towers: & HashMap<String, Tower>) -> TowerWithRef {
    let this_tower: Tower = towers.get(tower_name).expect("Expect the tower to be in the map").clone();
    let child_list = this_tower.children.clone();
    let mut this_tower_with_ref = TowerWithRef::new(this_tower);
    for child in child_list {
        this_tower_with_ref.add_child(create_tower(&child, towers))
    }
    return this_tower_with_ref;
}

fn get_iterative_weight(tower: &mut TowerWithRef) -> i32 {
    let mut weight = tower.tower.get_own_weight();
    for child in &mut tower.child_references {
        weight += get_iterative_weight(child);
    }
    tower.iterative_weight = weight;
    weight
}

fn get_outlier(towers: &[TowerWithRef]) -> Option<usize> {
    let correct_weight = if towers[0].iterative_weight == towers[1].iterative_weight {
        towers[0].iterative_weight
    } else {
        towers[2].iterative_weight
    };

    towers.iter().position(|tower| tower.iterative_weight != correct_weight).map(|outlier_idx| {
        println!("Found an outlier, correct weight should be {}, but {} has weight {}", correct_weight, towers[outlier_idx].tower.name, towers[outlier_idx].iterative_weight);
        println!("To correct this, the iterative weight needs to be increased {}", correct_weight - towers[outlier_idx].iterative_weight);
        outlier_idx
    })
}

fn get_is_balanced(tower: &TowerWithRef) -> bool {
    match tower.child_references.len() {
        0 => true,
        1 => get_is_balanced(&tower.child_references[0]),
        2 => 
            tower.child_references[0].iterative_weight == tower.child_references[1].iterative_weight || (get_is_balanced(&tower.child_references[0]) && get_is_balanced(&tower.child_references[1])),
            
        
        _ => {
            if let Some(outlier_idx) = get_outlier(&tower.child_references) {
                let outlier_tower = &tower.child_references[outlier_idx];
                if get_is_balanced(outlier_tower) {
                    println!("Found the error in {}", outlier_tower.tower.name);
                    exit(0);
                }
                return false;
            }
            return true;
        }
    }
}

pub fn main() {
    let input_data = get_data();
    
    let regex_variable = Regex::new(r"^(\w+) \((\d+)\)( -> (.+))?$").unwrap();
    let mut towers: HashMap<String, Tower> = HashMap::new();

    for line in input_data.iter() {
        match regex_variable.captures(line) {
            Some(captures) => {
                let own_weight: i32 = (&captures[2]).parse().unwrap();
                let name = (&captures[1]).to_string();
                
                let this_tower = towers.entry(name.clone())
                .and_modify(|tower| tower.set_own_weight(own_weight))
                .or_insert_with(|| Tower::new(name.clone(), own_weight));

            if let Some(children) = captures.get(4) {
                    let children_vector: Vec<String> = children.as_str().split(", ").map(|s| s.to_string()).collect();
                    this_tower.set_children(children_vector.clone());

                    for child_name_string in &children_vector {
                        towers.entry(child_name_string.clone()).and_modify(|tower| tower.set_parent(name.clone())).or_insert_with(|| {
                            let mut tower = Tower::new(child_name_string.clone(), 0);
                            tower.set_parent(name.clone());
                            tower
                        });
                    }
                    
                }
            },
            None => panic!()
        }
    }

    
    let (top_tower_name, _) = towers.iter().filter(|(_, v)| v.get_parent().is_none()).next().unwrap().clone();
    println!("top_tower_name {}", top_tower_name);
    
    
    // At this step, at the end of part 1, we have a map with all objects but with wtring references.
    // We will now create a new list starting from the top tower name, and create a proper tree.
    let mut top_tower = create_tower(top_tower_name, &towers);
    get_iterative_weight(&mut top_tower);
    println!("top_tower {:?}", top_tower);
    get_is_balanced(&top_tower);
    
       
    
    
}
