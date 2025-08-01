import cv2
import numpy as np
from PIL import Image
import os

def face_recognition_to_string(image_path):
    # 加载图像
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 调用OpenCV进行人脸检测
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # 将人脸区域的像素值转换为字符串
    face_string = ''
    for (x, y, w, h) in faces:
        face_data = gray[y:y+h, x:x+w].flatten()
        face_string += ''.join(str(pixel) for pixel in face_data)

    return face_string

image_path = 'me_image.jpg'  # 替换为你的图像路径
face_string = face_recognition_to_string(image_path)


# 将结果保存到文件
output_file_path = 'face_string.txt'  # 输出文件路径
with open(output_file_path, 'w') as file:
    file.write(face_string)

print(f"Face string has been saved to {output_file_path}")

import mnemonic
import hashlib

def generate_mnemonic_from_file(file_path):
    try:
        # 读取文件内容
        with open(file_path, 'rb') as file:
            file_content = file.read()
        
        # 使用hashlib生成文件内容的哈希值
        hash_object = hashlib.sha256(file_content).digest()
        
        # 创建一个Mnemonic对象，使用英文字典
        mnemo = mnemonic.Mnemonic("english")
        
        # 将哈希值转换为助记词
        mnemonic_phrase = mnemo.to_mnemonic(hash_object)
        
        # 返回生成的助记词
        return mnemonic_phrase
    except Exception as e:
        print(f"Error: {e}")
        return None

# 指定文件路径
file_path = 'face_string.txt'

# 生成并打印助记词
mnemonic_phrase = generate_mnemonic_from_file(file_path)
if mnemonic_phrase:
    print("Generated Mnemonic Phrase:")
    print(mnemonic_phrase)
else:
    print("Failed to generate mnemonic phrase.")
    
