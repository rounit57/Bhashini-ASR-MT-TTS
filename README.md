# Bhashini-ASR-MT-TTS
Pipeline to call and use ASR, MT, and TTS from BHASHINI 

Login/signUp to https://bhashini.gov.in/ulca/user/login there if go in profile you can see your UserID and you can also generate the ULCA API Key.

Here https://bhashini.gitbook.io/bhashini-apis You can get the complete Documentation to use ASR,TTS and MT.

Here You just have to get your userId and ulcaApiKey and paste it in functions provided , and call ASR_compute_call , nmt_compute_call and tts_compute_call to use it.



Pipeline for ASR, MT, and TTS Using BHASHINI

This repository provides a streamlined pipeline to call and use ASR (Automatic Speech Recognition), MT (Machine Translation), and TTS (Text-to-Speech) services from BHASHINI.

Prerequisites

BHASHINI Account:

Sign up or log in at BHASHINI.

Navigate to your profile to retrieve your UserID and generate the ULCA API Key.

Documentation Reference:

Access the complete API documentation here.

Features

This repository simplifies the usage of BHASHINI’s APIs by:

Providing functions to seamlessly integrate ASR, MT, and TTS.

Enabling direct calls to the APIs with minimal setup.

Getting Started

Setup

Clone this repository:

git clone https://github.com/your-repo-name.git
cd your-repo-name

Install dependencies:

pip install -r requirements.txt

Add your UserID and ULCA API Key:

Open the provided configuration file or script.

Paste your credentials into the designated fields.

Example:

USER_ID = "your-user-id"
ULCA_API_KEY = "your-ulca-api-key"

Usage

ASR (Automatic Speech Recognition)

Convert speech into text by calling:

from your_script_name import asr_compute_call
response = asr_compute_call(audio_file_path)
print(response)

MT (Machine Translation)

Translate text from one language to another using:

from your_script_name import nmt_compute_call
response = nmt_compute_call(text, source_language, target_language)
print(response)

TTS (Text-to-Speech)

Generate speech from text with:

from your_script_name import tts_compute_call
response = tts_compute_call(text, language)
print(response)

Additional Resources

For detailed API parameters and customization, refer to the BHASHINI API Documentation.

For troubleshooting, check out the docs folder or open an issue in this repository.

Contributing

Contributions are welcome! If you have suggestions or find issues, feel free to:

Submit a pull request.

Open an issue.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments

Thanks to the BHASHINI initiative for providing robust language processing APIs.
