import time
from typing import Dict

import jwt
from app.core.config import config


JWT_SECRET = config.secret
JWT_ALGORITHM = config.algorithm


def token_response(token: str):
    return {
        "access_token": token
    }


def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}


def refresh_jwt(token: str, user_id: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return token_response(token) if decoded_token["expires"] >= time.time() else sign_jwt(user_id)
    except:
        return {}


if __name__ == "__main__":
    user_id = 1
    payload = {
        "user_id": user_id,
        "expires": time.time() + 9999999999999999
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    print(token)