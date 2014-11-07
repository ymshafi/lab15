#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 4


class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "green")
		self.up.grid(row=0,column=1)
					
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.moveUp)
                
                self.up = Button(self.myContainer1)
		self.up.configure(text="Down", background= "green")
		self.up.grid(row=1,column=1)
					
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.moveDown)
                
                self.up = Button(self.myContainer1)
		self.up.configure(text="Left", background= "green")
		self.up.grid(row=1,column=0)
					
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.moveLeft)
		
		  
                self.up = Button(self.myContainer1)
		self.up.configure(text="Right", background= "green")
		self.up.grid(row=1,column=3)
					
		# "Bind" an action to the first button												
		self.up.bind("<Button-1>", self.moveRight)
                
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		self.animate()

		
	def moveUp(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
                if y1 > 10:
                    drawpad.move(player,0,-10)
                if y1 < 10:
                    return
                    
        def moveDown(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
                if y2 < 320:
                    drawpad.move(player,0,10)
                if y2 > 319:
                    return 
        def moveLeft(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
                if x1 > 1:
                    drawpad.move(player,-10,0)
                if x1 < 1:
                    return
        def moveRight(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
                if x2 < 480:
                    drawpad.move(player,10,0)
                if x2 > 480:
                    return  
         
        # Animate function that will bounce target left and right, and trigger the collision detection  
	def animate(self):
	    global direction
            global drawpad
            global player
            global target
            x1, y1, x2, y2 = drawpad.coords(target)
            if x1 < 1:
                direction = 1
            if x2 > drawpad.winfo_width():
                direction = -1
            drawpad.move(target,direction,0)
            didwehit = self.collisionDetect()
            if didwehit == True:
                return
            else:
                drawpad.after(1, self.collisionDetect)
                drawpad.after(1, self.animate)
	    tx1,ty1,tx2,ty2 = drawpad.coords(target)
	    
	    # Insert the code here to make the target move, bouncing on the edges    
	        
	        
            
            
            #  This will trigger our collision detect function
            didwehit = self.collisionDetect()
            # Use the value of didWeHit to create an if statement
            # that determines whether to run drawpad.after(1,self.animate) or not
            
	# Use a function to do our collision detection
	def collisionDetect(self):
                global target
		global drawpad
                global player
                # Get the co-ordinates of our player AND our target
                x1,y1,x2,y2 = drawpad.coords(player)
                tx1,ty1,tx2,ty2 = drawpad.coords(target)
                if (x1 > tx1 and x2 < tx2) and (y1 > ty1 and y2 < ty2):
                    return True
                else:
                    return False 

                # Do your if statement - remember to return True if successful!                
		
myapp = MyApp(root)

root.mainloop()