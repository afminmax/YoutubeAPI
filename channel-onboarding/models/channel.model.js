const mongoose = require('mongoose');

var channelSchema = new mongoose.Schema({
  ytcId: {
    type: String,
    unique: true,
    required: 'Required Field',
  },
  channelName: { type: String, required: 'Required Field' },
  description: { type: String },
  primaryNation: { type: String },
  language: { type: String },
  mainTheme: { type: String },
  tags: { type: Array },
  references: {
    email: { type: Array },
    website: { type: Array },
    twitter: { type: Array },
    facebook: { type: Array },
    instagram: { type: Array },
    twitch: { type: Array },
    wechat: { type: Array },
    tiktok: { type: Array },
    otherYt: { type: Array },
    vimeo: { type: Array },
    misc: { type: Array },
  },
  comments: { type: String },
  active: { type: Boolean },
  process: { type: Boolean },
  videoIds: { type: Array },
  playListIds: { type: Array },
  afmSites: { type: Array },
  addedBy: { type: String },
  dateAdded: { type: Date },
  datePaused: { type: Date },
  lastUpdate: { type: Date },
});

//// Custom validation for email
// channelSchema.path('email').validate((val) => {
//   emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
//   return emailRegex.test(val);
// }, 'Invalid e-mail.');

mongoose.model('Channel', channelSchema);
