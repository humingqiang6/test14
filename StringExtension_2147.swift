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
var originalString = "Hello, world!"
print("Original: $originalString)")

originalString.reverse()
print("After mutating reverse: $originalString)")

let anotherString = "Swift"
let reversedString = anotherString.reversed()
print("Original: $anotherString), Reversed: $reversedString)")