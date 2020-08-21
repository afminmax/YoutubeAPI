require('./models/db');
const express = require('express');
const path = require('path');
const exphbs = require('express-handlebars');

const Handlebars = require('handlebars');
const {
  allowInsecurePrototypeAccess,
} = require('@handlebars/allow-prototype-access');

const bodyparser = require('body-parser');
const app = express();
app.use(
  bodyparser.urlencoded({
    extended: true,
  })
);
app.use(bodyparser.json());
app.set('views', path.join(__dirname, '/views/'));
app.engine(
  'hbs',
  exphbs({
    extname: 'hbs',
    defaultLayout: 'mainLayout',
    layoutsDir: __dirname + '/views/layouts/',
    handlebars: allowInsecurePrototypeAccess(Handlebars),
  })
);

app.set('view engine', 'hbs');

const channelController = require('./controllers/channelController');

app.listen(3000, function () {
  console.log('server started on port 3000');
});

app.use('/channel', channelController);
