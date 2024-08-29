# RSA Encryption/Decryption

This project implements a basic RSA encryption and decryption system in Python. The script can generate RSA public and private keys, encrypt messages, and decrypt encrypted messages. It includes several standard algorithms for cryptographic operations and number theory computations.

## Features

- **Linear Congruential Generator (LCG):** Generates pseudo-random numbers.
- **Prime Number Check:** Utilizes the Miller-Rabin primality test.
- **Karatsuba Multiplication:** Efficiently multiplies large integers.
- **Extended Euclidean Algorithm:** Computes the modular inverse.
- **Chinese Remainder Theorem:** Improves decryption performance.
- **Message Encryption & Decryption:** Supports variable block sizes.
- **ASCII and General Encoding:** Allows encryption in ASCII or other character sets.


## Usage

1. **Clone the repository**
    ```sh
    git clone https://github.com/ftm-zarin/rsa-encryption.git
    cd rsa-encryption
    ```

2. **Run the script**
    ```sh
    python rsa_encryption.py
    ```

### Key Generation

To generate new RSA public and private keys:
```plaintext
Do you want to generate new public and private keys? (YES or NO)
```

### Encryption

To encrypt a message:
```plaintext
Would you like to encrypt or decrypt? (Enter E or D)
```
Specify the block size and encoding type:
```plaintext
How long is the block size?
Do you want to use ASCII (1) or another (2) language? (Enter 1 or 2)
```

Provide the message and optionally specify a public key file:
```plaintext
What would you like to encrypt?
Do you want to encrypt using your own public key? (YES or NO)
Enter the file name that stores the public key: 
```

### Decryption

To decrypt a message:
```plaintext
Would you like to encrypt or decrypt? (Enter E or D)
```
Specify the block size and encoding type:
```plaintext
How long is the block size?
Do you want to use ASCII (1) or another (2) language? (Enter 1 or 2)
```

Provide the encrypted message for decryption:
```plaintext
What would you like to decrypt?
```

## Files

- **public_key:** Stores the public key `(e, n)`.
- **private_key:** Stores the private key `(d, n)` and primes `(p, q)`.

## Code Structure

- **LCG:** Generates random numbers for RSA operations.
- **gcd:** Computes the greatest common divisor of two numbers.
- **Miller-Rabin Test:** Checks if a number is prime.
- **Karatsuba Multiplication:** Efficient multiplication of large numbers.
- **Extended Euclidean Algorithm:** Computes the modular inverse.
- **Chinese Remainder Theorem:** Used for efficient decryption.
- **key_maker:** Generates RSA public and private keys.
- **encrypt:** Encrypts messages using the provided public key.
- **decrypt:** Decrypts messages using the provided private key.
- **main:** Main function handling user interaction and operations.

## Security Note

This implementation of RSA encryption is primarily for educational purposes. For production-level security, consider using established libraries and frameworks that provide robust and well-tested implementations.

## Contribution

Feel free to open issues or submit pull requests if you find bugs or have suggestions for improvements.

---

Happy encrypting! If you have any questions or need further assistance, don't hesitate to reach out.
