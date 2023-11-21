import time

def dance_a(name,spaces):
    print("     ","      / "," *FELIZ{}NAVIDAD* ".format(spaces), "\      ")
    print("     ","(°u°)/","       *{}*         ".format(name)," \(°u°)")
    print("     ","<( )","             *{}*      ".format(name)," ( )>")
    print("     "," /  \ ","  *PASALA{}SUPER*     ".format(spaces),"/  \ ")

def dance_b(name,spaces):
    print("    ","\      ","   *FELIZ{}NAVIDAD*    ".format(spaces),"    / ")
    print("    "," \(°u°)","          *{}*       ".format(name),"(°u°)/")
    print("     "," ( )>","       *{}*            ".format(name),"<( )",)
    print("     "," /  \ ","  *PASALA{}SUPER*     ".format(spaces),"/  \ ")

def dance_man(x,y):
    for a in range(200):
        dance_a(x,y)
        time.sleep(.5)
        dance_b(x,y)
        time.sleep(.5)

def get_spaces(x):
    x=x.upper()
    spaces=""
    for i in x:
        spaces=spaces+" "

    return x,spaces