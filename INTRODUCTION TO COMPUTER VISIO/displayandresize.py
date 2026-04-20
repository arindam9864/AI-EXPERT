import cv2
import os

# ---- Step 1: Give correct image path ----
image_path = "example.jpg"   # change this if needed

# Optional: print current folder to debug
print("Current Working Directory:", os.getcwd())

# ---- Step 2: Load image ----
image = cv2.imread(image_path)

# ---- Step 3: Check if image loaded ----
if image is None:
    print("❌ Error: Image not found. Check file name/path.")
    exit()

# ---- Step 4: Create resizable window ----
cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)

# ---- Step 5: Resize window (not image) ----
cv2.resizeWindow('Loaded Image', 800, 500)

# ---- Step 6: Show image ----
cv2.imshow('Loaded Image', image)

# ---- Step 7: Wait for key press (IMPORTANT) ----
key = cv2.waitKey(0)

# Optional: press 'q' to close
if key == ord('q'):
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()

# ---- Step 8: Print image properties ----
print(f"✅ Image Dimensions: {image.shape}")
