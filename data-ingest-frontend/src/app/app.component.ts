import { Component } from '@angular/core';
import { TestService } from '../apis/test/api/test.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'data-ingest-frontend';

  constructor(
    private testApi: TestService
  ) {}

  postId() {
    this.testApi.postId({id: 2}).subscribe(
      rtv => {
        console.log(rtv);
      },
      err => {
        console.log(err);
      }
    )
  }

  getId() {
    this.testApi.getId(2).subscribe(
      rtv => {
        console.log(rtv);
      },
      err => {
        console.log(err);
      }
    )
  }

}
