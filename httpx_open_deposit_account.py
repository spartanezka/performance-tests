import json
import time
from typing import Any

import httpx

SUCCESS_STATUS_CODE = 200
HTTP_GATEWAY = "http://localhost:8003"

def create_user() -> dict[str, Any] | None:
    """Создание нового пользователя."""
    user_payload = {
        "email": f"user.{time.time()}@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string",
        "phoneNumber": "string",
    }
    response = httpx.post(f"{HTTP_GATEWAY}/api/v1/users", json=user_payload)

    if response.status_code != SUCCESS_STATUS_CODE:
        print(f"Ошибка при создании пользователя: {response.text}")
        return None

    return response.json()

def open_deposit_account(user_id: str) -> dict[str, Any] | None:
    """Открытие депозитного счёта для пользователя."""
    payload = {
        "userId": user_id,
    }
    response = httpx.post(f"{HTTP_GATEWAY}/api/v1/accounts/open-deposit-account", json=payload)

    print(response.status_code)

    if response.status_code != SUCCESS_STATUS_CODE:
        print(f"Ошибка при открытии депозитного счёта: статус {response.text}")
        return None

    return response.json()

def main() -> None:
    user_responce_data = create_user()

    if user_responce_data is None:
        return

    account = open_deposit_account(user_responce_data["user"].get("id"))

    if account is None:
        return

    print(json.dumps(account, indent=2))

if __name__ == "__main__":
    main()
