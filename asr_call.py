import requests
import json

def ASR_config_call(language):

    url = "https://meity-auth.ulcacontrib.org/ulca/apis/v0/model/getModelsPipeline"

    payload = json.dumps({
    "pipelineTasks": [
        {
        "taskType": "asr",
        "config": {
            "language": {
            "sourceLanguage": language
            }
        }
        }
    ],
    "pipelineRequestConfig": {
        "pipelineId": "64392f96daac500b55c543cd"
    }
    })
    headers = {
    'ulcaApikey': <<<Your ulcaapikey>>>,
    'userID': <<Your userID>>,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    text = response.text
    json_object = json.loads(text)
    serviceID = json_object['pipelineResponseConfig'][0]['config'][0]['serviceId']
    inference_api_key = json_object['pipelineInferenceAPIEndPoint']['inferenceApiKey']['value']

    return serviceID,inference_api_key


def ASR_compute_call(language,audio_64):

    url = "https://dhruva-api.bhashini.gov.in/services/inference/pipeline"
    serviceID , infer_key = ASR_config_call(language)

    payload = json.dumps({
    "pipelineTasks": [
        {
        "taskType": "asr",
        "config": {
            "language": {
            "sourceLanguage": language
            },
            "serviceId": serviceID,
            "audioFormat": "wav",
            "samplingRate": 16000
        }
        }
    ],
    "inputData": {
        "audio": [
        {
            "audioContent": audio_64
        }
        ]
    }
    })
    headers = {
    'Authorization': infer_key,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.text
    json_obj = json.loads(res)
    out_text = json_obj['pipelineResponse'][0]['output'][0]['source']
    return out_text


# lan= 'en'
# import base64

# with open('output.wav', 'rb') as f:
#     audio_bytes = f.read()

# base64_audio = base64.b64encode(audio_bytes).decode('utf-8')
# out = ASR_compute_call(lan,base64_audio)
# print(out)
