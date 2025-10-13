const { v4: uuidv4 } = require('uuid');

function generateFibonacci(n) {
  if (n <= 0) return [];
  if (n === 1) return [0];
  if (n === 2) return [0, 1];

  const sequence = [0, 1];
  for (let i = 2; i < n; i++) {
    sequence[i] = sequence[i - 1] + sequence[i - 2];
  }
  return sequence;
}

// Generate a random filename using uuid
const randomFileName = `/workspace/fibonacci_${uuidv4()}.js`;

// Create the content for the new file using a template literal correctly
const fileContent = `// Fibonacci sequence up to \${n} terms
function fibonacciSequence(n) {
  console.log("Fibonacci sequence up to \${n} terms:");
  const sequence = generateFibonacci(n);
  console.log(sequence.join(", "));
}

function generateFibonacci(n) {
  if (n <= 0) return [];
  if (n === 1) return [0];
  if (n === 2) return [0, 1];

  const sequence = [0, 1];
  for (let i = 2; i < n; i++) {
    sequence[i] = sequence[i - 1] + sequence[i - 2];
  }
  return sequence;
}

fibonacciSequence(\${process.argv[2] || 10});
`;

// Write the content to the new file
const fs = require('fs');
fs.writeFileSync(randomFileName, fileContent);

console.log(`Fibonacci function generated and saved to ${randomFileName}`);