from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.documents.client import build_documents_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client

users_client = build_users_gateway_http_client()
accounts_client = build_accounts_gateway_http_client()
documents_client = build_documents_gateway_http_client()

create_user_response = users_client.create_user()
user_id = create_user_response["user"]["id"]
print(f"Create user response: {create_user_response}")

account_response = accounts_client.open_credit_card_account(user_id)
account_id = account_response["account"]["id"]
print(f"Open credit card account response: {account_response}")

tariff_response = documents_client.get_tariff_document(account_id)
print(f"Get tariff document response: {tariff_response}")

contract_response = documents_client.get_contract_document(account_id)
print(f"Get contract document response: {contract_response}")
