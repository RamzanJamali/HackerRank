from PIL import Image, ImageFilter, ImageEnhance
import pytesseract
import cv2
import xlsxwriter
pytesseract.pytesseract.tesseract_cmd = r"D:\SponsorYou\tesseract.exe"
# Opens a image in RGB mode
im = Image.open(r"image_a7.jpeg")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

crop_size = 21.62
crops = 29
# Setting the points for cropped image

workbook = xlsxwriter.Workbook('company_a7.xlsx')
worksheet = workbook.add_worksheet("sheet1")
row = 1
col = 0

left = 0 
right = 40
ranges = range(crops)
l = [0, 40, 310, 420, 530, 790, 960, 1100, 1275, 1380]
r = [40, 300, 410, 525, 780, 940, 1090, 1250, 1360, 1468]

while True:
    i = ranges[row - 1]
    # 0-40, 40-300, 310-410, 420-525, 530-780, 790-940, 960-1090, 1100-1250, 1275-1360, 1380-1470
    
    bottom = crop_size + (crop_size * i)
    top = 0 + (crop_size * i )

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
    if i == ranges[-1] and col == 9:
        break
    if i == ranges[-1]:
        i = 0
        col += 1
        row = 1
        left = l[col]
        right = r[col]


    
    

workbook.close()