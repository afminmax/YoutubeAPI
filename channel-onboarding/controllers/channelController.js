const express = require('express');
var router = express.Router();
const mongoose = require('mongoose');
const Channel = mongoose.model('Channel');
module.exports = router;

// following route displays the form
router.get('/', function (req, res) {
  res.render('channel/addOrEdit', {
    viewTitle: 'Insert Channel',
  });
});

// following route triggers after submit is pressed and inserts the form
// data into the database, the helper function "insertRecord" is used to insert
router.post('/', function (req, res) {
  console.log(req.body);
  insertRecord(req, res);
});

function insertRecord(req, res) {
  var channel = new Channel();
  channel.channelName = req.body.channelName;
  channel.ytcId = req.body.ytcId;
  channel.primaryNation = req.body.primaryNation;
  channel.language = req.body.language;
  channel.save((err, doc) => {
    if (!err) {
      res.redirect('channel/list');
    } else {
      console.log('Error during record insertion : ' + err);
    }
  });
}

// after record insert, redirect to a new page called 'list' that lists the inserted content
router.get('/list', function (req, res) {
  res.json('list contents of insert here');
});
