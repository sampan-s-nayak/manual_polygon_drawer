import cv2
import numpy as np

# ***** replace with required image path *****
path = "./2.jpeg"
img = cv2.imread(path)
clone = img.copy()
temp = img.copy()

# ***** global variable decleration *****
done = False
points = []
current = (0, 0)
prev_current = (0,0)


def on_mouse(event, x, y, buttons, user_param):
    global done, points, current,temp
    # Mouse callback that gets called for every mouse event (i.e. moving, clicking, etc.)
    if done: # Nothing more to do
        return
    if event == cv2.EVENT_MOUSEMOVE:
        # We want to be able to draw the line-in-progress, so update current mouse position
        current = (x, y)
    elif event == cv2.EVENT_LBUTTONDOWN:
        # Left click means adding a point at current position to the list of points
        print("Adding point #%d with position(%d,%d)" % (len(points), x, y))
        cv2.circle(img,(x,y),5,(0,200,0),-1)
        points.append([x, y])
        temp = img.copy()
    elif event == cv2.EVENT_RBUTTONDOWN:
        # Right click means we're done
        print("Completing polygon with %d points." % len(points))
        done = True

cv2.namedWindow("image")
cv2.setMouseCallback("image", on_mouse)

while(not done):
            # This is our drawing loop, we just continuously draw new images
            # and show them in the named window
            if (len(points) > 1):
                if(current != prev_current):
                    img = temp.copy()
                # Draw all the current polygon segments
                cv2.polylines(img, [np.array(points)], False, (255,0,0), 1)
                # And  also show what the current segment would look like
                cv2.line(img, (points[-1][0],points[-1][1]), current, (0,0,255))

            # Update the window
            cv2.imshow("image", img)
            # And wait 50ms before next iteration (this will pump window messages meanwhile)

            if cv2.waitKey(50) == ord('d'): # press d(done)
                done = True

# User finised entering the polygon points, so let's make the final drawing
img = clone.copy()
# of a filled polygon
if (len(points) > 0):
    cv2.fillPoly(img, np.array([points]), (255,0,0))
# And show it
cv2.imshow("image", img)
# Waiting for the user to press any key
cv2.waitKey(0)
cv2.destroyWindow("image")
