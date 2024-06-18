from spicyChat.spicychat import spicy

auth = ""
char_id = ""
conv_id = ""

s = spicy(
    auth=auth
)
while True:
    msg = input("You: ")
    high = s.send_message(msg, char_id, conv_id)
    print(high)
