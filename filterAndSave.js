const fs = require('fs');
const path = require('path');

/**
 * Filters even numbers from an array and saves them to a file with a random name.
 * @param {number[]} array - The input array of numbers.
 * @returns {string} - The name of the file where the even numbers were saved.
 */
function filterAndSaveEvenNumbers(array) {
  const evenNumbers = array.filter(num => num % 2 === 0);
  const randomFileName = `even_numbers_${Math.floor(Math.random() * 1000000)}.json`;
  const filePath = path.join(__dirname, randomFileName);

  fs.writeFileSync(filePath, JSON.stringify(evenNumbers, null, 2));
  console.log(`Even numbers filtered and saved to ${randomFileName}`);
  return randomFileName;
}

module.exports = { filterAndSaveEvenNumbers };
