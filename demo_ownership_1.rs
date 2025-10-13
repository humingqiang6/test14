// Rust 所有权演示

fn main() {
    // 1. 变量绑定和所有权
    let s1 = String::from("hello");
    println!("s1: {}", s1);

    // 2. 移动语义 (Move)
    // 将 s1 的所有权转移给 s2，s1 不再有效
    let s2 = s1;
    println!("s2: {}", s2);
    // println!("s1: {}", s1); // 这行代码会报错，因为 s1 已经被移动了

    // 3. 克隆 (Clone) - 堆上数据的深拷贝
    let s3 = String::from("world");
    let s4 = s3.clone(); // 显式克隆堆上的数据
    println!("s3: {}", s3); // s3 仍然有效
    println!("s4: {}", s4); // s4 是 s3 的一个副本

    // 4. 函数所有权示例
    let s5 = String::from("hello");
    takes_ownership(s5); // s5 的所有权被移动到函数内部
    // println!("{}", s5); // 这行代码会报错

    let x = 5;
    makes_copy(x); // x 是 Copy 类型，会被复制
    println!("x is still available: {}", x); // x 仍然可用
}

// 这个函数获取 String 的所有权
fn takes_ownership(some_string: String) {
    println!("Received string: {}", some_string);
} // some_string 在这里离开作用域并被丢弃 (drop)

// 这个函数接收一个 Copy 类型的值
fn makes_copy(some_integer: i32) {
    println!("Received integer: {}", some_integer);
} // some_integer 在这里离开作用域，但因为是 Copy 类型，所以不会发生任何事情