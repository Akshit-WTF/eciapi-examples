const express = require("express");
const bodyParser = require("body-parser");
const app = express();
app.use(bodyParser.json());

const port = 3000;

app.post("/", (req, res) => {
  if (req.body.error === true) {
    console.log("There was an error!");
    // Your own error handling code here!
  } else {
    console.log(req.body.jobId);
    console.log(req.body.data);
    // Your own success handling code here!
  }
  res.sendStatus(200);
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
