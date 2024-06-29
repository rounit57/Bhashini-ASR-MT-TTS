import requests
import json

def TTS_config_call(target_lan):

    url = "https://meity-auth.ulcacontrib.org/ulca/apis/v0/model/getModelsPipeline"

    payload = json.dumps({
    "pipelineTasks": [
        {
        "taskType": "tts",
        "config": {
            "language": {
            "sourceLanguage": target_lan
            }
        }
        }
    ],
    "pipelineRequestConfig": {
        "pipelineId": "64392f96daac500b55c543cd"
    }
    })
    headers = {
    'userID': <<<Your ulcaapikey>>>,
    'ulcaApikey': <<Your userID>>,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    text = response.text
    json_object = json.loads(text)
    serviceID = json_object['pipelineResponseConfig'][0]['config'][0]['serviceId']
    inference_api_key = json_object['pipelineInferenceAPIEndPoint']['inferenceApiKey']['value']

    return serviceID, inference_api_key

def TTS_compute_call(language,input_text):

    url = "https://dhruva-api.bhashini.gov.in/services/inference/pipeline"

    serviceID,infer_key = TTS_config_call(language)
    payload = json.dumps({
    "pipelineTasks": [
        {
        "taskType": "tts",
        "config": {
            "language": {
            "sourceLanguage": language
            },
            "serviceId": serviceID,
            "gender": "female"
        }
        }
    ],
    "inputData": {
        "input": [
        {
            "source": input_text
        }
        ],
        "audio": [
        {
            "audioContent": None
        }
        ]
    }
    })
    headers = {
    'Authorization': 'vAhBOFg8AT_gDkcevrkxRtwTygQIKIIYaYBhhuBcg9gmJ530FXYI35dNUg3r7miD',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.text
    json_obj = json.loads(res)
    out_audio = json_obj['pipelineResponse'][0]['audio'][0]['audioContent']
    return out_audio



# lan= 'en'
# text = "i am rounit agrawal "
# audio_64  = TTS_compute_call(lan, text)
# print(audio_64)
# import base64
# import os

# def base64_to_audio(audio_64, output_file):
#     # Decode the base64 audio
#     audio_bytes = base64.b64decode(audio_64)

#     # Write the audio bytes to a file
#     with open(output_file, 'wb') as f:
#         f.write(audio_bytes)

#     print(f"Audio saved to {output_file}")

# output_file = "output.wav"
# base64_to_audio(audio_64, output_file)
