import React, { Component } from 'react';
import _ from 'lodash';
import { Button, Row, Col, Upload, Input, Modal, message } from 'antd';

import './App.css';
import axios from 'axios';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      result: '',
    };
  }

  componentWillMount() {
    axios
      .get('/hello')
      .then(res => {
        this.setState({
          result: res.data,
        });
      })
      .catch(e => {
        console.error('hello', e.response);
      });
  }

  /**
   * before upload, get the file content, parse it then call api manually.
   * the later uploading is not necessary so return false to stop it
   * @param file
   * @returns {boolean}
   */
  beforeUpload = file => {
    var reader = new FileReader();
    let callback = text => {
      axios
        .post('/load', text)
        .then(res => {
          console.log(res.data);
          this.setState({
            result: res.data,
          });
        })
        .catch(e => {
          console.error(e.response);
        });
    };
    reader.onload = function(e) {
      var text = reader.result;
      callback(text);
    };
    reader.readAsText(file);

    return false;
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
          <Button type="primary">Load</Button>
        </Upload>
        <div>{this.state.result}</div>
      </div>
    );
  }
}

export default App;
