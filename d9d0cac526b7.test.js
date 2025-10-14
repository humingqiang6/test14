import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import ButtonComponent from './ButtonComponent';

describe('ButtonComponent', () => {
  it('renders the button with the correct label', () => {
    const label = 'Click Me';
    render(<ButtonComponent label={label} />);
    expect(screen.getByText(label)).toBeInTheDocument();
  });

  it('calls the onClick handler when clicked', () => {
    const mockOnClick = jest.fn();
    render(<ButtonComponent label="Test Button" onClick={mockOnClick} />);
    fireEvent.click(screen.getByText('Test Button'));
    expect(mockOnClick).toHaveBeenCalledTimes(1);
  });

  it('is disabled when the disabled prop is true', () => {
    render(<ButtonComponent label="Disabled Button" disabled={true} />);
    expect(screen.getByText('Disabled Button')).toBeDisabled();
  });
});