from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np
from rest_framework import permissions

model_path = "./ml_model/distlBert-model-v8"

model_labels = ['Algorithm Design',
                'Basic Machine Organisation',
                'Computer System',
                'Data Manipulation and Analysis',
                'Data Organisation and Data Control',
                'Elementary Web Authoring',
                'Health and Ethical Issues',
                'Information Processing',
                'Intellectual Property',
                'Internet Services and Applications',
                'Multimedia Elements',
                'Networking and Internet Basics',
                'Program Development',
                'Spreadsheets and Databases',
                'Threats and Security on the Internet']
id2label = {idx: label for idx, label in enumerate(model_labels)}
label2id = {label: idx for idx, label in enumerate(model_labels)}


class ModelAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self):
        pass

    def post(self, request):
        # load the model
        model = AutoModelForSequenceClassification.from_pretrained(
            model_path, local_files_only=True)
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        # model.to('cuda')
        # data = request.data
        # text = data["text"]
        # print(text)

        try:
            data = request.data
            text = data["text"]
            print('\nposted data: ' + text)
            if text != None:
                # tokenize the text for loading into model
                encoding = encodeText(tokenizer, model, text)
                output = model(**encoding)
                logits = output.logits
                result = showPredictions(logits)
                predictions = {
                    'error': '0',
                    'message': 'Successfull',
                    'prediction': result,
                }
            else:
                predictions = {
                    'error': '1',
                    'message': 'Invalid Parameters'
                }
        except Exception as e:
            predictions = {
                'error': '2',
                "message": str(e)
            }

        return Response(predictions)


def encodeText(tokenizer, model, data):
    encoding = tokenizer(data, return_tensors="pt")
    encoding = {k: v.to(model.device) for k, v in encoding.items()}
    return encoding


def showPredictions(logits):
    sigmoid = torch.nn.Sigmoid()
    probs = sigmoid(logits.squeeze().cpu())
    predictions = np.zeros(probs.shape)
    predictions[np.where(probs >= 0.5)] = 1
    # turn predicted id's into actual label names
    predicted_labels = [id2label[idx]
                        for idx, label in enumerate(predictions) if label == 1.0]
    return predicted_labels
