import React, { Component } from 'react';
import './App.css';
import ScrapyCard from './ScrapyCard'
import Grid from '@material-ui/core/Grid';

class App extends Component {
  state = {
    data: []
  };

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
    let urlParams = new URLSearchParams(window.location.search);
    let tag = urlParams.get('tag');
    fetch('/api/clip?tag=' + tag)
      .then(res => res.json())
      .then(data => this.setState({ data }));
  }

  render() {
    let data_list = [];
    for(var i in this.state.data){
      let url = this.state.data[i].url
      let img = this.state.data[i].img
      let title = this.state.data[i].title
      data_list.push(
        <ScrapyCard title={title} url={url} img={img} />
      );
    }

    return (
      <div className="App">
        <Grid container spacing={24}>
          {data_list}
        </Grid>
      </div>
    );
  }
}

export default App;
