import express from 'express';
import bodyParser from 'body-parser';

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
/**
 * increase json file size limit to 1024kb
 */
app.use(bodyParser.json({ limit: '1024kb' }));

app.get('/hello', function(req, res) {
  res.status(200).send('hello world');
});

app.post('/load', function(req, res) {
  console.log('load api', req.body);
  res.status(200).send('load successful');
});

/**
 * the other api calls will be 404 not found
 */
app.use((req, res) => {
  res.status(404).send('404 Not Found');
});

module.exports = app;
