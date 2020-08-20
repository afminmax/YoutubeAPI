const express = require('express');
var router = express.Router();

router.get('/', function (request, response) {
  response.render('channel/addOrEdit', {
    viewTitle: 'Insert Channel',
  });
});

module.exports = router;
