use std::collections::HashMap;

fn is_prime(n: i64) -> bool {
    if n <= 1 {
        return false;
    }
    if n <= 3 {
        return true;
    }
    if n % 2 == 0 || n % 3 == 0 {
        return false;
    }
    let mut i = 5;
    while i * i <= n {
        if n % i == 0 || n % (i + 2) == 0 {
            return false;
        }
        i += 6;
    }
    true
}


pub fn main() {      
    
    // Setup
    let mut b: i64 = 108_400;
    let c: i64 = 108_400 + 17_000;
    let mut d: i64 = 2;
    let mut e: i64 = 2;
    let mut f: i64 = 1;
    let mut g: i64 = 0;
    
    // loop 1, covering increase of e until something happens
    // Things that could happen is that 2*e == b, assuming b even OR
    // e == b
    // loop {
        //     f = 1;
        //     d = 2;
    //     loop {
    //         e = 2;
    //         loop {
        //             if !is_prime(b) {
            //                 f = 0;
            //             }
            //             break;
            //         }
            
            //         break;
            //     }
            
            //     if f != 0 {
                //         h += 1;
    //     }
    
    //     if b == c {
        //         break;
        //     }
        
        //     b += 17;
        // }
        
    let mut h: i64 = 0;
    let mut b: i64 = 108_400;
    for _ in 0..=1000 {
        if !is_prime(b) {
            h += 1;
        }

        b += 17;
    }

    println!("h value {}", h);
}

// // This inner loop can only have two results.
// // If b is even, f will be reset to 0.
// // If b is odd, f will not be reset.

// if b % 2 == 0 {
//     f = 0;
// }
// break;