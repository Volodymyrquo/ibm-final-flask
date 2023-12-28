import unittest

from EmotionDetection.emotion_detection import emotion_detector

statements = {
'I am glad this happened':'joy',
'I am really mad about this':'anger',
'I feel disgusted just hearing about this':'disgust',
'I am so sad about this':'sadness',
'I am really afraid that this will happen':'fear'
}


class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        for key in statements:
            self.assertEqual(emotion_detector(key)["dominant_emotion"],statements[key])

if __name__ == "__main__":
    unittest.main()