# import time
# import winsound
# code ="....   ....     ....   ..     ...   ....     ..   .....     .   .     ...   ..."
# frequency = 1000
# duration = 500
#
# for char in code:
#     if char == ".":
#         winsound.Beep(frequency, duration)
#         print("Dot")
#     else:
#         time.sleep(1)
#         print("Space")

from assets import logo,alp_to_code_dict

print(logo)
print("Welcome to Morse Code Convertor")
code_to_alp_dict = {value: key for (key, value) in alp_to_code_dict.items()}


def alp_to_code(code_text):
    decode_text = ""
    for char in code_text:
        decode_text += f"{alp_to_code_dict[char]} "
    return f"Decoded text: {decode_text}"


game_continue = True


# while game_continue:
#     code_way = input("Enter 'd' for decoding a morse code or 'c' for generating a morse code.: ")
#     code_text = input("Enter the Code Text: ").upper()
