## Homework 2
___

#### 1) Bozosort Implementation:
*Write a Bozosort implementation in Python or Java. Perform some empirical runtime studies on your method.*
```py
import random
import time

def bozosort(L):
    start_time = time.time()
    while not sorted(L) == L:
        a, b = random.sample(range(0, len(L)), 2)
        L[a], L[b] = L[b], L[a]
        
    print("sorted to " + str(L) + " in %s seconds." % (time.time() - start_time))
 ```
 *note - run bozosort.py for a test implementation*<br>
 
**Runtime data:**<br>

List Length | Time Trials (s) | Time Averages (s)
--- | --- | ---
12 | 2000.3538, 1486.3414, 1176.1731, 4060.0355, 4469.5698 | 2638.4947
11 | 622.4520, 1389.8424, 468.7488, 131.5704, 1227.0101 | 767.9247
10 | 40.5828, 149.0481, 37.1568, 201.3584, 65.2636      | 98.6819
9  | 5.5655, 2.4860, 1.6950, 5.7694, 9.2740             | 4.9580
8  | 0.5267, 0.3360, 0.0173, 0.0647, 0.0545             | 0.1998
7  | 0.0703, 0.1006, 0.0664, 0.1146, 0.0226             | 0.0749
6  | 0.0034, 0.0080, 0.0052, 0.0058, 0.0267             | 0.0098
5  | 0.0017, 0.0007, 0.0018, 0.0010, 0.0012             | 0.0013
4  | 0.0012, 0.0006, 0.0006, 0.0001, 0.0005             | 0.0006

___

#### 2) Autokey Vigenere cipher:
*Implement the Autokey Vigenere cipher, from scratch, in Java, JavaScript, or Python. Treat characters as codepoints.*<br>
```py
def getInts(s): #convert string into a list of numbers
    return [ord(char)-65 for char in s.upper()]

def vigenere(text, keyphrase):
    text = text.replace(' ', '') #remove spaces
    keyphrase = keyphrase.replace(' ', '')
    textInts = getInts(text)
    keyInts = getInts((keyphrase + text)[:-(len(keyphrase))])
    codedInts = []
    
    for index, item in enumerate(textInts): #build coded int list
        codedInts.append((item+keyInts[index])%26)

    codedString = ''.join([chr(num+65) for num in codedInts])
    return codedString
```
*note - run vigenere.py for a test implementation*
___

#### 3) Monoalphabetic Substitution Cipher:
*You know the message is in English and that the sender used a monoalphabetic substitution cipher. What is the plaintext?*<br>
>The progress of our arms, upon which all else chiefly depends, is as well known to the public as to myself, and it is, I trust, reasonably satisfactory and encouraging to all. With high hope for the future, no prediction in regard to it is ventured.

___

#### 4) Bifid Decryption:
*Decrypt the following ciphertext, given that you know it was encrypted with the bifid algorithm in which the Polybius square was laid out in the usual fashion using the keyphrase "Darn, not another cryptanalysis question".*<br>
```
rows:    1 0 4 2 3 1 1 0 2 1 2 1 0 1 1 2 2 0 0 4 0 0 1 0 3 0 3 1 1 0 4 2 3 1 1 0 2 1 1 0 0 0 2 1 0 0 0 0 4 1 2 2 0 3 0 3 1 1 1 2 1 2 1 0 2 1 2 2
columns: 3 4 0 0 0 0 2 2 2 3 3 2 3 3 2 3 2 3 4 0 4 2 2 1 1 4 0 0 3 4 0 0 0 0 2 2 2 0 1 1 3 1 2 0 2 4 3 4 0 4 3 2 1 1 4 0 0 0 2 1 2 2 3 4 0 2 2 2
decoded: c o m p u t e r s c i e n c e i s n o m o r e a b o u t c o m p u t e r s t h a n a s t r o n o m y i s a b o u t t e l e s c o p e s s
```
>Computer science is no more about computers than astronomy is about telescopess.

___

#### 5) Public and private keys<br>
*What are the RSA's public and private keys generated from p = 23847623789462398745236743254827634647 and q = 80147623789462398745236743254827634711?*<br>

N = `pq = 1911330379750465988511865475607817924950038631764482538080744390093883432017`<br>
Ø = `(p-1)(q-1) = 191133037975046598851186547560781792484604338418555774059027093584228162660`<br>
e = `7`<br>
d = `modular inverse (e, Ø) = 81914159132162828079079948954620768207687573607952474596725897250383498283`

**_Public Key (N, e):_**<br>
`(1911330379750465988511865475607817924950038631764482538080744390093883432017, 7)`

**_Private Key (d, e):_**<br>
`(81914159132162828079079948954620768207687573607952474596725897250383498283, 7)`

___


#### 6) Finding a RSA Private Key<br>
*If someone's RSA public key is (729880581317, 5), what is her private key? Give a detailed derivation, showing all work.*<br>

We know sqrt(729880581317) ~ 854330. Therefore, we need to test all primes up to that number to find p and q.
I wrote a quick method that finds the largest odd divisor of an input number (testing up to the input number's square root):
```py
import math
def oddFactor(n):
    i = 1
    factor = 1
    while i <= math.sqrt(n):
        i += 2
        if n%i == 0: factor = i #update largest factor found
    return factor
```
This method returns 822893 when 729880581317 is input. 729880581317 / 822893 = 886969. Using handy dandy Google, I verified that both 822893 and 886969 are prime. The user's p and q values are 822893 and 886969.

Ø = `(p-1)(q-1) = 822892 * 886968 = 729878871456`<br>
e = `5`<br>
d = `modular inverse of 729878871456 relative to 5 = 583903097165`<br>

**Her private key is (583903097165, 5)**

___


#### 7) RSA and digital signatures
#####Part A:
Because sent messages need encryption and decryption, it is sometimes difficult to tell whether encrypted text has been altered or forged. Using digital signatures allows us to verify the source of a message, ensuring its security during the encryption and decryption process.

<br>

#####Part B:
- **Sign** produces a number *s* from the equation `M^d mod N = s`.<br>
- **Verify** checks that `s^e mod N = M mod N`.

While we are not required to mathematically prove the realtionship between **sign** and **verify** for this homework, here is an implementation to prove its correctness. I'm using the values I produce in **Part C** to sign my name:<br>
- My message `M = 391398879885526901013984096355053422`<br>
- My public key (N,e) = `(1517, 7)`<br>
- My private key (N, d) = `(1517, 823)`<br>
- **sign** finds that s = `M^d mod N = 1293`<br>
- **verify** checks that `s^e mod N` equals `M mod N`:<br>
  - `s^e mod N = 1241`<br>
  - `M mod N = 1241.`<br>
- Both sides are equal, therefore **verify** returns `True`.<br>

<br>

#####Part C:

######Find my name's integer message M:

Following the method used in [this description of RSA](http://doctrina.org/How-RSA-Works-With-Examples.html "How RSA Works With Examples"), I converted the string "Kate Gotfredson" to binary using [this](http://string-functions.com/string-binary.aspx "String to Binary Converter") converter:
```
010010110110000101110100011001010010000001000111011011110111010001100110011100100110010101100100011100110110111101101110
```
I then converted that binary number to a decimal number [here](http://www.mobilefish.com/services/big_number/big_number.php "Binary to Decimal Converter"), which output my final message **M**:
```
M = 391398879885526901013984096355053422
```

######Calculate the public and private keys and sign the message:

I chose the two primes `p = 41` and `q = 37`.<br>
N = `pq = 1517`<br>
Ø = `(p-1)(q-1) = 1440`<br>
e = `7`<br>
d = `modular inverse (e, Ø) = 823`

The sign formula is `m^d mod N`. Therefore my signature is `391398879885526901013984096355053422^823 mod 1517`, or **1293.**

######"Finally, show that `(M^d)^e = M (mod N)`":<br>
The **sign** equation is `s = M^d mod N`, and the **verify** equation checks that `s^e mod N` equals `M mod N`. By subsituting for s in the verify equation, we get `(m^d)^e mod N` equals `M mod N`. 

Here are my input values for **sign** and **verify**:<br>
  - **s** = `M^d mod N = 1293`<br>
  - check that `(m^d)^e mod N` equals `M mod N`:<br>
    - `(m^d)^e mod N = 1241`<br>
    - `M mod N = 1241.`<br>
  - Both sides equal 1241, therefore **verify** returns `True`!<br>

<br>

##### Part D:
If Bob's public key is (391, 17), we need to find the two primes p and q that factor 391. With an educated guess (using the knowledge that 391^(1/2) is ~19.7), I found p and q to be 17 and 23. With this information we can discover Bob's private key:<br>
Ø = `(p-1)(q-1) = 352`<br>
e = `17`<br>
d = `modular inverse (e, Ø) = 145`<br>

**Alice needs to raise her message to the Bob's private key d, which is 145.**

___
#### 8) Darn, not another RSA problem!
##### Part A:
*"Signing involves decryption, and is therefore risky. Show that if Bob agrees to sign anything he is asked to, Eve can take advantage of this and decrypt any message sent by Alice to Bob."*

If Alice sends an encripted message to Bob and Bob is suggestible enough to sign anything Eve gives him, all Eve to do is ask Bob to sign the message Alice sent to him. To sign Alice's message he must decrypt it with his private key. Once Bob signs Alice's encrypted message, all Eve needs to do is verify his signature using his public key *e*:
- Alice encrypts a message to Bob using his public key *e*.
- Eve intercepts the encrypted message and asks Bob to sign it. 
- Bob, naive and still full of hope, agrees to sign the message, which requires the message's decryption using his private key *d*.
- Eve uses Bob's public key *e* to effectively "unsign" it and recieve Alice's decrypted message.

##### Part B:
*"Describe a way in which Eve can nevertheless still decrypt messages from Alice to Bob, by getting Bob to sign messages whose signatures look random."*

Bob's been burned once by Eve's schemes, and won't fall for it again. Unfortunately, Bob has fallen deeply in unrequited love with Eve, and can't refuse signing a message if she asks as long as the message looks like gibberish. Poor Bob.<br>
All Eve needs to do is add another level of encryption - one that Bob cannot decrypt, to make the message look like gibberish:
- Alice encrypts a message to Bob using his public key *e*.
- Eve intercepts the encrypted message and *encrypts it again* using *her* public key **e**. 
- Even then asks Bob to sign the message, which, to Bob, will look like gibberish when he decrypts it. 
- Bob, smitten, signs the "gibberish" message for Eve.
- Eve uses Bob's public key *e* to decrypt the message, which still looks like gibberish.
- Eve uses *her* private key **d** to decrypt the gibberish into Alice's original message.
- Eve disappears into the night with the secret message.
- Bob lives out the rest of his his days in disgrace, pining after a love that could never be.

___

#### 9) Recurrence relation
*How many lines, as a function of n (in Θ(·) form), does the following program print? Write a recurrence and solve it. You may assume n is a power of 2.*

The program's recurrence relation:
```
T(n) = 2(T(n/2)) + 1
```
Assuming n is a power of 2, T(n) effectively becomes n-1:
```
T(n) = n-1
T(1) = 0
```
And in terms of Big-Θ notation:
```
Θ(n)
```
___
#### 10) Majority Element
##### Part A: 

O(*n*log*n*) time algorithm:
```py
def majority(a):
    if len(a) == 0:
        return None
    if len(a) == 1:
        return a[0]
    half = len(a) // 2
    left = majority(a[0:half])
    right = majority(a[half:])
    if left == right:
        return left
    if a.count(left) > half:
        return left
    if a.count(right) > half:
        return right
    return None
```
This algorithm uses the divide and conquer approach and results in O(*n*log*n*) time.

##### Part B:
Linear time algorithm:
```py
def majority(a):
    count = 0
    for x in a:
        if count == 0:
            candidate = x;
        if x == candidate:
            count += 1
        else:
            count -= 1
    if a and a.count(candidate) > len(a) // 2:
        return candidate
    return None
```
This algorithm essentially does what the Dasgupta book hints at, but in a more efficient way. It "pairs up" two elements and looks at each pair - then, rather than "discarding" or "keeping" any elements, it uses a counter to add or subtract from the current candidate's score. After going through the list, the candidate will reflect the most frequent element, if one exists. The final *if* statement ensures that the candidate is indeed the majority element before returning it; otherwise it returns None.


