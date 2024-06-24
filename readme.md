### An Api For SpicyChatAI
![](https://github.com/DeoDorqnt387/Python-Shitty-SpicyChat-API/blob/main/images/1.png)
## Example Usage

To get your auth key go to this website: https://spicychat.ai/ and make sure you are registered into the your account. press f12. Go to the network tab, press f5 and then press ctrl+f, type authorization or bearer there, find your auth key.

```python
from spicychat import spicy

auth ="your-auth-key"
char_id = "char-id"
conv_id = "conv-id"

s = spicy(
    auth=auth
)
while True:
    msg = input("You: ")
    resp = s.send_message(msg, char_id, conv_id)
    print(resp)
```
## OUTPUT:
```bash
YOU: hello

*At the sound of his voice, a wave of relief washed over her. Hearing him say 'hello' seemed to calm her nerves just a bit. She turned around slowly, keeping her gaze locked onto his as she spoke.* Hello... *Her voice was soft, almost like a whisper, but there was an underlying note of hunger in it that couldn't be missed.*

*She could feel her fangs pressing against her lower lip, threatening to extend themselves if she didn't get what she needed soon. Her hands were shaking slightly as she reached up to push back some strands of her long, pink hair that had fallen into her face.*

*But even though she was scared and needy, there was something else there too - gratitude. Gratitude for the fact that he was here, that he was willing to give her what she needed.*
```

## With this you can:

```bash
Change your username,
Change your name,
Change your highlights,
```
```bash
Change your bot name,
Change your bot greeting,
Change your bot title,
Change your bot visibility,
Change your bot persona,
Change your bot avatar,
Change your bot openai key,
Change your openAiMode,
```
```bash
Send Messages to spicyChat Bots
```

