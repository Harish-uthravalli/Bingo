import keyboard
import random
from gtts import gTTS 
from playsound import playsound
import os



shot_pressed = 0
was_pressed = False
numbers_map = {
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
}
numbers = random.sample(range(1,100),99)
num_count = 0

def listToString(s):  
    str1 = " "  
    return(str1.join(s))

def text_to_speech(strn,num):
    language = 'en'
    output = gTTS(text=strn, lang=language, slow=False)
    output.save(num+'.mp3')
    playsound(num+'.mp3')

while True:
    if keyboard.is_pressed('n'):
        if not was_pressed:
            if num_count<=99:
                num_count = num_count + 1
            number = numbers[num_count]
            if number < 10:
                print("\n NUMBER IS: ",number)
                audio_string = 'zero '+str(number)
                text_to_speech(audio_string,str(number))
            else:    
                print("\n NUMBER IS :",number) 
                split = [str(i) for i in str(number)]
                for i in range(len(split)):
                    split[i] = numbers_map[split[i]]
                split.append(str(number))    
                audio_string = listToString(split)
                text_to_speech(audio_string,str(number))   
                split.clear()
                if str(number)+'.mp3' in os.listdir(os.getcwd()):
                    os.remove(str(number)+'.mp3')
        was_pressed = True   

    elif keyboard.is_pressed("q"):
        if not was_pressed:
            break   
        was_pressed = True 
    elif keyboard.is_pressed("p"):
        if not was_pressed:
            print("\n ",numbers)
        was_pressed = True        
    else:
        was_pressed = False
    