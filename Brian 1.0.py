import openai
import gradio

### Enter your own API key from OpenAI into the quotations below
openai.api_key = ""

### Change Brian's personality by replacing the sentence that starts with "You are an"
messages = [{"role": "system", "content": "You are an incredibly smart and sassy personal assistant"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

### Change the title of the web browser by replacing "Brian 1.0"
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Brian 1.0")

### Change to "True" to generate a live link to share while running
demo.launch(share=False)
