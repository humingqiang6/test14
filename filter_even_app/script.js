// Function to filter even numbers from an array
function filterEvenNumbers(inputArray) {
  return inputArray.filter(num => num % 2 === 0);
}

// Example usage
const originalArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evenNumbers = filterEvenNumbers(originalArray);
console.log('Original Array:', originalArray);
console.log('Filtered Even Numbers:', evenNumbers);

// Generate a random filename
const randomFileName = `even_numbers_${Math.floor(Math.random() * 1000000)}.js`;

// Write the result to the random file
// Note: This part requires Node.js environment and 'fs' module
// For a simple browser script, the file writing part would be different or omitted.
const fs = require('fs');
const fileContent = `// This file contains the result of filtering even numbers.\nconst evenNumbers = ${JSON.stringify(evenNumbers)};\nconsole.log('Filtered Even Numbers:', evenNumbers);\n`;
fs.writeFileSync(randomFileName, fileContent);
console.log(`Result saved to ${randomFileName}`);
