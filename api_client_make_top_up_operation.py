from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.operations.client import build_operations_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client

users_client = build_users_gateway_http_client()
accounts_client = build_accounts_gateway_http_client()
operations_client = build_operations_gateway_http_client()

create_user_response = users_client.create_user()
user_id = create_user_response["user"]["id"]
print(f"Create user response: {create_user_response}")

open_debit_card_account_response = accounts_client.open_debit_card_account(user_id)
account_id = open_debit_card_account_response["account"]["id"]
card_id = open_debit_card_account_response["account"]["cards"][0]["id"]  # Берем первую карту
print(f"Open debit card account response: {open_debit_card_account_response}")

top_up_response = operations_client.make_top_up_operation(card_id, account_id)
print(f"Make top up operation response: {top_up_response}")
