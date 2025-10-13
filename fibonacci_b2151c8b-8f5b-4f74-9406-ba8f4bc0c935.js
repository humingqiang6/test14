// Fibonacci sequence up to ${n} terms
function fibonacciSequence(n) {
  console.log("Fibonacci sequence up to ${n} terms:");
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

fibonacciSequence(${process.argv[2] || 10});
