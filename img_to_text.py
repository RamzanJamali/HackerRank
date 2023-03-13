from PIL import Image, ImageFilter, ImageEnhance
import pytesseract
import cv2
import xlsxwriter
pytesseract.pytesseract.tesseract_cmd = r"D:\SponsorYou\tesseract.exe"
# Opens a image in RGB mode
im = Image.open(r"image_b7.jpeg")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

crop_size = 22.3
crops = 10
# Setting the points for cropped image

workbook = xlsxwriter.Workbook('company_b7.xlsx')
worksheet = workbook.add_worksheet("sheet1")
row = 1
col = 0

left = 0
right = 40
ranges = range(crops)
l = [0, 40, 340, 425, 600, 735, 930, 1080, 1240]
r = [40, 310, 420, 560, 730, 910, 1070, 1235, 1390]

while True:
    i = ranges[row - 1]
    # 0-40, 40-310, 340-420, 425-560, 600-730, 735-910, 930-1070, 1080-1235, 1240-1390
    
    bottom = 1 + crop_size + (crop_size * i)
    top = 1 + (crop_size * i )

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    # Shows the image in image viewer
    
    basewidth = (right - left) * 2.4
    wpercent = (basewidth/float(im1.size[0]))
    hsize = int((float(im1.size[1])*float(wpercent)) * 2)
    im1 = im1.resize((int(basewidth),hsize), Image.Resampling.LANCZOS)
    im1.save("temp.jpeg")
    #im1.show()

    # Grayscale, Gaussian blur, Otsu's threshold
    image = cv2.imread('temp.jpeg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    
    # Morph open to remove noise and invert image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening
    #cv2.imshow('invert', invert)
    #cv2.waitKey()

    # Perform text extraction
    data = pytesseract.image_to_string(gray, lang='eng', config='--psm 7')
    print(data)
    worksheet.write(row, col, data)
    row += 1
    #os.remove('temp.jpg')
    if i == ranges[-1] and col == 8:
        break
    if i == ranges[-1]:
        i = 0
        col += 1
        row = 1
        left = l[col]
        right = r[col]


    
    

workbook.close()