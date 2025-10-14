const { filterAndSaveEvenNumbers } = require('./filterAndSave');

const testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const savedFileName = filterAndSaveEvenNumbers(testArray);

console.log(`The function returned the filename: ${savedFileName}`);