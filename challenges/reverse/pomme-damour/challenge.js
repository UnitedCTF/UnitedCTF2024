(function challenge() {
  if (process.argv.length !== 3) process.exit(1);
  const secret = [
    153, 249, 11, 249, 58, 194, 9, 234, 21, 237, 16, 240, 9, 248, 251, 18, 232,
    5, 15, 2, 243, 11, 254, 251, 245, 13, 240, 7,
  ];
  const input = new TextEncoder().encode(process.argv[2]);
  if (input.length !== secret.length) process.exit(1);
  for (let i = 0; i < input.length; ++i) {
    let check = input[i];
    for (let j = 0; j < i + 1; ++j) {
      check = (check + secret[j]) % 255;
    }
    if (check !== 0) process.exit(check);
  }
  process.exit(0);
})();
