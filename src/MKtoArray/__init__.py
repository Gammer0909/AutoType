import re

# Tbh ChatGPT wrote this, I have no clue how this works
def markdown_to_array(text):

    # Split the text into an array of words
    words = re.split(r'(\s+)', text)

    segments = []
    for word in words:
        if re.match(r'\*\*.*\*\*', word):
                # Bold formatting, remove the Markdown markers
                segments.append("BOLD_START")
                segments.append(word.strip('**'))
                segments.append("BOLD_END")
        elif re.match(r'\*.*\*', word):
            # Italic formatting, remove the Markdown markers
            segments.append("ITALIC_START")
            segments.append(word.strip('*'))
            segments.append("ITALIC_END")
        elif re.match(r'__.*__$', word):
            # Underline formatting, remove the Markdown markers
            segments.append("UNDERLINE_START")
            segments.append(word.strip('__'))
            segments.append("UNDERLINE_END")
        else:
            # No formatting, add the word as is
            segments.append(word)

    return segments

