import AutoType as at
import MKtoArray as mkta
import Response as res
import time
import random
import os

# Path: src/main.py

def main():
    if os.path.exists("outputraw.txt"):
        os.remove("outputraw.txt")
    raw = open("outputraw.txt", "w")
    random.seed()
    # These are hardcoded for MY computer. You will need to change them for yours, if you wish to automatically run this program. Otherwise, keep them commented out.
    # at.Goto(x=416, y=49)
    # at.Click(x=416, y=49)
    # at.Goto(x=175, y=397)
    # at.Click(x=175, y=397)

    
    # Here's a short version on how to get your coordinates:
    # 1. Make a new file (not in src). Call it whatever you want, for this walkthrough, I'll call it "coordinates.py"
    # 2. In that file, put this code:
    # import pyautogui
    # while 1:
    #     try:
    #         x, y = pyautogui.position()
    #         positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
    #         print(positionStr, end="")
    #         print("\b" * len(positionStr), end="", flush=True)
    #     except KeyboardInterrupt:
    #         print("\nDone.")
    # 3. Run the file. It will print out the coordinates of your mouse. On windows, press Control+C to stop the program, on a Mac, RIP.
    # 4. Copy the coordinates that you want to click, and paste them into the Goto and Click functions above.


    # This just makes the program wait, so it doesn't start typing before you have a chance to click on the text box.
    time.sleep(5) # Change this number as you see necessary.

    # Get the response from the GPT-3.5 API. If you don't have an API key, grab one from OpenAI's API page.
    # Note, however, this does cost money. Alternatively, you can just copy paste a response from ChatGPT.
    # To do that instead, comment out the line below, and uncomment the line below that.
    response = res.GetResponse("Write a short paragraph about the TV show \"The Office\".")
    # response = "ChatGPT copied response here."
    raw.write(response)
    raw.close()
    responseArray = mkta.markdown_to_array(response)
    justDidSomething = False
    for segment in responseArray:
        typoOrPause = random.randint(0, 10)
        if segment == "BOLD_START":
            at.Bold()
        elif segment == "BOLD_END":
            at.Bold()
        elif segment == "ITALIC_START":
            at.Italic()
        elif segment == "ITALIC_END":
            at.Italic()
        elif segment == "UNDERLINE_START":
            at.Underline()
        elif segment == "UNDERLINE_END":
            at.Underline()
        elif segment == "RESET":
            at.Bold()
            at.Italic()
            at.Underline()
        elif typoOrPause == 0 and justDidSomething == False:
            time.sleep(random.randint(1, 3))
            at.type(segment, interval=0.01)
            justDidSomething = True
        elif typoOrPause == 1 and justDidSomething == False:
            # make a typo
            typo = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+[]{};':\",./<>?")
            at.type(typo, interval=0.01)
            time.sleep(random.randint(1, 2))
            # Delete the typo
            at.type("\b", interval=0.01)
            #type the correct character
            at.type(segment, interval=0.01)
            justDidSomething = True
        else:
            at.type(segment, interval=0.01) 
            justDidSomething = False


if __name__ == "__main__":
    main()