use std::fs;

pub fn solve() {
    let data: Vec<Vec<bool>> = fs::read_to_string("inputs/day03.txt")
        .unwrap()
        .lines()
        .map(|x| x.trim().chars().map(|y| y == '#').collect())
        .collect();

    let slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];
    let x_len = data[0].len();
    let y_len = data.len();

    let trees_on_slope = |dx: usize, dy: usize|
        (0..y_len).step_by(dy).enumerate()
            .filter(|x| data[x.1][x.0 * dx % x_len])
            .count();

    let part_a = trees_on_slope(3, 1);
    println!("part a: {}", part_a);

    let part_b: usize = slopes.iter().map(|x| trees_on_slope(x.0, x.1)).product();
    println!("part b: {}", part_b);
}