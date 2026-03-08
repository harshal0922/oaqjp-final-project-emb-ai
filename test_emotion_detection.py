from EmotionDetection import emotion_detector

def test_emotion_detector():

    sentences = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for sentence, expected_emotion in sentences.items():
        result = emotion_detector(sentence)

        if result["dominant_emotion"] == expected_emotion:
            print(f"PASS: {sentence}")
        else:
            print(f"FAIL: {sentence}")

test_emotion_detector()