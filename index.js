

const tmi = require('tmi.js');
const fs = require('fs');
const client = new tmi.Client({
  options: { debug: true },
  connection: {
    secure: true,
    reconnect: true
  },
  identity: {
    username: 'eurystheussc2',
    password: 'oauth:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
  },
  channels: ['eurystheussc2']
});


client.connect();
fs.watchFile("/Users/matth/Desktop/mmrdetector/supply_block.txt",(curr, prev) => {
      const data = fs.readFileSync('/Users/matth/Desktop/mmrdetector/supply_block.txt', 'utf8');
      client.say('#DaveTestaSC', data);



});
