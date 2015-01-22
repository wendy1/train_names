
''' '''
# this nicely gets an input and then displays it
import androidhelper
droid = androidhelper.Android()
name = droid.dialogGetInput("Hello!", "What is your name?")
print str(name)  # name is a namedtuple
if name.result is None:
	droid.makeToast('Cancel was pressed')
else:
	droid.makeToast("Hello, %s" % name.result)
''' '''

'''
# This one does a nice set of toasts
import androidhelper
droid = androidhelper.Android()

for i in range(10):
	droid.makeToast('One %d \nTwo %d' % (i, 2*i))
'''

''' 
# the following seems to work fine
import androidhelper
from kivy.app import App
from kivy.uix.button import Button
 
class TestApp(App):
	def buttonPress(self,instance):
	    droid = androidhelper.Android()
	    line = droid.dialogGetInput()
    	    s = 'Hello %s' % line.result
            droid.makeToast(s)
 
    def build(self):
	    btn1 = Button(text='Hello world 1')
        btn1.bind(on_press=self.buttonPress)
        return btn1
 
TestApp().run()'''