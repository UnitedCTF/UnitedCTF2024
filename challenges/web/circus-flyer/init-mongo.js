db = db.getSiblingDB('united');
db.createUser({
  user: 'ctfuser',
  pwd: 'Pgc0O9RdEp8HOcwJUU83',
  roles: [{ role: 'readWrite', db: 'united' }]
});
db.colors.insert([
{ "name": "circus-red", "hex": "#FF4500" },
{ "name": "clown-nose-red", "hex": "#DC143C" },
{ "name": "tent-yellow", "hex": "#FFD700" },
{ "name": "ringmaster-blue", "hex": "#1E90FF" },
{ "name": "acrobatic-purple", "hex": "#8A2BE2" },
{ "name": "performer-pink", "hex": "#FF69B4" },
{ "name": "elephant-gray", "hex": "#A9A9A9" },
{ "name": "lion-mane-orange", "hex": "#FFA500" },
{ "name": "juggler-green", "hex": "#32CD32" },
{ "name": "tightrope-turquoise", "hex": "#40E0D0" },
  {"name": "LgpPkEpSo3", "hex": "synt-zbatbvffbzntvp" }
]);

