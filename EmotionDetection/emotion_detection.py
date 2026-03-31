# emotion_detection.py

import requests  # Used to call Watson NLP API

def emotion_detector(text_to_analyze):
    """
    Sends input text to Watson NLP API and returns emotion scores.
    """
    if text_to_analyze.strip() == "":
        return None


    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }


    input_json = {
        "raw_document": {"text": text_to_analyze}
    }

    # API call
    response = requests.post(url, json=input_json, headers=headers)

    # Successful response
    if response.status_code == 200:
        return response.json()["emotionPredictions"][0]["emotion"]

    # Error case
    return None
