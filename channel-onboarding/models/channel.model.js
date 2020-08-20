const { mongo } = require('mongoose');

const mongoose = require('mongoose');

var channelSchema = new mongoose.Schema({
  _id: null,
  ytcId: null,
  displayName: null,
  channelActive: null,
  ytDescription: null,
  tags: [],
  videoIds: [],
  playListIds: [],
  afmSites: [],
  references: {
    email: [],
    website: [],
    twitter: [],
    facebook: [],
    instagram: [],
    twitch: [],
    wechat: [],
    otherYt: [],
  },
  addedBy: null,
  dateAdded: null,
  datePaused: null,
  lastUpdate: null,
});

mongoose.model('Channel', channelSchema);
