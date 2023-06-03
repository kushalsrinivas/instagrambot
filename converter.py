import cv2
import os
# open image
def converter():
    from PIL import Image
    for image in os.listdir('images'):
        if image.endswith('jpg'):
    # open image
            try:
                img = Image.open(f'images/{image}')

                # set the desired width for the image
                width = 1080

                # calculate the height based on the aspect ratio of the original image
                height = int((width / float(img.size[0])) * img.size[1])
                print(height)
                # resize the image
                img = img.resize((width, height))

                # save the resized image
                img.save(f'images/reformatted/{image}')
            except Exception as e:
                print(e)
                pass
converter()