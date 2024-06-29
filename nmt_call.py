import requests
import json

def MT_config_call(source_language,target_language):

    url = "https://meity-auth.ulcacontrib.org/ulca/apis/v0/model/getModelsPipeline"

    payload = json.dumps({
    "pipelineTasks": [
        {
        "taskType": "translation",
        "config": {
            "language": {
            "sourceLanguage": source_language,
            "targetLanguage": target_language
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
    # serviceID = json_object['pipelineResponseConfig'][0]['config'][0]['serviceId']
    inference_api_key = json_object['pipelineInferenceAPIEndPoint']['inferenceApiKey']['value']


    return inference_api_key


def MT_compute_call(source_lan,target_lan,input_text):

    url = "https://dhruva-api.bhashini.gov.in/services/inference/pipeline"

    serviceID = "ai4bharat/indictrans-v2-all-gpu--t4"
    inference_key = MT_config_call(source_lan,target_lan)

    payload = json.dumps({
    "pipelineTasks": [
        {
        "taskType": "translation",
        "config": {
            "language": {
            "sourceLanguage": source_lan,
            "targetLanguage": target_lan
            },
            "serviceId": serviceID
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
    'Authorization': inference_key,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = response.text
    json_obj = json.loads(res)
    out_text = json_obj['pipelineResponse'][0]['output'][0]['target']

    return out_text


# sou='hi'
# tar='en'
# inp="मेरा नाम विहिर है और मैं भाषाावर्ष यूज कर रहा हूँ"
# res = MT_compute_call(sou,tar,inp)
# print(res)
