from aip import AipOcr
import base64


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


APP_ID = '10698781'
API_KEY = 'Hgu9XSdt9Pr69SrvFxDB9Goo'
SECRET_KEY = 'yqiFRf8aoTllDHWCek0EYHBAaAD4uLpY'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

image = get_file_content('test2.jpg')

image_base64 = base64.b64encode(image)

options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"


answer2 = client.basicAccurate(image, options)

print(answer2)