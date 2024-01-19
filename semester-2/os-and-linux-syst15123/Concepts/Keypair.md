A keypair is a security system that requires 2 keys: a **public key** and a **private key**. In order to remotely access anything, you need to generate a public key and a private key.

The private key will be downloaded, while the public key will be stored on the server.

The reason for this is to do a [[Fermat's Little Theorem]] on the keys to verify the user. The strings are generally long enough that it's secure. 

There are multiple formats for the keys. For the purpose of our course, we will be using the most common `.pem` rather than `sha256`. Although I guess it's basically the same at this point, just different encryptions of the same prime number.