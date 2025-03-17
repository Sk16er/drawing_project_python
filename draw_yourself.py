import cv2
import turtle
import numpy as np

# Step 1: Capture image from webcam
def capture_image():
    cam = cv2.VideoCapture(0)
    print("Press SPACE to capture the image.")
    
    while True:
        ret, frame = cam.read()
        cv2.imshow("Press SPACE to Capture", frame)
        
        if cv2.waitKey(1) & 0xFF == ord(' '):
            img = frame
            break
    
    cam.release()
    cv2.destroyAllWindows()
    return img

# Step 2: Process the image (resize, grayscale, better threshold)
def process_image(img, width=120, height=120):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Grayscale
    resized = cv2.resize(gray, (width, height))  # Resize for turtle
    # Apply adaptive threshold for better detail
    bw = cv2.adaptiveThreshold(
        resized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )
    return bw

# Step 3: Draw using Turtle
def draw_with_turtle(bw_image):
    turtle.bgcolor("white")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.colormode(255)
    turtle.tracer(0, 0)  # No animation for speed

    screen_width = 800
    screen_height = 800
    turtle.setup(screen_width, screen_height)

    height, width = bw_image.shape
    pixel_size = min(screen_width // width, screen_height // height)

    start_x = -width * pixel_size // 2
    start_y = height * pixel_size // 2

    turtle.penup()

    # Draw pixel by pixel
    for i in range(height):
        for j in range(width):
            color = bw_image[i][j]
            if color == 0:  # Black
                x = start_x + j * pixel_size
                y = start_y - i * pixel_size
                turtle.goto(x, y)
                draw_dot(pixel_size)

    turtle.update()
    turtle.done()

def draw_dot(size):
    turtle.begin_fill()
    turtle.circle(size // 2)
    turtle.end_fill()

# Main Function
def main():
    img = capture_image()
    bw_image = process_image(img)  # Now better thresholding + resized image
    draw_with_turtle(bw_image)     # Turtle draws with circular dots now

if __name__ == "__main__":
    main()
