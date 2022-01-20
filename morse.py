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
                 '-.--': 'Y', '--..': 'Z'}


def encode_to_morse(text):  # "sos sos" => "... --- ...  ... --- ..."
    result = ''
         for i in text.upper().split():
                  result += ' '.join([morse[j] for j in i])
                  result += "  "
    return result


def decode_from_morse(code):  # "... --- ...  ... --- ..." => "sos sos"
    result = ''
         for i in code.split():
                  result += ' '.join([reverse_morse[j] for j in i]).upper()
                  result += "  "
    return code


def main():
    pass
