## Description
```
In RSA, a small e value can be problematic, but what about N? Can you decrypt this?
```

## Values

We have been given the following values:
```
Decrypt my super sick RSA:
c: 964354128913912393938480857590969826308054462950561875638492039363373779803642185
n: 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e: 65537
```
C is the ciphertext we wish to decode. N is the result of multiplying two prime numbers p and q, ie. `n = p * q`. E is the multiplicative inverse of a private exponent `d` modulo `phi`. Phi is equal to `(p-1)*(q-1)`. Here in a more ordered fashion:
```
C = ciphertext
p and q = prime numbers
n = p * q
phi = (p-1) * (q-1)
e = some number that 1 < e < phi and gcd(e,phi) == 1
d = e^(-1) mod phi
```
Great! Now we just need to find p and q...

## Factor db

[Factordb](http://factordb.com/) is a database of factorised numbers. We could try out n:
```
n = 2159947535959146091116171018558446546179 * 658558036833541874645521278345168572231473
```
Awesome! Now we can just calculate.

## Solving

```py
from Crypto.Util.number import inverse, long_to_bytes

c = 964354128913912393938480857590969826308054462950561875638492039363373779803642185
n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e = 65537
p = 2434792384523484381583634042478415057961
q = 650809615742055581459820253356987396346063

phi = (p-1)*(q-1)

d = inverse(e, phi)

m = pow(c,d,n)

print(long_to_bytes(m))
```
```bash
python3 solve.py 
'picoCTF{sma11_N_n0_g0od_73918962}'
```
There we go! 