# README
## Improved Table Cipher
This program allows you to encrypt and decrypt messages using the following method:
1. The key is the amount of columns in the table the original message will be split into.
2. The message is put into the table from left to right, top to bottom.
3. The rows are then inversed, and the encrypted message is written from top to bottom, left to right.

## Installation
1. Make sure to have Python version 3.X installed.
2. Download the code from repository onto your computer.

## Launch
1. Open a terminal or a command prompt.
2. Open folder with the code.
3. Launch program with the following code:
`python ImprovedTableCipher.py`

## Testing
1. Open a terminal or a command prompt.
2. Open folder with the code.
3. Launch the program with the following code: 
`python -m unittest ImprovedTableCipherTests.py`