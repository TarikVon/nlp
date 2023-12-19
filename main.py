import gradio as gr
import re
from keras.models import load_model
from keras.utils import pad_sequences
import pickle
from nltk.corpus import stopwords


def load_and_predict(user_input, model_path="./NLP.h5"):
    # Load the entire model
    model = load_model(model_path)
    with open("./tokenizer.pkl", "rb") as file:
        tokenizer = pickle.load(file)
    stop = stopwords.words("english")

    # Perform the same text preprocessing steps as during training
    cleaned_input = user_input.lower()
    cleaned_input = re.sub("[^A-Za-z0-9\s]", "", cleaned_input)
    cleaned_input = re.sub("\n", "", cleaned_input)
    cleaned_input = re.sub("\s+", " ", cleaned_input)
    cleaned_input = " ".join([word for word in cleaned_input.split() if word not in stop])

    # Use the tokenizer created earlier for text markup
    input_sequence = tokenizer.texts_to_sequences([cleaned_input])
    padded_input = pad_sequences(input_sequence, maxlen=500, padding="post", truncating="post")

    # Make model prediction
    prediction = model.predict(padded_input)

    # Print prediction results
    if prediction > 0.5:
        return "REAL NEWS.\n"
    else:
        return "FAKE NEWS!!!\n"


demo = gr.Interface(fn=load_and_predict, inputs="text", outputs="text")
demo.launch(server_name="0.0.0.0", server_port=7860)
