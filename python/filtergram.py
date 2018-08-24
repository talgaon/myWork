from Filters import *


#loop thrught the list of pixels

def tal_blackAndWhite(im):
    pixels = list(im.getdata())
    for i in range(len(pixels)):
        pixel = pixels[i] #pixel is a variable that is a tree touple


        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        intensity = red + green + blue
        if intensity <182:
            pixels[i] = 	(0,0,255)
        elif intensity < 364:
            pixels[i] = (0, 128, 128)
        elif intensity <546:
            pixels[i] = 	(65,105,225)
        else:
            pixels[i] = (135,206,250)

    im.putdata(pixels)
    return im

def main():
    inside = load_img("suga.jpg")
    personal_img = tal_blackAndWhite(inside)
    save_img(personal_img, "obamicaon_img.jpg")

    show_img(personal_img)
    #fine the intensity of each of the pixels
    #change the color of the pixels depedning on the intensity
    #if the colors match up swith them to the desired shade
    #return image as an object.
if __name__ == '__main__':
    main()
