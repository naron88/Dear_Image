# notebooks/gqa 수정 파일

import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
from PIL import Image
import requests
from io import BytesIO

def exe_gqa(imageURL, chat, interpreter, prompter, generator):
    image = Image.open(imageURL)
    image.thumbnail((640,640),Image.Resampling.LANCZOS)
    init_state = dict(
    IMAGE=image.convert('RGB')
    )

    question = chat
    prog,_ = generator.generate(dict(question=question))
    result, prog_state, html_str = interpreter.execute(prog,init_state,inspect=True)
    return html_str

def exe_imageEdit(imageURL, chat, interpreter, generator):
    # URL에서 이미지 다운로드
    response = requests.get(imageURL)
    image_data = response.content

    # 이미지 데이터를 PIL Image로 열기
    image = Image.open(BytesIO(image_data))

    image.thumbnail((640,640),Image.Resampling.LANCZOS)
    init_state = dict(
    IMAGE=image.convert('RGB')
    )

    instruction = chat
    prog,_ = generator.generate(instruction)
    result, prog_state, html_str = interpreter.execute(prog,init_state,inspect=True)
    
    return result