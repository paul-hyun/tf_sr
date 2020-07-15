# LibriSpeech

## libri_speech_flac_to_wav.py
- LibriSpeech의 flac 파일을 wav로 변경. 나머지 파일은 복사
- 출력
  - wav로 변환된 파일과 나머지 내용이 복사된 폴더

## libri_speech_make_json.py
- LibriSpeech의 wav파일 및 label을 분석하여 json 형태로 저장
- 출력
  - {"key": [wave path], "duration": [wave length], "label": [wave text]} 형태로 저장된 파일