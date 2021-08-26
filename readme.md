# report CSP violations 

1. setup a report resceiver uri with this service here
2. set headers

```

    add_header Content-Security-Policy-Report-Only "
      default-src 'self';
      [...]
      report-uri /csp-violation/;" always;

```

assuming your nginx frontend knows the location:

```
    location /csp-violation/ {
        proxy_set_header   Host                 $host;
        proxy_set_header   X-Real-IP            $remote_addr;
        proxy_set_header   X-Forwarded-For      $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto    $scheme;

        proxy_pass http://csp:6000/;
    }
```


the browser will post a request to the service at csp:6000 on violation
