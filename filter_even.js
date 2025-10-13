/**
 * Filters even numbers from an array.
 * @param {number[]} arr - The input array of numbers.
 * @returns {number[]} A new array containing only the even numbers.
 */
function filterEvenNumbers(arr) {
  if (!Array.isArray(arr)) {
    throw new Error("Input must be an array.");
  }
  return arr.filter(num => {
    if (typeof num !== 'number' || !Number.isInteger(num)) {
      throw new Error("Array must contain only integers.");
    }
    return num % 2 === 0;
  });
}

// Example usage:
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evenNumbers = filterEvenNumbers(numbers);
console.log("Original array:", numbers);
console.log("Filtered even numbers:", evenNumbers);

module.exports = { filterEvenNumbers };
