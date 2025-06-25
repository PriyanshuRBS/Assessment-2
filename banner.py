import time
#the banner function
def banner(text):
    #creating spacing between the letters
    bannertext = ' '.join(text.upper())
    #creating the pattern for the upper and lower line. There will be stars on the corners and lines between then
    upperandlowerline = '*'+'-'*(len(bannertext) + 12)+'*'
    #printing the stuff
    print(upperandlowerline) 

    print(f"*---- {bannertext} ! ----*") 

    print(upperandlowerline)