#!/usr/bin/env node
setTimeout(() => process.exit(0), 5 * 60 * 1000);
(async function challenge() {
  console.log(challenge.toString());
  try {
    const linereader = require("readline").createInterface({
      input: process.stdin,
    });

    process.mainModule.require = require = () => {
      throw new Error("ILLEGAL INPUT DETECTED!");
    };
    process.stdout.write("> ");
    for await (const line of linereader) {
      eval(line);
      process.stdout.write("> ");
    }
  } catch (err) {
    console.log(err.message);
  }
})().finally(() => process.exit(0));
