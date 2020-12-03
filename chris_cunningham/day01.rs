use std::fs;
use itertools::Itertools;

fn get_answer(d: &Vec<i32>, r: usize) -> i32 {
    d.iter().cloned().combinations(r)
        .find(|x| x.iter().sum::<i32>() == 2020)
        .unwrap()
        .iter()
        .product()
}

pub fn solve() {
    let data: Vec<i32> = fs::read_to_string("inputs/day01.txt")
        .unwrap()
        .lines()
        .filter_map(|s| s.parse::<i32>().ok())
        .collect();

    println!("part a: {}", get_answer(&data, 2));
    println!("part b: {}", get_answer(&data, 3));
}
