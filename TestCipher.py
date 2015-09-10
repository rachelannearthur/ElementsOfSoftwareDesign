#  File: TestCipher.py

#  Description: Program that uses two ciphers to encode and decode strings

#  Student Name: Rachel-Anne Arthur

#  Student UT EID: ra26928

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: February 7, 2014

#  Date Last Modified: February 7, 2014


import string

# Create global variables for use in both ciphers
plainTxt = list(string.ascii_lowercase)
# Create global variable for use in substitution cipher
cipher = "q a z w s x e d c r f v t g b y h n u j m i k o l p"
cipher = cipher.split(" ")

# Function that encodes a string using the substituion cipher
def substitution_encode (strng):
  output = '' 
  for ch in strng:
    if (ch > 'z' or ch < 'a'):
      output += ch
    else:
      idx = ord(ch) - ord('a')
      output += cipher[idx]
  return output

# Function that decodes an encoded string using the substitution cipher
def substitution_decode (strng):
  output = ''
  for ch in strng:
    if (ch > 'z' or ch < 'a'):
      output += ch
    else:
      idx = cipher.index(ch)
      output += plainTxt[idx]
  return output

# Function the encodes a string using a vigenere cipher
def vigenere_encode (strng, passwd):
  passwd = elongate_string (strng, passwd)
  output = ''
  for i in range (len(strng)):
    ch = strng[i]
    elt = passwd[i]
    if (ch > 'z' or ch < 'a'):
      output += ch
    else:
      idx = ((ord(ch) - ord('a')) + (ord(elt) - ord('a'))) % 26
      output += plainTxt[idx]
  return output


# Function that elongates a string to the length of another
def elongate_string (strng, passwd):
  newpasswd = '' 
  if len(strng) > len(passwd):
    count = 0
    for i in range(len(strng)):
      ch = strng[i]
      if (ch > 'z' or ch < 'a'):
        newpasswd += ch
      else:
        newpasswd += passwd[count]
        count += 1
        if (count > (len(passwd) - 1)):
          count = 0
  return newpasswd

#Function that decodes an encoded string using the substitution cipher
def vigenere_decode (strng, passwd):
  passwd = elongate_string (strng, passwd)
  output = ''
  for i in range (len(strng)):
    ch = strng[i]
    elt = passwd[i]
    if (ch > 'z' or ch < 'a'):
      output += ch
    else:
      idx = (ord(ch) - ord('a')) - (ord(elt) - ord('a')) % 26
      output += plainTxt[idx]
  return output 

def main():
  # open file for reading
  in_file = open ("./cipher.txt", "r")

  # print header for substitution cipher
  print ("Substitution Cipher")
  print ()

  # read line to be encoded
  line = in_file.readline()
  line = line.strip()

  # encode using substitution cipher
  encoded_str = substitution_encode (line)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded
  line = in_file.readline()
  line = line.strip()

  # decode using substitution cipher
  decoded_str = substitution_decode (line)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()

  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # encode using vigenere cipher
  encoded_str = vigenere_encode (line, passwd)

  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Encoded Text: " + encoded_str)
  print ()

  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()

  # decode using vigenere cipher
  decoded_str = vigenere_decode (line, passwd)

  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print ()

  # close file
  in_file.close()

main() 
