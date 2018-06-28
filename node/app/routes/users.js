var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');
var mongo_schema = new mongoose.Schema({
  url: String,
  title: String
},{
  collection : 'article'
});
var  mongo_model = mongoose.model('Data', mongo_schema);


router.get('/', function(req, res, next) {
  mongoose.connect('mongodb://mongoadmin:password@mongo/scrapy?authSource=admin');

  var data;
  mongo_model.find({},{}, {sort:{_id: -1},limit:20}, function(err, docs) {
    if(!err) {
      console.log("num of item => " + docs.length)
      data = docs;
      res.json(data)
      mongoose.disconnect()  // mongodbへの接続を切断
    } else {
      console.log("find error")
    }
  });
});

module.exports = router;
