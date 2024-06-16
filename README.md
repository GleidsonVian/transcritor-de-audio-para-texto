# Audio Recording and Speech Recognition

Este projeto grava áudio do microfone e transcreve o áudio gravado para texto usando a biblioteca `SpeechRecognition` do Python.

## Requisitos

Antes de executar o projeto, certifique-se de ter instalado os seguintes requisitos:

- Python 3.x
- Bibliotecas Python listadas em `requirements.txt`

## Instalação

1. Clone este repositório para o seu ambiente local:

    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```sh
    python -m venv venv
    source venv/bin/activate   # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências listadas no arquivo `requirements.txt`:

    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Execute o script `transcritor.py` para gravar áudio e transcrever para texto:

    ```sh
    python transcritor.py
    ```

2. O script gravará 10 segundos de áudio do microfone e salvará o áudio em um arquivo `output.wav`.

3. Após a gravação, o script tentará transcrever o áudio para texto em português (pt-BR) usando o serviço de reconhecimento de fala da Google.

