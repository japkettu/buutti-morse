# Morse.py

Python kirjasto ja komentoriviohjelma morsekoodin kääntämiseen. Lukee tiedostosta listan sanoja, muuttaa tekstin morsekoodiksi (encode) tai morsekoodin tekstiksi (decode). Tallentaa käännetyt sanat käyttäjän määrittelemään tiedostoon. Toimiakseen oikein input-tiedostossa saa olla vain yksi sana rivillään.



## Käyttö:



```sh
$ python morse_test.py -h

usage: morse_test.py [-h][-i input file] [-o output file] mode

positional arguments:

  mode            decode/encode

optional arguments:

  -h, --help      show this help message and exit

  -i input file   input file

  -o output file  output file

Convert text to morse:

python morse_test.py -i path/to/text -o path/to/morse encode

Convert morse to text:

python morse_test.py -i path/to/morse -o path/to/text decode
```


