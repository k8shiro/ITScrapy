import React, { Component } from 'react';
import './App.css';

class App extends Component {
  state = {users: []}

//  componentDidMount() {
//    fetch('/users')
//      .then(res => res.json())
//      .then(users => this.setState({ users }));
//  }

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
      .then(users => this.setState({ users }));
  }

  render() {
    return (
      <div className="App">
        <h1>Users</h1>
        <h1>{JSON.stringify(this.state.users)}</h1> </div>
    );
  }

}

export default App;
