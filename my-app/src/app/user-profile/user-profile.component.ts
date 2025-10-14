import { Component, OnInit } from '@angular/core';

// Define a simple User interface
interface User {
  id: number;
  name: string;
  email: string;
  role: string;
}

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {

  user: User | undefined;

  constructor() { }

  ngOnInit(): void {
    // In a real app, you would fetch this data from a service
    this.user = {
      id: 1,
      name: 'John Doe',
      email: 'john.doe@example.com',
      role: 'Admin'
    };
  }

}