const express = require('express');
const app = express();
const port = 3000;

// Define a route for the GET API call
app.get('/', (req, res) => {
  res.send('Hello World');
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
