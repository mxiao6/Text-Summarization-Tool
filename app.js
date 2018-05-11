import express from 'express';
import bodyParser from 'body-parser';

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
/**
 * increase json file size limit to 1024kb
 */
app.use(bodyParser.json({ limit: '1024kb' }));

app.post('/load', function(req, res) {
  // console.log('load api', req.body);
  var spawn = require('child_process').spawn;
  var pythonProcess = spawn('python2.7', ['./test.py', ...req.body]);
  pythonProcess.stdout.on('data', function(data) {
    res.status(200).send(data);
  });
});

/**
 * the other api calls will be 404 not found
 */
app.use((req, res) => {
  res.status(404).send('404 Not Found');
});

module.exports = app;
