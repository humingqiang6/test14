fn main() {
    // --- Ownership Rules Demonstration ---

    // 1. Each value in Rust has a variable that's called its owner.
    // 2. There can only be one owner at a time.
    // 3. When the owner goes out of scope, the value will be dropped.

    println!("--- Basic Ownership Transfer ---");
    {
        // `s1` owns the String value
        let s1 = String::from("hello");
        println!("Initial owner s1: {}", s1);

        // `s2` takes ownership of the String value from `s1`
        // `s1` is no longer valid after this line.
        let s2 = s1;

        // println!("s1 is now invalid: {}", s1); // This would cause a compile-time error!
        println!("s2 is the new owner: {}", s2);
    } // `s2` goes out of scope here, and the String is dropped.

    println!("\n--- Ownership with Functions ---");
    {
        let s3 = String::from("world");
        println!("Owner before function call: {}", s3);

        // `takes_ownership` takes ownership of `s3`
        takes_ownership(s3);

        // println!("s3 is invalid after function call: {}", s3); // This would cause a compile-time error!
    } // `s3` was moved, so nothing happens here for `s3` itself.

    println!("\n--- Return Values and Ownership ---");
    {
        // `gives_ownership` returns a String, which `s4` takes ownership of.
        let s4 = gives_ownership();
        println!("Owner after function returns: {}", s4);

        // `s4` is moved to `s5`. `s4` becomes invalid.
        let s5 = s4;
        println!("New owner after assignment: {}", s5);

    } // `s5` (formerly `s4`) goes out of scope and is dropped.

    println!("\n--- References and Borrowing ---");
    {
        let s6 = String::from("Rust");
        println!("Original string s6: {}", s6);

        // `calculate_length` borrows `s6`, does not take ownership.
        let len = calculate_length(&s6);
        println!("Length calculated by function: {}, and s6 is still valid: {}", len, s6);

        // Mutable reference example
        let mut s7 = String::from("Hello, ");
        println!("String s7 before mutation: {}", s7);
        append_world(&mut s7);
        println!("String s7 after mutation: {}", s7);
    } // `s6` and `s7` go out of scope and are dropped.
}

// Function that takes ownership of a String
fn takes_ownership(some_string: String) {
    println!("Function took ownership and printed: {}", some_string);
    // `some_string` goes out of scope here, and the String is dropped.
}

// Function that returns a String, transferring ownership to the caller
fn gives_ownership() -> String {
    let some_string = String::from("yours");
    some_string // Ownership of `some_string` is moved to the calling function.
}

// Function that calculates length by borrowing a reference to a String
fn calculate_length(s: &String) -> usize {
    s.len() // `s` is a reference, so it doesn't own the value and doesn't drop it.
}

// Function that mutates a string by borrowing a mutable reference
fn append_world(s: &mut String) {
    s.push_str("world!"); // `s` is a mutable reference, so we can change the value it points to.
}