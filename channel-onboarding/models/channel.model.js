const mongoose = require('mongoose');

var channelSchema = new mongoose.Schema({
  channelName: { type: String, required: 'Required Field' },
  ytcId: { type: String },
  primaryNation: { type: String },
  language: { type: String },
  channelAlias: { type: String },
  email: { type: String },
});

// Custom validation for email
channelSchema.path('email').validate((val) => {
  emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return emailRegex.test(val);
}, 'Invalid e-mail.');

mongoose.model('Channel', channelSchema);
