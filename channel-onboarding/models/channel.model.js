const mongoose = require('mongoose');

var channelSchema = new mongoose.Schema({
  channelName: { type: String },
  ytcId: { type: String },
  primaryNation: { type: String },
  language: { type: String },
});

mongoose.model('Channel', channelSchema);
