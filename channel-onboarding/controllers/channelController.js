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
  channel.email = req.body.email;
  channel.save((err, doc) => {
    if (!err) res.redirect('channel/list');
    // if no error, go to the list
    else {
      if (err.name == 'ValidationError') {
        // if there is a validation error, refresh page with alerts
        handleValidationError(err, req.body); // calls the validation helper function
        res.render('channel/addOrEdit', {
          viewTitle: 'Insert Channel',
          channel: req.body,
        });
      } else console.log('Error during record insertion : ' + err); // catches any other errors, eg db/conn
    }
  });
}

// validation helper function
function handleValidationError(err, body) {
  for (field in err.errors) {
    switch (err.errors[field].path) {
      case 'channelName':
        body['channelNameError'] = err.errors[field].message;
        break;
      case 'email':
        body['emailError'] = err.errors[field].message;
        break;
      default:
        break;
    }
  }
}

// after record insert, redirect to a new page called 'list' that lists the inserted content
router.get('/list', (req, res) => {
  Channel.find((err, docs) => {
    if (!err) {
      res.render('channel/list', {
        list: docs, //pre-handlebars post 4.6.0
        // list: docs.map((doc) => doc.toJSON()), //updated for handlebars post 4.6.0
      });
    } else {
      console.log('Error retrieving the channel list :' + err);
    }
  });
});
// Note: https://github.com/handlebars-lang/handlebars.js/issues/1642

router.get('/:id', (req, res) => {
  Channel.findById(req.params.id, (err, doc) => {
    if (!err) {
      res.render('channel/addOrEdit', {
        viewTitle: 'Update Channel',
        channel: doc,
      });
    }
  });
});

// (doc = doc.toJSON()),
