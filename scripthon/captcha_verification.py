from PIL import Image, ImageDraw, ImageFont
import random


def generate_captcha_code(length=6):
    _chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    _code = ''.join(random.choice(_chars) for _ in range(length))
    return _code


def create_captcha_image(code, width=200, height=80):
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size=36)

    for x in range(0, width, 50):
        for y in range(height):
            if random.random() > 0.8:
                draw.point((x, y), fill='black')

    for i, char in enumerate(code):
        draw.text((20 + i * 30, 20), char, font=font, fill='black')

    return image


def verify_captcha(code, response):
    return code == response


if __name__ == "__main__":
    captcha_code = generate_captcha_code()
    captcha_image = create_captcha_image(_code)
    captcha_image.show()

    user_response = input("Enter the characters you see in the CAPTCHA image: ")

    if verify_captcha(captcha_code, user_response):
        print("CAPTCHA verification successful!")
    else:
        print("CAPTCHA verification failed. Please try again.")
