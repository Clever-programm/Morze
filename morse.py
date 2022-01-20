morse = {'A': '.-', 'B': '-...', 'C': '-.-.',
         'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---',
         'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-',
         'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..',
         }

reverse_morse = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
                 '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                 '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                 '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                 '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                 '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                 '-.--': 'Y', '--..': 'Z', '': ' '}


def encode_to_morse(text):  # "sos sos" => "... --- ...  ... --- ..."
    result = ''
         for i in text.upper().split():
                  result += ' '.join([morse[j] for j in i])
                  result += "  "
    return result


def decode_from_morse(code):  # "... --- ...  ... --- ..." => "sos sos"
    #result = ''
    #     for i in code.split():
    #              result += ' '.join([reverse_morse[j] for j in i]).upper()
    #              result += "  "
    #return code
    # не работает-^^^
    result = ""
         for i in code.split(' '):
                  result += reverse_morse[i]
    return result
    # работает-^^^


def main():
    while True:
         answer = input('Хотите ли вы "закодировать" текст или же "декодировать?"')
         if answer == "закодировать":
                  print(encode_to_morse(input("Введите текст:")))
         else:
                  print(decode_from_morse(input("Введите код:")))
