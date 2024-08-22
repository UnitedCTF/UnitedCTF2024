const express = require('express');
const bodyParser = require('body-parser');
const { MongoClient } = require('mongodb');
const path = require('path');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

const url = 'mongodb://ctfuser:Pgc0O9RdEp8HOcwJUU83@mongo:27017/united?authSource=united';
const db_name = 'united';
let db;

MongoClient.connect(url, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(client => {
    db = client.db(db_name);
    console.log(`Connected to database`);
  })
  .catch(error => console.error(error));


app.get('/', (_, res) => { res.render('index') });


app.get('/color', async (req, res) => {
  try {
    const name = req.query.name;
    const query = `{ "name": "${name}" }`;
    
    const colors = await db.collection('colors').find(JSON.parse(query)).toArray();
    res.send(colors);
  } catch (error) {
    res.send('error');
  }
});


app.listen(3000, () => { });
