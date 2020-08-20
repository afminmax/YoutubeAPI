const mongoose = require('mongoose');
require('dotenv').config();

// Read the mongodb key from here:
const fs = require('fs');

const file = process.env.FILEPATH;
let conn = fs.readFileSync(file).toString();
//console.log('kapow: ' + conn);

mongoose.connect(conn, { useUnifiedTopology: true }, (err) => {
  if (!err) {
    console.log('Mongodb connection succeeded');
  } else {
    console.log('Error in db connection: ' + err);
  }
});
