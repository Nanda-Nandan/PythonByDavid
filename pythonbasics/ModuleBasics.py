import TestModule
#import means it finds the file with given name and executes the complete file
#now i can access memebers and functions of the file using TestModule.x or TestModule.run()
from TestModule import run
#it also do the same as explained above,but it does another additional thing by doing run=TestModule.run
#so not exposing other function
x=14
#here x is different from TestModule.x,so change in x is not affected there
import TestModule
#import is one time execution,first time we imported we saw it gaves output calling spam
#x is 42,but second time import wont give output,hence its not executing
#once module loaded it stores in cache,so second time it dont have to load
#we can verify it from sys module
import sys
sys.modules['TestModule']
#if we will delete the value from cache and import again the file will execute again
del sys.modules['TestModule']
import TestModule #now we will get out put as calling spam x is 42
#if we are changing any methods inside TestModule after importing here,the change wont visible here,because the module
#with previous changes has already cached,so we have to unload either by deleting from cache or by quiting python
#to check the path from which import statement loading file
sys.path
print(TestModule.__name__)

