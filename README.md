# Fake News Detection Analysis (LSTM Classification) | NLP | Python

If you want to download and run our model, it may take up `1.66 GB` of your local storage space.

Please take the following steps:

## 1. Clone our repository

Clone our repository locally by running the following command in the terminal:

```bash
cd /path/to/your/folder/ # Please specify a folder for storing the repository
git clone https://github.com/TarikVon/nlp.git
```

## 2. Install the dependencies

Click on the following link to download our environment dependencies:

[env.tar.gz](https://drive.google.com/file/d/1-6J56CobKInlKEjF0Qf5Gl95RYcO42IT/view?usp=drive_link)

Put the downloaded file `env.tar.gz` into the cloned folder above, then run the following command in the terminal:

```bash
tar -xzvf env.tar.gz
```

## 3. Activate the environment and run the program

```bash
.\env\Scripts\activate
python .\main.py
```

If prompted with "`Running on local URL: http://0.0.0.0:7860`", it indicates that the program ran successfully on local port `7860`. Please open the following website in your browser:

```
http://localhost:7860/
```

Enter the news text in the input box of "user_input" on the left (you can use the news test text we provide: `./news.txt`), click the Submit button below, and wait for a few seconds to see the running result on the right:

<img src="https://www.tarikvon.cn/images/deployments/20231219091049.png" width="50%">

## 4. Exit program

Press the `Ctrl+C` combination button on the terminal interface, and if prompted with "`Keyboard interruption in main thread... closing server.`", The program has successfully exited, you can close the terminal.

Wishing you a pleasant experience!
