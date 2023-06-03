import os
def cleaner():
    try:
        a  = ('.jpg.REMOVE_ME','.jpg')
        for image in os.listdir('images'):
            if image.endswith(a):
                os.remove(f'images/{image}')
        for image in os.listdir('images/reformatted'):
            if image.endswith(a):
                os.remove(f'images/reformatted/{image}')
    except Exception as e:
        print(e)
        pass

        # specify the directory path where the files should be removed



cleaner()
