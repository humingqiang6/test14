// This is a generated test file for MyComponent.
// A full setup with Jest and React Testing Library is usually required for these tests to run.

import { render, screen } from '@testing-library/react';
import MyComponent from './MyComponent';

describe('MyComponent', () => {
  test('renders with default name', () => {
    render(<MyComponent />);
    expect(screen.getByText(/Hello, World!/i)).toBeInTheDocument();
  });

  test('renders with custom name', () => {
    render(<MyComponent name="Alice" />);
    expect(screen.getByText(/Hello, Alice!/i)).toBeInTheDocument();
  });
});