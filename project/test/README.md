# What's here

A demonstration of encryption and decryption. 

# How to see it working
```
    echo "hello world -pad" > foo
```
Note the length - if we're using -nopad option, then the size of foo must be a [exact] multiple of 16.
```
    key="12345678123456781234567812345678"
    openssl enc -aes-128-cbc -K "$key" -iv "$key" -nopad -nosalt -a -p -in foo -out foo.aes
```
The terms include: padding, salting, aes-128-cbc. '-a' says let the output be base64. '-p' says print the key and the IV. You may also want to take a look at the [various encoding systems](https://www.skorks.com/2009/08/different-types-of-encoding-schemes-a-primer/).

Once the encrypted file is ready, edit enc.html accordingly; open it in a browser. Open Developer Tools. Open console. Type 'dec' in the console.

# Additional Resources

[Youtube - introduction to symmetric encryption using openssl](https://www.youtube.com/watch?v=bbEFjT9CuVk) 
