# Exclusive
Solves: 6

## Description
Some sketchy mathematicians approached me on the street with an encrypted note and told me to remember the word `math`, do you know what to do with this information?
```
JTI3PCsaGQkDGCsFAgURGgM+FxoUEQAHHhgHHAgMBzcfBBgRMg4aNxUOBhU=
```
## Solution
Since the string ends in `=` it is very likely to be bas64 encoded, as base64 adds `=` as padding at the end of a string. The biggest hint in this challenge is the name as it hints to the use of XOR, exclusive or, for encryption. The emphasis on the word `math` also hints towards the use of repeating key XOR with math as the key. The easiest way to do this, especially from my phone, is using [CyberChef(click for solution)](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)XOR(%7B'option':'UTF8','string':'math'%7D,'Standard',false)&input=SlRJM1BDc2FHUWtER0NzRkFnVVJHZ00rRnhvVUVRQUhIaGdISEFnTUJ6Y2ZCQmdSTWc0YU54VU9CaFU9)

Which gives the flag:
```
HSCTF{many_modern_cryptosystems_rely_on_xor}
```