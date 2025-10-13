fn main() {
    // --- Ownership Demo ---

    // 1. Variable Binding and Ownership
    println!("--- 1. Variable Binding and Ownership ---");
    let s1 = String::from("hello"); // `s1` owns the string data
    println!("s1: {}", s1);
    println!("Address of data s1 points to: {:p}", s1.as_ptr());

    // 2. Move Semantics (Moving ownership)
    println!("\n--- 2. Move Semantics ---");
    let s2 = s1; // Ownership of the string data is moved from `s1` to `s2`
                 // `s1` is no longer valid here, it's an error to use it
    println!("s2: {}", s2);
    println!("Address of data s2 points to: {:p}", s2.as_ptr());
    // println!("s1: {}", s1); // This would cause a compile-time error!

    // 3. Cloning (Deep Copy)
    println!("\n--- 3. Cloning (Deep Copy) ---");
    let s3 = s2.clone(); // A deep copy is made. `s3` gets its own copy of the data.
    println!("s2: {}", s2);
    println!("s3: {}", s3);
    println!("Address of data s2 points to: {:p}", s2.as_ptr());
    println!("Address of data s3 points to: {:p}", s3.as_ptr());
    // Now both `s2` and `s3` are valid and own their own data.

    // 4. Ownership and Functions
    println!("\n--- 4. Ownership and Functions ---");
    let s4 = String::from("world");
    println!("Before passing to function, s4: {}", s4);

    takes_ownership(s4); // `s4`'s value is moved into the function.
    // println!("After function, s4: {}", s4); // This would cause a compile-time error!

    let x = 5; // `x` is an integer, which is Copy.
    println!("Before passing to function, x: {}", x);
    makes_copy(x); // `x` would be copied when passed in, but it's a Copy type, so the original is still usable.
    println!("After function, x: {}", x); // This is fine because integers are Copy types.

    // 5. Return Values and Scope
    println!("\n--- 5. Return Values and Scope ---");
    let s5 = gives_ownership(); // The return value is moved to `s5`.
    println!("Value returned and assigned to s5: {}", s5);

    let s6 = String::from("rust");
    println!("s6 before giving ownership: {}", s6);
    let s7 = takes_and_gives_back(s6); // `s6` is moved into the function, and its value is moved out and assigned to `s7`.
    // println!("s6 after giving ownership: {}", s6); // This would cause a compile-time error!
    println!("Value returned and assigned to s7: {}", s7);

    // 6. References and Borrowing
    println!("\n--- 6. References and Borrowing ---");
    let s8 = String::from("hello");
    let len = calculate_length(&s8); // `&s8` creates a reference to `s8`. `s8` keeps ownership.
    println!("The length of '{}' is {}.", s8, len);

    // Mutable reference
    let mut s9 = String::from("hi");
    println!("s9 before mutation: {}", s9);
    change(&mut s9); // Pass a mutable reference
    println!("s9 after mutation: {}", s9);

    // Preventing mutable aliasing
    {
        let r1 = &mut s9;
        // let r2 = &mut s9; // This would cause a compile-time error due to mutable aliasing rules.
        println!("r1: {}", r1);
    } // `r1` goes out of scope, so we can create a new mutable reference again.

    let r2 = &mut s9;
    println!("r2: {}", r2);
}

// Function that takes ownership of a String
fn takes_ownership(some_string: String) {
    println!("Received string (ownership taken): {}", some_string);
    // `some_string` goes out of scope here and `drop` is called. The memory is freed.
}

// Function that takes a Copy type (like an integer)
fn makes_copy(some_integer: i32) {
    println!("Received integer (copied): {}", some_integer);
    // `some_integer` goes out of scope here. Nothing special happens.
}

// Function that gives ownership of a new String
fn gives_ownership() -> String {
    let some_string = String::from("yours");
    some_string // The value is moved out to the calling function
}

// Function that takes and returns ownership
fn takes_and_gives_back(a_string: String) -> String {
    a_string // The value is moved in and then moved out again
}

// Function that takes an immutable reference
fn calculate_length(s: &String) -> usize {
    s.len() // `s` is a reference, so it does not own the data. No `drop` is called here.
}

// Function that takes a mutable reference
fn change(some_string: &mut String) {
    some_string.push_str(", world"); // This is allowed because the reference is mutable.
}