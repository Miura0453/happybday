# This is a sample Python script.
import dance as dc
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def start(x):
    name,spaces=dc.get_spaces(x)
    dc.dance_man(name,spaces)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name=input("Name")
    start(name)

