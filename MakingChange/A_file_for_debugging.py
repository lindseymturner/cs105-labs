#
# To debug a Python function,
#  * make sure the function is imported into this file
#      (i.e., use   from buyingThings import can_i_buy_this
#      if you want to debug the can_i_buy_this function from buyingThings)
#  * in this file, call the function you want to debug once (as per the example below)
#  * click to the right of a line number in left margin, to get a 'stop-light' on that line
#  * right-click on this file in the Project pane on the left of your PyCharm window,
#    and choose "Debug ..."
#
#  then debug the program, as illustrated in lecture
#
#  When done, remember to:
#  * stop the program by clicking on the "red box" that indicates that the program is running
#    (if that box is grey rather than red, the program is already stopped)
#  * right-click on "Debug" in your perspectives menu and choose "close"
#


from buyingThings import can_i_buy_this
print("Hoping for False... ",)
print(can_i_buy_this(3, 8, 4, 6, 1.99))
print("Hoping for True...",)
print(can_i_buy_this(3, 8, 4, 6, 1.19))
