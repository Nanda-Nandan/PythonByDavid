x=42
def spam():
    print('x is',x)
def run():
    print('calling spam')
    spam()
    #show the import message when imported in main function,dont show for other files
    #name is a global variable which stores the name of module
if __name__=='__main__':
    print('running')
    run()

