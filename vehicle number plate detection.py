import cv2
import pytesseract
l=0
a=[]
pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract'
img=cv2.imread("C:\\Users\\admin\\Desktop\\1.jpg")
g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
g=cv2.bilateralFilter(g,250,90,190)
ret,thresh=cv2.threshold(g,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
t=pytesseract.image_to_string(thresh,lang="eng")
cv2.imshow("1",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("THE NUMBER IS:",t)
for i in range(0,len(t)):
    if t[i]=='T':
        l=i
        break
for j in range(l,len(t)):
    if t[j].isupper():
        a.append(t[j])
    elif t[j].isnumeric():
        a.append(t[j])
print(*a)

