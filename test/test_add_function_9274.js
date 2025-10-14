// test_add_function_9274.js
const { expect } = require('chai');
const { add } = require('../src/math_functions');

describe('Add Function', () => {
  it('should add two positive numbers correctly', () => {
    expect(add(2, 3)).to.equal(5);
  });

  it('should add two negative numbers correctly', () => {
    expect(add(-2, -3)).to.equal(-5);
  });

  it('should add a positive and a negative number correctly', () => {
    expect(add(5, -3)).to.equal(2);
  });

  it('should add zero to a number correctly', () => {
    expect(add(42, 0)).to.equal(42);
  });
});