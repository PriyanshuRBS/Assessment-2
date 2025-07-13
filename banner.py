import time
#the banner function
def banner_generator(text):
    #creating spacing between the letters
    bannertext = ' '.join(text.upper())
    #creating the pattern for the upper and lower line. There will be stars on the corners and lines between then
    upperandlowerline = '|'+'-'*(len(bannertext) + 13)+'|'
    #printing the stuff
    print(upperandlowerline) 

    print(f"|----  {bannertext}   ----|") 

    print(upperandlowerline)

def banner_generator_v2(text):
    #creating spacing between the letters
    bannertext = ' '.join(text.upper())
    #creating the pattern for the upper and lower line. There will be stars on the corners and lines between then
    upperandlowerline = '|'+'-'*(len(bannertext) + 12)+'|'
    #printing the stuff
    print(upperandlowerline)  #double upper line 
    print(upperandlowerline) 
    print(f"|----  {bannertext}  ----|") 
    print(upperandlowerline)  #double lower line
    print(upperandlowerline)

