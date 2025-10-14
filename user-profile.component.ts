// This file was generated as a mock-up since the 'ng' command is not available in the current environment.
// In a real Angular project, you would generate this using the Angular CLI.

export interface User {
  id: number;
  name: string;
  email: string;
  role: string;
}

export class UserProfileComponent {
  user: User = {
    id: 1,
    name: 'John Doe',
    email: 'john.doe@example.com',
    role: 'Admin'
  };

  constructor() { }

  ngOnInit(): void {
    // Typically, you would fetch user data here
  }
}