const mongoose = require('mongoose');

var channelSchema = new mongoose.Schema({
  ytcId: { type: String },
  channelName: { type: String },
  language: { type: String },
  primaryNation: { type: String },
});

mongoose.model('Channel', channelSchema);
