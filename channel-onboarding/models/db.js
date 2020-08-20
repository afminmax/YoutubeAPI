const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
require('dotenv').config();

// Read the mongodb key from here:
const fs = require('fs');
const { response } = require('express');

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

app.get('/', function (request, response) {
  response.send('Boo!');
});

app.listen(3000, function () {
  console.log('server started on port 3000');
});
