// Swift extension to add a reverse method to String
extension String {
    /// Returns a new string with the characters in reverse order.
    func reversed() -> String {
        return String(self.reversed())
    }
    
    /// Reverses the string in place.
    mutating func reverse() {
        self = String(self.reversed())
    }
}

// Example usage:
// let originalString = "hello"
// let reversedString = originalString.reversed() // Returns "olleh"
// 
// var mutableString = "world"
// mutableString.reverse() // mutableString is now "dlrow"