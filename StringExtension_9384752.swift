extension String {
    /// Reverses the string in place.
    mutating func reverse() {
        self = String(self.reversed())
    }

    /// Returns a new string with the characters in reverse order.
    /// - Returns: A new reversed string.
    func reversed() -> String {
        return String(self.reversed())
    }
}

// Example usage:
// var myString = "hello"
// myString.reverse()
// print(myString) // prints "olleh"
//
// let originalString = "world"
// let reversedString = originalString.reversed()
// print(reversedString) // prints "dlrow"