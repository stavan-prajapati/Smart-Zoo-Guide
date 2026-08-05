import cv2
import numpy as np

# Create a black image
img = np.zeros((400, 700, 3), dtype=np.uint8)

# Team details
cv2.putText(img, "Stavan Prajapati 24000514", (20, 100),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv2.putText(img, "Het Patel 24000626", (20, 180),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv2.putText(img, "Yash Rathod 24001078", (20, 260),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, 100, 200)

# Display the result
cv2.imshow("Pipeline Test", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()