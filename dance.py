import time

def dance_a(name,spaces):
    print("     ","      / ","  *FELIZ{}CUMPLE* ".format(spaces), "\      ")
    print("     ","(°u°)/","       *{}*         ".format(name)," \(°u°)")
    print("     ","<( )","             *{}*      ".format(name)," ( )>")
    print("     "," /  \ ","  *PASALA{}SUPER*     ".format(spaces),"/  \ ")
    print("")

def dance_b(name,spaces):
    print("    ","\      ","    *FELIZ{}CUMPLE*    ".format(spaces),"    / ")
    print("    "," \(°u°)","          *{}*       ".format(name),"(°u°)/")
    print("     "," ( )>","       *{}*            ".format(name),"<( )",)
    print("     "," /  \ ","  *PASALA{}SUPER*     ".format(spaces),"/  \ ")
    print("")

def dance_man(x,y):
    for a in range(50):
        dance_a(x,y)
        time.sleep(.3)
        dance_b(x,y)
        time.sleep(.3)

def get_spaces(x):
    x=x.upper()
    spaces=""
    for i in x:
        spaces=spaces+" "

    return x,spaces