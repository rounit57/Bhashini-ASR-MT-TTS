from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import json
import requests
import yaml
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
socketio = SocketIO(app,async_mode= 'gevent', monkey_patch=True)
print_status = True

@app.route('/')
def home():
    return "Welcome to ASR-TTS-MT"

@socketio.on('new_user')
def handle_new_user(data):
    client_id = data['id']
    if print_status:
        print('\n'+f"New user connected with ID: {client_id}")

def load_config(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

config = load_config('config.yaml')
infer_key = config['ulcakeys']['Authorization']


def ASR_compute_call(language,audio_64):

    url = "https://dhruva-api.bhashini.gov.in/services/inference/pipeline"
    if language == 'bn'or'gu'or'or'or'mr'or'pa'or'sa'or'ur':
        serviceID = config['ASR_config']['nl_ServiceId']

    elif language == 'en':
        serviceID = config['ASR_config']['en_ServiceId']

    elif language == 'hi':
        serviceID = config['ASR_config']['hi_ServiceId']

    elif language == 'kn'or'ml'or'ta'or'te':
        serviceID = config['ASR_config']['sl_ServiceId']

    payload = json.dumps({"pipelineTasks": [{"taskType": "asr","config": {"language": {"sourceLanguage": language},
            "serviceId": serviceID,"audioFormat": "wav","samplingRate": 16000}}],
            "inputData": {"audio": [{"audioContent": audio_64}]}})
    
    headers = {
    'Authorization': infer_key,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.text
    json_obj = json.loads(res)
    out_text = json_obj['pipelineResponse'][0]['output'][0]['source']
    return out_text


def MT_compute_call(source_lan,target_lan,input_text):

    url = "https://dhruva-api.bhashini.gov.in/services/inference/pipeline"

    serviceID = config['MT_config']['mt_ServiceId']

    payload = json.dumps({"pipelineTasks": [{"taskType": "translation","config": {"language":{
            "sourceLanguage": source_lan,
            "targetLanguage": target_lan
            },"serviceId": serviceID}}],"inputData":{"input":[{"source": input_text}],
            "audio": [{"audioContent": None}]}})
    
    headers = {
    'Authorization': infer_key,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.text
    json_obj = json.loads(res)
    out_text = json_obj['pipelineResponse'][0]['output'][0]['target']

    return out_text


def TTS_compute_call(language,input_text):

    url = "https://dhruva-api.bhashini.gov.in/services/inference/pipeline"

    if language == 'bn'or'gu'or'or'or'mr'or'pa'or'hi'or'as':
        serviceID = config['TTS_config']['nl_ServiceId']

    elif language == 'en':
        serviceID = config['TTS_config']['en_ServiceId']

    elif language == 'kn'or'ml'or'ta'or'te':
        serviceID = config['TTS_config']['sl_ServiceId']


    payload = json.dumps({"pipelineTasks": [{"taskType": "tts","config": {"language": {"sourceLanguage": language},
            "serviceId": serviceID,"gender": "female"}}],
            "inputData":{"input": [{"source": input_text}],
            "audio":[{"audioContent": None}]}})
    
    headers = {
    'Authorization': infer_key,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.text
    json_obj = json.loads(res)
    out_audio = json_obj['pipelineResponse'][0]['audio'][0]['audioContent']
    return out_audio



@app.route('/asr', methods=['POST'])

def asr():

    language_map = {
    "english": "en",
    "hindi": "hi",
    "tamil": "ta",
    "telugu" : "te",
    "bengali":"bn",
    "gujarati":"gu",
    "malayalam":"ml",
    "punjabi":"pa",
    "marathi":"mr",
    "odia":"or"
}
    source_lan = request.form['source_language']
    audio = request.files['audio']
    encoded_audio = base64.b64encode(audio.read()).decode('utf-8')
    source_language = language_map.get(source_lan.lower())
    output_text = ASR_compute_call(source_language,encoded_audio)

    return jsonify({'output_text': output_text})


@app.route('/translate', methods=['POST'])
def translate():

    language_map = {
    "english": "en",
    "hindi": "hi",
    "tamil": "ta",
    "telugu" : "te",
    "bengali":"bn",
    "gujarati":"gu",
    "malayalam":"ml",
    "punjabi":"pa",
    "marathi":"mr",
    "odia":"or"
}
    data = request.get_json()
    source_lan = data['source_language']
    target_lan = data['target_language']
    input_text = data['input_text']
    source_language = language_map.get(source_lan.lower())
    target_language = language_map.get(target_lan.lower())

    output_text = MT_compute_call(source_language, target_language, input_text)
    return jsonify({'output_text': output_text})


@app.route('/tts', methods=['POST'])
def tts():

    language_map = {
    "english": "en",
    "hindi": "hi",
    "tamil": "ta",
    "telugu" : "te",
    "bengali":"bn",
    "gujarati":"gu",
    "malayalam":"ml",
    "punjabi":"pa",
    "marathi":"mr",
    "odia":"or"

}

    data = request.get_json()
    target_language = data['target_language']
    input_text = data['input_text']
    output_text = TTS_compute_call(target_language, input_text)

    return jsonify({'output_text': output_text})


if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',port = 0000,debug=True)

