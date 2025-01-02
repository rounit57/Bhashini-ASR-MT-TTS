
# Pipeline for ASR, MT, and TTS Using BHASHINI

This repository provides a streamlined pipeline to call and use **ASR (Automatic Speech Recognition)**, **MT (Machine Translation)**, and **TTS (Text-to-Speech)** services from **BHASHINI**.

---

## Prerequisites

1. **BHASHINI Account**: 
   - Sign up or log in at [BHASHINI](https://bhashini.gov.in/ulca/user/login).
   - Navigate to your profile to retrieve your **UserID** and generate the **ULCA API Key**.

2. **Documentation Reference**: 
   - Access the complete API documentation [here](https://bhashini.gitbook.io/bhashini-apis).

---

## Features

This repository simplifies the usage of BHASHINI’s APIs by:
- Providing functions to seamlessly integrate ASR, MT, and TTS.
- Enabling direct calls to the APIs with minimal setup.

---

## Getting Started

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Add your **UserID** and **ULCA API Key**:
   - Open the provided configuration file or script.
   - Paste your credentials into the designated fields.

   Example:
   ```python
   USER_ID = "your-user-id"
   ULCA_API_KEY = "your-ulca-api-key"

---

### Usage

#### ASR (Automatic Speech Recognition)
Convert speech into text by calling:
```python
from your_script_name import asr_compute_call
response = asr_compute_call(audio_file_path)
print(response)
```
#### MT (Machine Translation)
Translate text from one language to another using:
```python
from your_script_name import nmt_compute_call
response = nmt_compute_call(text, source_language, target_language)
print(response)## Contributing

Contributions are welcome! If you have suggestions or find issues, feel free to:
- Submit a pull request.
- Open an issue.
```
#### TTS (Text-to-Speech)
Generate speech from text with:
```python
from your_script_name import tts_compute_call
response = tts_compute_call(text, language)
print(response)
```

## Contributing

Contributions are welcome! If you have suggestions or find issues, feel free to:
- Submit a pull request.
- Open an issue.

## Acknowledgments
Thanks to the BHASHINI initiative for providing robust language processing APIs.

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.


