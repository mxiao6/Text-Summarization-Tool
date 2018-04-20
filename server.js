/**
 * listening on port 5000
 * @type {*|number}
 */
const port = process.env.PORT || 5000;

/**
 * separate app from server for testing easily
 */
const app = require('./app');

if (!module.parent) {
  app.listen(port, () => console.log(`Listening on ${port}`));
}
