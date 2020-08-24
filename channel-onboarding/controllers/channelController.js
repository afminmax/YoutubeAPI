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
  if (req.body._id == '') insertRecord(req, res);
  else updateRecord(req, res);
});

function insertRecord(req, res) {
  var channel = new Channel();

  // channel metadata input fields
  channel.ytcId = req.body.ytcId;
  channel.channelName = req.body.channelName;
  channel.description = req.body.description;
  channel.primaryNation = req.body.primaryNation;
  channel.language = req.body.language;
  channel.mainTheme = req.body.mainTheme;
  channel.tags = req.body.tags;
  channel.comments = req.body.comments;

  // references
  channel.references.email = req.body.email;
  channel.references.website = req.body.website;
  channel.references.twitter = req.body.twitter;
  channel.references.facebook = req.body.facebook;
  channel.references.instagram = req.body.instagram;
  channel.references.twitch = req.body.twitch;
  channel.references.wechat = req.body.wechat;
  channel.references.tiktok = req.body.tiktok;
  channel.references.otherYt = req.body.otherYt;
  channel.references.vimeo = req.body.vimeo;
  channel.references.misc = req.body.misc;

  // hidden fields
  channel.active = Boolean(true);
  channel.process = Boolean(true);
  channel.videoIds = [];
  channel.playListIds = [];
  channel.afmSites = [];
  channel.addedBy = 'afmadmin';
  var dt = new Date();
  channel.dateAdded = dt.toUTCString();
  channel.datePaused = null;
  channel.lastUpdate = null;

  channel.save((err, doc) => {
    if (!err) res.redirect('channel/list');
    // if no error, go to the list view
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

  // // setup here for adding channel time series document with new channel
  // var channelTimeData = new channelTimeData()
  // channelTimeData.save()
}
// update a channel's record
function updateRecord(req, res) {
  Channel.findOneAndUpdate(
    { _id: req.body._id },
    req.body,
    { new: true },
    (err, doc) => {
      if (!err) {
        res.redirect('channel/list');
      } else {
        if (err.name == 'ValidationError') {
          handleValidationError(err, req.body);
          res.render('channel/addOrEdit', {
            viewTitle: 'Update Channel',
            channel: req.body,
          });
        } else console.log('Channel update error occurred : ' + err);
      }
    }
  );
}

// delete a channel
router.get('/delete/:id', (req, res) => {
  Channel.findByIdAndRemove(req.params.id, (err, doc) => {
    if (!err) {
      res.redirect('/channel/list');
    } else {
      console.log('Channel delete error occurred :' + err);
    }
  });
});

// validation helper function
function handleValidationError(err, body) {
  for (field in err.errors) {
    switch (err.errors[field].path) {
      case 'channelName':
        body['channelNameError'] = err.errors[field].message;
        break;
      case 'ytcId':
        body['ytcIdError'] = err.errors[field].message;
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

// this route allows us to find a record by id and present it on the main crud page for eventual update
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
