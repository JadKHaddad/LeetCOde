struct Solution {}

impl Solution {
    pub fn int_to_roman(num: i32) -> String {
        let mut result = String::new();
        let mut num = num;
        while num > 0 {
            if num >= 1000 {
                result.push_str("M");
                num = num - 1000;
                continue;
            }
            if num >= 900 {
                result.push_str("CM");
                num = num - 900;
                continue;
            }
            if num >= 500 {
                result.push_str("D");
                num = num - 500;
                continue;
            }
            if num >= 400 {
                result.push_str("CD");
                num = num - 400;
                continue;
            }
            if num >= 100 {
                result.push_str("C");
                num = num - 100;
                continue;
            }
            if num >= 90 {
                result.push_str("XC");
                num = num - 90;
                continue;
            }
            if num >= 50 {
                result.push_str("L");
                num = num - 50;
                continue;
            }
            if num >= 40 {
                result.push_str("XL");
                num = num - 40;
                continue;
            }
            if num >= 10 {
                result.push_str("X");
                num = num - 10;
                continue;
            }
            if num >= 9 {
                result.push_str("IX");
                num = num - 9;
                continue;
            }
            if num >= 5 {
                result.push_str("V");
                num = num - 5;
                continue;
            }
            if num >= 4 {
                result.push_str("IV");
                num = num - 4;
                continue;
            }
            if num >= 1 {
                result.push_str("I");
                num = num - 1;
                continue;
            }
        }
        result
    }
}

fn main() {
    let num = 1994;
    println!("{}", Solution::int_to_roman(num));
}
