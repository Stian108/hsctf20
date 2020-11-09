# A3
Solves: 14

## Description
OWASP publishes a list of top 10 web application security risks every few years.

This challenge is related to number 3 on the list: [A3 - Sensitive Data Exposure](https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure). Data breaches are a major issue, and are often caused by human error and/or incompetence. In this challenge a series of mistakes by the website owner will lead you to find valid credentials for the website in question.

Can you log into this site?

[a3.heltsikker.no](https://a3.heltsikker.no/)

## Solution
The page looks like an ordinary login page, but looking at the source reveals a suspicious comment:
```html
<!-- Below meta tag is obselete, we changed to using /robots.txt a while back -->
<!-- meta name="robots" content="noindex, nofollow" -->
```

Guiding us in the direction of the [`/robots.txt`](https://a3.heltsikker.no/robots.txt):
```
User-Agent: *
Disallow: /backups/
```

Which again leads us the the direction of the [`/backups/`](https://a3.heltsikker.no/backups/) directory containing a file `users.sqlite.bak`

Opening this file in an SQLite viewer like https://inloop.github.io/sqlite-viewer/ shows:
| id      | username    | password                              |
| :------ | :---------: | ------------------------------------: |
| 1       | johnny      | `84d961568a65073a3bcf0eb216b2a576`    |

The password is not in cleartext, but using a Hash Cracker like https://crackstation.net/ yields the password `superman` .

We can then log into the site with the username `johnny` and password `superman` and get the flag:
```
 HSCTF{d0nt_us3_y0ur_w3bs3rv3r_@s_y0ur_pr1v@t3_dr0pb0x_j0hnny} 
```