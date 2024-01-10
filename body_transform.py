import string

def transform_body(body):
    return body.lower().lstrip().rstrip().strip(string.punctuation.strip())

