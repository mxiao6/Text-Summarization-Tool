import React, { Component } from 'react';
import _ from 'lodash';
import { Spin, Button, Upload } from 'antd';

import './App.css';
import axios from 'axios';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      result: '',
      inputList: [],
      loading: false,
    };
  }

  // input: [string1, string2]
  // output: [[key1, key2], []]

  _addToInput = value => {
    let newInput = this.state.inputList.slice(0);
    newInput.push(value);
    this.setState({
      inputList: newInput,
    });
  };

  /**
   * before upload, get the file content, parse it then call api manually.
   * the later uploading is not necessary so return false to stop it
   * @param file
   * @returns {boolean}
   */
  beforeUpload = file => {
    var reader = new FileReader();
    let callback = text => {
      this._addToInput(text);
      console.log('inputList', this.state.inputList);
    };
    reader.onload = function(e) {
      var text = reader.result;
      callback(text);
    };
    reader.readAsText(file);

    return false;
  };

  _onSubmit = () => {
    this.setState({
      loading: true,
    });
    axios
      .post('/load', this.state.inputList)
      .then(res => {
        console.log(res.data);
        this.setState({
          result: res.data,
          loading: false,
        });
      })
      .catch(e => {
        console.error(e.response);
      });
  };

  /**
   * react component render function
   * @returns {XML}
   */
  render() {
    return (
      <div className="App">
        <Upload
          action="http://localhost:5000/load"
          beforeUpload={this.beforeUpload}
        >
          <Button type="primary">Upload</Button>
        </Upload>
        <Button onClick={this._onSubmit}>Submit</Button>
        {this.state.loading ? <Spin /> : <div>{this.state.result}</div>}
      </div>
    );
  }
}

export default App;
