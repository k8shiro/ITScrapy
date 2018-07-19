import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardMedia from '@material-ui/core/CardMedia';
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';

const styles = {
  card: {
    width: '100%',
    height: '100%',
  },
  media: {
    paddingTop: '56.25%', // 16:9
  },
};

function SimpleMediaCard(props) {
  const { classes } = props;
  const theme = createMuiTheme({
    overrides: {
      MuiCard: {
        root: {
          backgroundColor: '#000000',
          width: '100%',
          height: '100%',
        }
      },
      MuiCardMedia: {
        root: {
          backgroundColor: '#ffffff',
        }
      },
    },
  });

  return (
    <Grid item xs={12} sm={6}  md={4} lg={3} xl={2}>
      <MuiThemeProvider theme={theme}>
        <Card className={classes.card}>
          <CardMedia
            className={classes.media}
            image={props.img}
            title="Contemplative Reptile"
          />
          <div className="cardTitle">
            <a href={props.url}>
              {props.title}
            </a>
          </div>
        </Card>
      </MuiThemeProvider>
    </Grid>
  );
}

SimpleMediaCard.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(SimpleMediaCard);
