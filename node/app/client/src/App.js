import React, { Component } from 'react';
import './App.css';

class App extends Component {
  state = {data: []}


  componentDidMount() {
    this.timerID = setInterval(
      () => this.tick(),
      1000
    );
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  tick() {
    fetch('/users')
      .then(res => res.json())
      .then(data => this.setState({ data }));
  }

  render() {
    let data_list = [];
    for(var i in this.state.data){
      let url = JSON.stringify(this.state.data[i].url)
      let title = JSON.stringify(this.state.data[i].title)
      data_list.push(
        <dl>
          <dt>Title</dt>
          <dd>{title}</dd>
          <dt>URL</dt>
          <dd>{url}</dd>
        </dl>
      );
    }

    return (
      <div className="App">
        <h1>Data</h1>
        <div>{data_list}</div>
      </div>
    );
  }

}

export default App;
