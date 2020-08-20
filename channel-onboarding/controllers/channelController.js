const express = require('express');
var router = express.Router();
const mongoose = require('mongoose');
const Channel = mongoose.model('Channel');
module.exports = router;

router.get('/', function (req, res) {
  res.render('channel/addOrEdit', {
    viewTitle: 'Insert Channel',
  });
});

router.post('/', function (req, res) {
  console.log(req.body);
});

function insertRecord(req, res) {
  var channel = new Channel();
  channel.channelName = req.body.channelName;
  channel.ytcId = req.body.ytcId;
  channel.primaryNation = req.body.primaryNation;
  channel.language = req.body.language;
  channel.save((err, doc) => {
    if (!err) console.log('somehting');
    else {
      console.log('Error during record insertion : ' + err);
    }
  });
}
