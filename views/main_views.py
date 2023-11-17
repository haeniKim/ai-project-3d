from flask import Flask, Blueprint, request, jsonify
import os
import base64
import deepl

# deepl
translator = deepl.Translator("DEEPL_KEY")

# # + 기능 1. 썸네일 

bp = Blueprint('main', __name__, url_prefix= '/')

@bp.route('/')
def hello():
    return "Hello World"





#Unreal text 통신 확인 -> deepl 영어 번역
@bp.route('/text', methods = ['POST', 'GET'])
def ur_text():
    if request.method == 'POST':
        data = request.get_json()
        prompt = data.get('Prompt')

        prompt_en = translator.translate_text(prompt, target_lang="en-us")
        print(prompt)
        print(prompt_en)

        return f"{prompt_en}"



# 이미지 받기 -> 3D 생성 -> 완료 후 결과 return      / 파일 이름 -> 물체 이름 입력 받아서, 이름명으로 저장, 중복 판단해서 중복시 1,2,3,4 이런식으로
@bp.route('/image', methods=['GET', 'POST'])
def ur_image():
    if request.method == 'POST':
        try:
            image_file = request.files['image']
            file_name = request.args.get('filename')

            decodingFileName = base64.b64decode(file_name)
            decodeStringFileName = decodingFileName.decode('utf-8')
            str2 = 'DecodeString: '
            print(str2+decodeStringFileName+'')

           # print(decodeStringFileName)
            if not image_file:
                return jsonify({'error': '이미지 데이터가 없습니다.'}), 400
            
            #f_name = request.headers.get('filename')
            
            #print(f_name)
            
            image_path = os.path.join('static/data', decodeStringFileName+'.png')
            #image_path = os.path.join('static/data', f_name)

            # 이미지 파일 저장
            image_file.save(image_path)

            return "Success"
            
        except Exception as e:
            return jsonify({'error': str(e)}), 400
