import React, { PureComponent } from 'react';
import './App.css';
import ScrapyCard from './ScrapyCard'
import Grid from '@material-ui/core/Grid';

class App extends PureComponent {
  state = {
    data: []
  };

  componentDidMount() {
    this.getCardState();
    this.timerID = setInterval(
      () => this.getCardState(),
      10000
    );
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  GetQueryString() {
    if (1 < document.location.search.length) {
      let query = document.location.search.substring(1);

      let parameters = query.split('&');

      let result = {};
      for (var i = 0; i < parameters.length; i++) {
        let element = parameters[i].split('=');

        let paramName = decodeURIComponent(element[0]);
        let paramValue = decodeURIComponent(element[1]);

        result[paramName] = decodeURIComponent(paramValue);
      }
      return result;
    }
    return null;
  }

  getCardState() {
    let urlParams = this.GetQueryString();
    let tag = urlParams['tag'];
    fetch('/api/clip?tag=' + tag)
      .then(res => res.json()).catch(function(err) {console.error(err);})
      .then(data => this.setState({ data }));
    console.log(this.state.data)
  }

  render() {
    let data_list = [];
    for(var i in this.state.data){
      let url = this.state.data[i].url
      let img = this.state.data[i].img
      let title = this.state.data[i].title
      data_list.push(
        <ScrapyCard title={title} url={url} img={img} key={url} />
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
