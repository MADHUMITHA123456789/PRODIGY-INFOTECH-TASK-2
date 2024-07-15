from PIL import Image
def encrypt_image(input_path,output_path,key):
    img=Image.open(input_path)
    pixels=img.load()
    width,height=img.size
    for i in range(width):
        for j in range(height):
            r,g,b=pixels[i,j]
            encrypted_pixel = (b,g,r)
            pixels[i,j] = encrypted_pixel
    img.save(output_path)
    print("We have encrypted the image")
def decrypt_image(input_path,output_path,key):
    img=Image.open(input_path)
    pixels=img.load()
    width,height=img.size
    for i in range(width):
        for j in range(height):
            r,g,b = pixels[i,j]
            decrypted_pixel=(b,g,r)
            pixels[i,j]=decrypted_pixel
    img.save(output_path)
    print("We have decrypted the image  successfully")
input_image=r"C:\Users\Asus\Desktop\Pixel Manipulation\input_image.jpg"
encrypted_image=r"C:\Users\Asus\Desktop\Pixel Manipulation\encrypted_image.jpg"
decrypted_image=r"C:\Users\Asus\Desktop\Pixel Manipulation\decrypted_image.jpg"
#encrypt_image(input_image,encrypted_image,key=None)
decrypt_image(encrypted_image,decrypted_image,key=None)

