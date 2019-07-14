import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  error: any;

  constructor(
    private authService: AuthService,
    private router: Router,
  ) { }

  ngOnInit() {
  }

  register(nickname: string, email: string, password: string) {
    console.log(nickname)
    console.log(email)
    console.log(password)
    this.authService.register(nickname, email, password).subscribe(
      success => this.router.navigate(['login']),
      error => this.error = error
    );
  }

}
