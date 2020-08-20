const express = require('express');
var router = express.Router();
const mongoose = require('mongoose');
const Channel = mongoose.model('Channel');
module.exports = router;

router.get('/', function (request, response) {
  response.render('channel/addOrEdit', {
    viewTitle: 'Insert Channel',
  });
});

router.post('/', function (request, response) {
  console.log(request.body);
});

function insertRecord(request, response) {
  var channel = new Channel();
  channel.channelName = req.body.channelName;
  channel.ytcId = req.body.ytcId;
  channel.primaryNation = req.body.primaryNation;
  channel.language = req.body.language;
  channel.save((err, doc) => {
    if (!err) res.render('added');
    else {
      console.log('Error during record insertion: ' + err);
    }
  });
}
