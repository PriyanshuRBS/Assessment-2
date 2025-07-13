import time
#function that prints text and a space, and has a delay for a period of time
def time_text_spacer(text, sleep_time):
    print(text)
    print('')
    time.sleep(sleep_time) #delay
    
#function that prints text and has a delay for a period of time. no spcaes in this one
def time_text(text, sleep_time):
    print(text)
    time.sleep(sleep_time) #delay