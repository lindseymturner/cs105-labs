"""

    THIS FILE HANDLES THE GRAPHICS FOR CS 105 LAB 1
    STUDENTS SHOULD RUN IT BUT DO ***NOT*** NEED TO READ OR CHANGE IT
    
"""


try:
    from tkinter import *
except:
    print("tkinter import failed in OverlapTestGraphics")
    print("  other files, e.g. Circle.py, should work, but graphics won't on this machine")

from math import *


def do_range_overlap(min1, max1, min2, max2):
    from Range import rangeOverlap
    return rangeOverlap(min1, max1, min2, max2)


def do_window_overlap(minx1, maxx1, miny1, maxy1, minx2, maxx2, miny2, maxy2):
    from Window import windowOverlap
    print("Testing: >>> windowOverlap(", minx1, ", ", maxx1, ", ", miny1, ", ", maxy1, ", ", minx2, ", ", maxx2, ", ", miny2, ", ", maxy2, ")")
    return windowOverlap(minx1, maxx1, miny1, maxy1, minx2, maxx2, miny2, maxy2)


def do_circle_overlap(x1, y1, r1, x2, y2, r2):
    from Circle import circle_overlap
    print("Testing: >>> circle_overlap(", x1, ", ", y1, ", ", r1, ", ", x2, ", ", y2, ", ", r2, ")")
    return circle_overlap(x1, y1, r1, x2, y2, r2)


def do_circle_rectangle_overlap(center_x, center_y, radius, xmin, xmax, ymin, ymax):
    from CircleRectangle import circle_rectangle_overlap
    print("Testing: >>> circle_rectangle_overlap(", center_x, ", ", center_y, ", ", radius, ", ", xmin, ", ", xmax, ", ", ymin, ", ", ymax, ")")
    return circle_rectangle_overlap(center_x, center_y, radius, xmin, xmax, ymin, ymax)


def do_segment_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
    from Segment import segmentOverlap
    print("Testing: >>> segmentOverlap(", x1, ", ", y1, ", ", x2, ", ", y2, ", ", x3, ", ", y3, ", ", x4, ",", y4, ")")
    return segmentOverlap(x1, y1, x2, y2, x3, y3, x4, y4)

    
def greater_of_two(int1, int2):
    if int1 > int2:
        return int1
    else:
        return int2


def lesser_of_two(int1, int2):
    if int1 < int2:
        return int1
    else:
        return int2


def distance(x1, x2, y1, y2):
    return sqrt(pow((x1-x2),2)+pow((y1-y2),2))


class App:

    def __init__(self, master):

        self.frame = Frame(master)
        self.frame.pack()

        self.canvas = Canvas(self.frame, height=500, width=500, bg="black", highlightthickness=0, cursor="crosshair")
        self.canvas.pack(side=LEFT)
        
        self.frame_side = Frame(self.frame, height=500, width=200, bg="light blue")
        self.frame_side.pack(side=LEFT, expand=1, fill=BOTH)
        self.frame2 = Frame(self.frame_side, height=400, width=200, bg="light blue")
        self.frame2.pack(side=TOP, anchor=N, expand=1)
        self.frame3 = Canvas(self.frame_side, height=100, width=200, bg="light green", highlightthickness=0)
        self.frame3.pack()
        self.temptext = self.frame3.create_text(100,50,text="?")
               
        v = IntVar()
        self.record = IntVar()
        self.button1 = Radiobutton(self.frame2, text="Range Overlap", bg="yellow", variable=v, value=1, command=self.rangebind)
        self.button2 = Radiobutton(self.frame2, text="Window Overlap", bg="green", variable=v, value=2, command=self.windowbind)
        self.button3 = Radiobutton(self.frame2, text="Circle Overlap", bg="orange", variable=v, value=3, command=self.circlebind)
        self.button4 = Radiobutton(self.frame2, text="Circle Rectangle Overlap", bg="purple", variable=v, value=4, command=self.circrectbind)
        self.button5 = Radiobutton(self.frame2, text="Segment Overlap", bg="Red", variable=v, value=5, command=self.segmentbind)
        c = Checkbutton(self.frame2, text="Record Tests", bg="light blue", variable=self.record)
        b = Button(self.frame2, text="Play Back Recorded Test", highlightbackground="light blue", command=self.playback)
        b2 = Button(self.frame2, text="Delete Recorded Tests", highlightbackground="light blue", command=self.clear_recorded)
        
        self.button1.pack(side=TOP, anchor=W)
        self.button2.pack(side=TOP, anchor=W)
        self.button3.pack(side=TOP, anchor=W)
        self.button4.pack(side=TOP, anchor=W)
        self.button5.pack(side=TOP, anchor=W)
        c.pack(side=TOP, anchor=W)
        b.pack(side=TOP, anchor=W)
        b2.pack(side=TOP, anchor=W)
        
        from hccs_testing import starting_a_graphics_test
        starting_a_graphics_test()
        # If I knew how to detect the window closing,
        #  I might call the finished_a_graphics_test function there...

    def playback(self):
        self.clear_canvas()
        file = open("stored_tests.py", "r")
        lines = file.read()
        file.close()
        line = lines.split("\n")
        # This seems to re-write with the 1st test at the bottom, to rotate through...
        file = open("stored_tests.py", "w")
        for i in range(1,len(line)):
            if(len(line[i])>=3):
                file.write(line[i] + "\n")
        #   CUT THE CONDITIONAL ON THE RE-WRITE OF 0 --- Sept '08 davew:
        #   if(self.record.get()):
        file.write(line[0] + "\n")

        file.close()
        # Changed Sept 2007 by davew to allow things that look like real calls from doctest:
        # < func = line[0].split(" ")
        import re 
        func = re.sub("[>(), ]+", " ", line[0] + " ").lstrip(" ").rstrip(" ").split(" ")
        print("Debugging: ", func)
        # End of Dave's 9/07 change
        self.clear_text()
        if(func[0] == "rangeOverlap"):
            self.temp = self.canvas.create_line([func[1],200,func[2],200],fill="yellow")
            self.temp = self.canvas.create_line([func[3],300,func[4],300],fill="yellow")
            if(do_range_overlap(int(func[1]), int(func[2]), int(func[3]), int(func[4]))):
                self.temptext = self.frame3.create_text(100,50,text="Range Overlap")
            else:
                self.temptext = self.frame3.create_text(100,50,text="No Range Overlap")
        elif(func[0] == "windowOverlap"):
            self.temp = self.canvas.create_rectangle([func[1],func[3],func[2],func[4]],outline="green")
            self.temp = self.canvas.create_rectangle([func[5],func[7],func[6],func[8]],outline="green")
            if(do_window_overlap(int(func[1]), int(func[2]), int(func[3]), int(func[4]), int(func[5]), int(func[6]), int(func[7]), int(func[8]))):
                self.temptext = self.frame3.create_text(100,50,text="Window Overlap!")    
            else:
                self.temptext = self.frame3.create_text(100,50,text="No Window Overlap!")    
        elif(func[0] == "circle_overlap"):  # Note #3 and #6 are radii, i.e. may be non-integer
            self.temp = self.canvas.create_oval([int(func[1])-float(func[3]),int(func[2])-float(func[3]),int(func[1])+float(func[3]),int(func[2])+float(func[3])],outline="orange")
            self.temp = self.canvas.create_oval([int(func[4])-float(func[6]),int(func[5])-float(func[6]),int(func[4])+float(func[6]),int(func[5])+float(func[6])],outline="orange") 
            if(do_circle_overlap(int(func[1]), int(func[2]), float(func[3]), int(func[4]), int(func[5]), float(func[6]))):
                self.temptext = self.frame3.create_text(100,50,text="Circle Overlap!")    
            else:
                self.temptext = self.frame3.create_text(100,50,text="No Circle Overlap!")
        elif(func[0] == "circle_rectangle_overlap"):  # Note #3 is radius, i.e. may be non-integer
            self.temp = self.canvas.create_rectangle([func[4],func[6],func[5],func[7]],outline="purple")
            self.temp = self.canvas.create_oval([int(func[1])-float(func[3]),int(func[2])-float(func[3]),int(func[1])+float(func[3]),int(func[2])+float(func[3])],outline="purple")
            if(do_circle_rectangle_overlap(int(func[1]), int(func[2]), float(func[3]), int(func[4]), int(func[5]), int(func[6]), int(func[7]))):
                self.temptext = self.frame3.create_text(100,50,text="Circle Rectangle Overlap!")    
            else:
                self.temptext = self.frame3.create_text(100,50,text="No Circle Rectangle Overlap!")
        elif(func[0] == "segmentOverlap"):
            self.temp = self.canvas.create_line([func[1],func[2],func[3],func[4]],fill="red")
            self.temp = self.canvas.create_line([func[5],func[6],func[7],func[8]],fill="red") 
            if(do_segment_overlap(int(func[1]), int(func[2]), int(func[3]), int(func[4]), int(func[5]), int(func[6]), int(func[7]), int(func[8]))):
                self.temptext = self.frame3.create_text(100,50,text="Segment Overlap!")    
            else:
                self.temptext = self.frame3.create_text(100,50,text="No Segment Overlap!")
        
    def clear_recorded(self):
        file = open("stored_tests.py", "w")
        lines = file.write("")
        file.close()
        
    def clear_canvas(self):
        stufftoclear = self.canvas.find_all()
        (self.min1,self.max1,self.min2,self.max2) = (0,0,0,0) # clear range overlap values
        (self.minx1,self.maxx1,self.miny1,self.maxy1,self.minx2,self.maxx2,self.miny2,self.maxy2) = (0,0,0,0,0,0,0,0) # clear window overlap values
        (self.x1,self.y1,self.r1,self.x2,self.y2,self.r2) = (0,0,0,0,0,0) # clear circle overlap values
        self.horizontal = 0
        self.vertical = 0
        for i in stufftoclear:
            self.canvas.delete(i)

    def clear_text(self):
        stufftoclear = self.frame3.find_all()
        for i in stufftoclear:
            self.frame3.delete(i)

#================================================================================
#Range Overlap        
#================================================================================
    def rangebind(self):
        self.clear_canvas()
        self.canvas.bind("<Button-1>", self.startflatline)
        self.canvas.bind("<B1-Motion>", self.previewflatline)
        self.canvas.bind("<ButtonRelease-1>", self.endflatline)
    
    def startflatline(self, event):
        self.startx = event.x
        self.starty = event.y
        self.temp = self.canvas.create_line([self.startx,self.starty,event.x,self.starty],fill="yellow")
        
    def previewflatline(self, event):
        self.canvas.delete(self.temp)
        self.temp = self.canvas.create_line([self.startx,self.starty,event.x,self.starty],fill="yellow")
        
    def endflatline(self, event):
        self.canvas.delete(self.temp)
        self.temp = self.canvas.create_line([self.startx,self.starty,event.x,self.starty],fill="yellow")
        if(self.min1):
            self.max2 = greater_of_two(self.startx, event.x)
            self.min2 = lesser_of_two(self.startx, event.x)
            self.clear_text()
            if(do_range_overlap(self.min1, self.max1, self.min2, self.max2)):
                self.temptext = self.frame3.create_text(100,50,text="Range Overlap!")
            else:
                self.temptext = self.frame3.create_text(100,50,text="No Range Overlap")
            if(self.record.get()):
                file = open("stored_tests.py", "a")
                file.write(">>> rangeOverlap(" + str(self.min1) + ", " + str(self.max1) + ", " + str(self.min2) + ", " + str(self.max2) + ")\n")
                file.close()
            self.clear_canvas()
        else:
            self.max1 = greater_of_two(self.startx, event.x)
            self.min1 = lesser_of_two(self.startx, event.x)
                
#================================================================================
#Window Overlap
#================================================================================

    def windowbind(self):
        self.clear_canvas()
        self.canvas.bind("<Button-1>", self.startwindow)
        self.canvas.bind("<B1-Motion>", self.previewwindow)
        self.canvas.bind("<ButtonRelease-1>", self.endwindow)
    
    def startwindow(self, event):
        self.startx = event.x
        self.starty = event.y
        self.temp = self.canvas.create_rectangle([self.startx,self.starty,event.x,event.y],outline="green")
        
    def previewwindow(self, event):
        self.canvas.delete(self.temp)
        self.temp = self.canvas.create_rectangle([self.startx,self.starty,event.x,event.y],outline="green")
        
    def endwindow(self, event):
        self.canvas.delete(self.temp)
        self.temp = self.canvas.create_rectangle([self.startx,self.starty,event.x,event.y],outline="green")
        if(self.minx1):
            self.maxx2 = greater_of_two(self.startx, event.x)
            self.minx2 = lesser_of_two(self.startx, event.x)
            self.maxy2 = greater_of_two(self.starty, event.y)
            self.miny2 = lesser_of_two(self.starty, event.y)
            self.clear_text()
            if(do_window_overlap(self.minx1, self.maxx1, self.miny1, self.maxy1, self.minx2, self.maxx2, self.miny2, self.maxy2)):
                self.temptext = self.frame3.create_text(100,50,text="Window Overlap!")
            else:
                self.temptext = self.frame3.create_text(100,50,text="No Window Overlap")
            if(self.record.get()):
                file = open("stored_tests.py", "a")
                file.write(">>> windowOverlap(" + str(self.minx1) + ", "  + str(self.maxx1) + ", "  + str(self.miny1) + ", "  + str(self.maxy1) + ", "  + str(self.minx2) + ", "  + str(self.maxx2) + ", "  + str(self.miny2) + ", "  + str(self.maxy2) + ")\n")
                file.close()
            self.clear_canvas()
        else:
            self.maxx1 = greater_of_two(self.startx, event.x)
            self.minx1 = lesser_of_two(self.startx, event.x)
            self.maxy1 = greater_of_two(self.starty, event.y)
            self.miny1 = lesser_of_two(self.starty, event.y)

#================================================================================
#Circle Overlap
#================================================================================

    def circlebind(self):
        self.clear_canvas()
        self.canvas.bind("<Button-1>", self.startcircle)
        self.canvas.bind("<B1-Motion>", self.previewcircle)
        self.canvas.bind("<ButtonRelease-1>", self.endcircle)
    
    def startcircle(self, event):
        self.startx = event.x
        self.starty = event.y
        self.temp = self.canvas.create_oval([self.startx,self.starty,self.startx,self.starty],outline="orange")
        
    def previewcircle(self, event):
        self.canvas.delete(self.temp)
        difference = distance(event.x,self.startx,event.y,self.starty)
        self.temp = self.canvas.create_oval([self.startx-difference,self.starty-difference,self.startx+difference,self.starty+difference],outline="orange")
            
            
    def endcircle(self, event):       
        self.canvas.delete(self.temp)
        difference = distance(event.x,self.startx,event.y,self.starty)
        self.temp = self.canvas.create_oval([self.startx-difference,self.starty-difference,self.startx+difference,self.starty+difference],outline="orange")
        if(self.x1):
            self.x2 = self.startx
            self.y2 = self.starty
            self.r2 = difference
            self.clear_text()
            if(do_circle_overlap(self.x1, self.y1, self.r1, self.x2, self.y2, self.r2)):
                self.temptext = self.frame3.create_text(100,50,text="Circle Overlap!")
            else:
                self.temptext = self.frame3.create_text(100,50,text="No Circle Overlap")
            if(self.record.get()):
                file = open("stored_tests.py", "a")  # Dave W took out "int" for radii Sept 2011
                file.write(">>> circle_overlap(" + str(self.x1) + ", " + str(self.y1) + ", " + str(self.r1) + ", " + str(self.x2) + ", " + str(self.y2) + ", " + str(self.r2) + ")\n")
                file.close()
            self.clear_canvas()
        else:
            self.x1 = self.startx
            self.y1 = self.starty
            self.r1 = difference

#================================================================================
#Circle Rectangle Overlap
#================================================================================

    def circrectbind(self):
        self.clear_canvas()
        self.canvas.bind("<Button-1>", self.startcircrect)
        self.canvas.bind("<B1-Motion>", self.previewcircrect)
        self.canvas.bind("<ButtonRelease-1>", self.endcircrect)
    
    def startcircrect(self, event):
        self.startx = event.x
        self.starty = event.y
        self.temp = self.canvas.create_oval([self.startx,self.starty,self.startx,self.starty],outline="purple")
        
    def previewcircrect(self, event):       
        if(self.minx1):
            self.canvas.delete(self.temp)
            difference = distance(event.x,self.startx,event.y,self.starty)
            self.temp = self.canvas.create_oval([self.startx-difference,self.starty-difference,self.startx+difference,self.starty+difference],outline="purple")
        else:
            self.canvas.delete(self.temp)
            self.temp = self.canvas.create_rectangle([self.startx,self.starty,event.x,event.y],outline="purple")
        
    def endcircrect(self, event):
        if(self.minx1):
            self.canvas.delete(self.temp)
            difference = distance(event.x,self.startx,event.y,self.starty)
            self.temp = self.canvas.create_oval([self.startx-difference,self.starty-difference,self.startx+difference,self.starty+difference],outline="purple")
            
            self.x2 = self.startx
            self.y2 = self.starty
            self.r2 = difference
            self.clear_text()

            if(do_circle_rectangle_overlap(self.x2, self.y2, self.r2, self.minx1, self.maxx1, self.miny1, self.maxy1)):
                self.temptext = self.frame3.create_text(100,50,text="Circle Rectangle Overlap!")
            else:
                self.temptext = self.frame3.create_text(100,50,text="No Circle Rectangle Overlap")
            if(self.record.get()):
                file = open("stored_tests.py", "a")  # dave W took out "int" for radius Sept 2011
                file.write(">>> circle_rectangle_overlap(" + str(self.x2) + ", " + str(self.y2) + ", " + str(self.r2) + ", " + str(self.minx1) + ", " + str(self.maxx1) + ", " + str(self.miny1) + ", " + str(self.maxy1) + ")\n")
                file.close()
            self.clear_canvas()
        else:
            self.canvas.delete(self.temp)
            self.temp = self.canvas.create_rectangle([self.startx,self.starty,event.x,event.y],outline="purple")
        
            self.maxx1 = greater_of_two(self.startx, event.x)
            self.minx1 = lesser_of_two(self.startx, event.x)
            self.maxy1 = greater_of_two(self.starty, event.y)
            self.miny1 = lesser_of_two(self.starty, event.y)

#================================================================================
#Segment Overlap
#================================================================================

    def segmentbind(self):
        self.clear_canvas()
        self.canvas.bind("<Button-1>", self.startsegment)
        self.canvas.bind("<B1-Motion>", self.previewsegment)
        self.canvas.bind("<ButtonRelease-1>", self.endsegment)
        self.frame.bind("<KeyPress>", self.segmentoptions)
        self.frame.bind("<KeyRelease>", self.segmentendoptions)
        self.frame.focus()
    
    def segmentoptions(self, event):
        if(event.keysym == "Shift_L"):
            self.horizontal = 1
        elif(event.keysym == "Control_L"):
            self.vertical = 1
            
    def segmentendoptions(self, event):
        if(event.keysym == "Shift_L"):
            self.horizontal = 0
        elif(event.keysym == "Control_L"):
            self.vertical = 0
        
    def startsegment(self, event):
        self.startx = event.x
        self.starty = event.y
        self.temp = self.canvas.create_line([self.startx,self.starty,event.x,event.y],fill="red")
        
    def previewsegment(self, event):
        self.canvas.delete(self.temp)
        self.currentx = event.x
        self.currenty = event.y
        if(self.horizontal == 1):
            self.currenty = self.starty
        elif(self.vertical == 1):
            self.currentx = self.startx
        self.temp = self.canvas.create_line([self.startx,self.starty,self.currentx,self.currenty],fill="red")
        
    def endsegment(self, event):
        self.canvas.delete(self.temp)
        self.currentx = event.x
        self.currenty = event.y
        if(self.horizontal == 1):
            self.currenty = self.starty
        elif(self.vertical == 1):
            self.currentx = self.startx
        self.temp = self.canvas.create_line([self.startx,self.starty,self.currentx,self.currenty],fill="red")
        if(self.minx1):
            self.maxx2 = self.currentx
            self.minx2 = self.startx
            self.maxy2 = self.currenty
            self.miny2 = self.starty
            self.clear_text()
            if(do_segment_overlap(self.minx1, self.miny1, self.maxx1, self.maxy1, self.minx2, self.miny2, self.maxx2, self.maxy2)):
                self.temptext = self.frame3.create_text(100,50,text="Segment Overlap!")
            else:
                self.temptext = self.frame3.create_text(100,50,text="No Segment Overlap")
            if(self.record.get()):
                file = open("stored_tests.py", "a")
                file.write(">>> segmentOverlap(" + str(self.minx1) + ", " + str(self.miny1) + ", " + str(self.maxx1) + ", " + str(self.maxy1) + ", " + str(self.minx2) + ", " + str(self.miny2) + ", " + str(self.maxx2) + ", " + str(self.maxy2) + ")\n")
                file.close()
            self.clear_canvas()
        else:
            self.maxx1 = self.currentx
            self.minx1 = self.startx
            self.maxy1 = self.currenty
            self.miny1 = self.starty








root = Tk()

app = App(root)

root.mainloop()


