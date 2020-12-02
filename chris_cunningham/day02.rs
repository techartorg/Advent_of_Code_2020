use std::fs;
use regex::{Regex, Captures};


fn part_a_test(matches: &Captures) -> bool {
    let low = matches.get(1).unwrap().as_str().parse::<usize>().unwrap();
    let high = matches.get(2).unwrap().as_str().parse::<usize>().unwrap();
    let char = matches.get(3).unwrap().as_str();
    let pw = matches.get(4).unwrap().as_str();
    let c = pw.matches(char).count();
    return c >= low && c <= high;
}

fn part_b_test(matches: &Captures) -> bool {
    let low = matches.get(1).unwrap().as_str().parse::<usize>().unwrap();
    let high = matches.get(2).unwrap().as_str().parse::<usize>().unwrap();
    let char = matches.get(3).unwrap().as_str().chars().nth(0).unwrap();
    let pw = matches.get(4).unwrap().as_str();
    return (pw.chars().nth(low - 1).unwrap() == char) ^ (pw.chars().nth(high - 1).unwrap() == char);
}

pub fn main() {
    let r: Regex = Regex::new(r"(\d+)-(\d+) (\w): (\w+)").unwrap();

    let data = fs::read_to_string("inputs/day02.txt").unwrap();
    let data: Vec<Captures> = data
        .lines()
        .map(|s| r.captures(s).unwrap())
        .collect();

    let part_a = data.iter()
        .filter(|x| part_a_test(x))
        .count();
    println!("part a: {}", part_a);

    let part_b = data.iter()
        .filter(|x| part_b_test(x))
        .count();
    println!("part b: {}", part_b);
}
