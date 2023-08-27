# AutoType

AutoType is a python macro that automatically types a GPT-3.5 response, while looking like a human has written it, with random typos, and pauses as if a human is thinking.

## How it works

First, the script gets a response from GPT-3.5
Next, the response is split into seperate words, with Markdown Syntax being split as so:

| Markdown | Split |
|----------|-------|
| ** | BOLD_START/BOLD_END |
| * | ITALIC_START/ITALIC_END |
| __ | UNDERLINE_START/UNDERLINE_END |

Here's an example sentence that shows what it looks like before and after the split:

```python
example = "This is a **bold** word, and this is an *italic* word, and this is an __underlined__ word."
segmented_example = markdown_to_array(example)
print(segmented_example)
# Outputs
# ['This', ' ', 'is', ' ', 'a', ' ', 'BOLD_START', 'bold', 'BOLD_END', ' ', 'word,', ' ', 'and', ' ', 'this', ' ', 'is', ' ', 'an', ' ', 'ITALIC_START', 'italic', 'ITALIC_END', ' ', 'word,', ' ', 'and', ' ', 'this', ' ', 'is', ' ', 'an', ' ', 'UNDERLING_START', 'underlined', 'UNDERLINE_END', ' ', 'word.']
```

The list of words are then looped through, and the script will type each word, with a delay of 0.1 seconds between each word.

Also, the script will periodically pause as if a human thinking, and will randomly make typos (That do get fixed!).

Any more questions about how it works? Look at `src/main.py`, it's all there.

## Installation and use

First, clone the Repo, `git clone https://github.com/Gammer0909/AutoType.git`

Next, install the requirements by running `pip install -r requirements.txt` (If anything's missing, add it to the requirements.txt file and make a PR!)

If you wish to use the GPT-3.5 API, you will need an OpenAI API key with funding. Put this file in the src/ folder and name it `key.txt`

Finally, run the script with `python src/main.py`

Once you've run the script, you will have 5 seconds to click over to whatever you want to type in, eg. a Google Doc, Notepad file, etc.

## Contributing

If you wish to contribute, please make a PR with your changes. If you have any questions, feel free to open an issue.

## Why Did you Make this?

In english class, my teacher was talking about the tool she has installed that will let her see if we cheat using ChatGPT, and that "She will know". So, I basically wanted to prove her wrong.
Guess what? I can now. Will I actually use this to cheat? No. This was for educational purposes only, any use outside of the Ethical Use Disclaimer is not my fault.

## License and Ethical Use Disclaimer

This project is licensed under a modified MIT License. See the LICENSE file for more information.

This project is for educational purposes only. I am not responsible for any misuse of this project. Please use this project ethically.