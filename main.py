import pyautogui
import time
import keyboard
import pyperclip
#don't forget to pip install pyautogui and pyperclip in the cmd!

seconds_taken = 0  
number_of_tags_renamed = 0
max_characters = 95
Tag_name_already_present = 0

start_x, start_y = 926, 426  
end_x, end_y = 434, 426  


def check_interruption():
    return keyboard.is_pressed('esc')

def rename_tag():
    global number_of_tags_renamed 
    global max_characters
    global seconds_taken
    global Tag_name_already_present  
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('f2')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    initial_tag = pyperclip.paste()
    print("Initial, unedited tag:", initial_tag)
    num_charcters = len(initial_tag)
    
    if num_charcters >= 95:  #evernote only allows you to have 100 characters in a given note name. This leads to complications if your updated tag prefix makes the note longer than 100 characters, in which case you will have a chopped off prefix. This fixes it by checking and editing the string before entering the new prefix.
        print(f"Error: The string has {initial_tag} characters.")
        pyautogui.press('end')
        pyautogui.press('end')
        characters_to_delete = 100 - (num_charcters)
        if characters_to_delete > 0:
            for _ in range(characters_to_delete):
                pyautogui.press('backspace')
    else:
        print("String is within the allowed length.")

    pyautogui.press('home')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    
    #use as many "backspace" and "right" functions as you need to delete the tag 
    
    pyautogui.write("RENAMED TAG TEXT GOES HERE")
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c') 
    copied_text = pyperclip.paste()
    print("Most Recent Edit:", copied_text)
    pyautogui.press('left')
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=0.00005)
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.mouseUp()
    pyautogui.click()
    check_for_Tag_name_already_present = pyperclip.paste()

    #the module below checks if there is a "Tag name already present" error. The macro solves this error by adding a "+" to the end of the tag. It checks for this error by dragging the mouse across the screen in the place that the error message usually occurs, and copying any text it finds. If the error message is in the text, it will add a "+" to the end of the string, solving this error.

    
    if "Tag name already present" in check_for_Tag_name_already_present:
        print("Tag name already present. Adding + to the end")
        pyautogui.moveTo(441, 385, duration=1)
        pyautogui.click()
        pyautogui.press('end')
        pyautogui.write("+")
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        updated_text = pyperclip.paste()
        print("Updated tag:", updated_text)
        Tag_name_already_present += 1


    else:
        print("No errors found. Continuing to the next tag")

    time.sleep(0.5)
    pyautogui.press('enter')    
    number_of_tags_renamed += 1
    seconds_taken += 18

X = True

while X:
    if check_interruption() == True:
        print("Program interrupted by user.")
        break

    if number_of_tags_renamed == 350:
        print("Renaming paused due to reaching 350 tags completed")
        time.sleep(10000000)
        break

    time.sleep(15)
    rename_tag() 
    print(f"This super OP macro has renamed {number_of_tags_renamed} tags in {seconds_taken} seconds so far")
    print(f"This macro has also successfully solved {Tag_name_already_present} 'tag name already present' errors.")
    print("+=======================================================+")
