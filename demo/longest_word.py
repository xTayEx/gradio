import gradio as gr

gr.reset_all()


def longest_word(text):
    words = text.split(" ")
    lengths = [len(word) for word in words]
    return max(lengths)

ex = "The quick brown fox jumped over the lazy dog."

io = gr.Interface(longest_word, "textbox", "label", interpretation="default", examples=[[ex]])

io.test_launch()
io.launch()