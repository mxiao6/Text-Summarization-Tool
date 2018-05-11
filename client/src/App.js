import React, { Component } from 'react';
import { Spin, Button, Upload, Table } from 'antd';
import _ from 'lodash';

import './App.css';
import axios from 'axios';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      dataSource: [],
      inputList: [],
      loading: false,
      nameList: [],
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
    this.setState({
      nameList: [...this.state.nameList, file.name],
    });

    return false;
  };

  _onSubmit = () => {
    this.setState({
      loading: true,
    });
    axios
      .post('/load', this.state.inputList)
      .then(res => {
        this.setState({
          dataSource: this._parseData(res.data),
          loading: false,
        });
      })
      .catch(e => {
        console.error(e.response);
      });
  };

  _parseData = data => {
    const { nameList } = this.state;

    data = data.slice(2, -3);
    var parsedList = data.split('], [');

    return _.map(_.zip(nameList, parsedList), t => ({
      key: t[0],
      filename: t[0],
      words: t[1],
    }));
  };

  _renderButtons = () => {
    return (
      <div className="buttonsContainer">
        <div>
          <Upload
            action="http://localhost:5000/load"
            beforeUpload={this.beforeUpload}
          >
            <Button type="primary">Upload</Button>
          </Upload>
        </div>
        <div>
          <Button onClick={this._onSubmit}>Submit</Button>
        </div>
      </div>
    );
  };

  _renderResults = () => {
    const { dataSource } = this.state;

    return (
      <div className="resultsContainer">
        <Table dataSource={dataSource} columns={columns} />
      </div>
    );
  };

  /**
   * react component render function
   * @returns {XML}
   */
  render() {
    const { dataSource, loading } = this.state;
    return (
      <div className="App">
        {this._renderButtons()}
        {loading ? <Spin /> : !_.isEmpty(dataSource) && this._renderResults()}
      </div>
    );
  }
}

const columns = [
  {
    title: 'Filename',
    dataIndex: 'filename',
    key: 'filename',
  },
  {
    title: 'Keywords',
    dataIndex: 'words',
    key: 'words',
  },
];

export default App;
