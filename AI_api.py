import json
import requests

model = "mistral"


def generate(user_input, context):
    r = requests.post("http://127.0.0.1:11434/api/generate",
                      json={
                          "prompt": user_input,
                          "context": context,
                          "model": model
                      },
                      stream=True)
    r.raise_for_status()

    for chunk in r.iter_content(chunk_size=None):
        body = json.loads(chunk)
        response_part = body.get("response", '')
        print(response_part, end='', flush=True)

        if "error" in body:
            raise Exception(body["error"])

        if body.get("done", False):
            return body["context"]


def main():
    context = []

    while True:
        user_input = input("Ecris qql chose : ")
        if user_input == "/bye":
            print("bye")
            break
        print()
        context = generate(user_input, context)
        print()


if __name__ == '__main__':
    main()
