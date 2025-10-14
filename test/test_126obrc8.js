const { add } = require('../src/calculator');

describe('Calculator', function() {
  describe('Addition', function() {
    it('should add two positive numbers correctly', function() {
      const result = add(2, 3);
      if (result !== 5) throw new Error(`Expected 5, got ${result}`);
    });

    it('should add two negative numbers correctly', function() {
      const result = add(-2, -3);
      if (result !== -5) throw new Error(`Expected -5, got ${result}`);
    });

    it('should add a positive and a negative number correctly', function() {
      const result = add(5, -3);
      if (result !== 2) throw new Error(`Expected 2, got ${result}`);
    });

    it('should throw an error if the first argument is not a number', function() {
      let errorCaught = false;
      try {
        add('2', 3);
      } catch (e) {
        errorCaught = true;
        if (e.message !== 'Both arguments must be numbers') {
          throw new Error(`Expected error message 'Both arguments must be numbers', got '${e.message}'`);
        }
      }
      if (!errorCaught) throw new Error('Expected function to throw an error for non-number first argument');
    });

    it('should throw an error if the second argument is not a number', function() {
      let errorCaught = false;
      try {
        add(2, '3');
      } catch (e) {
        errorCaught = true;
        if (e.message !== 'Both arguments must be numbers') {
          throw new Error(`Expected error message 'Both arguments must be numbers', got '${e.message}'`);
        }
      }
      if (!errorCaught) throw new Error('Expected function to throw an error for non-number second argument');
    });
  });
});