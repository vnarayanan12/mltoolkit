import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';
import { DatasetService } from '../apis/test/api/dataset.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'data-ingest-frontend';

  path = new FormControl('');

  filenames = [];

  datasetName = '';

  constructor(
    private testApi: DatasetService
  ) {}

  postDataSet() {
    
  }

  getFilepaths() {
    this.testApi.getFilepaths().subscribe(
      rtv => {
        console.log(rtv);
      },
      err => {
        console.log(err);
      }
    )
  }

  getDataSetFromDB() {

  }

}
