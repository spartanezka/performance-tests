from typing import TypedDict

from httpx import QueryParams, Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


# Базовые TypedDict для общих полей
class BaseOperationRequestDict(TypedDict):
    """Базовая структура данных для операций."""

    status: str
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(BaseOperationRequestDict):
    """Структура данных для создания операции покупки."""

    category: str


class GetOperationsQueryDict(TypedDict):
    """Структура параметров запроса для получения списка операций."""

    accountId: str


class OperationsGatewayHTTPClient(HTTPClient):
    """Клиент для взаимодействия с /api/v1/operations сервиса http-gateway."""

    def get_operation_api(self, operation_id: str) -> Response:
        """Получение информации об операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """Получение чека по операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """Получение списка операций для определенного счета.

        :param query: Словарь с параметрами запроса.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsQueryDict) -> Response:
        """Получение статистики по операциям для определенного счета.

        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: BaseOperationRequestDict) -> Response:
        """Создание операции комиссии.

        :param request: Словарь с данными для создания операции комиссии.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: BaseOperationRequestDict) -> Response:
        """Создание операции пополнения.

        :param request: Словарь с данными для создания операции пополнения.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: BaseOperationRequestDict) -> Response:
        """Создание операции кэшбэка.

        :param request: Словарь с данными для создания операции кэшбэка.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: BaseOperationRequestDict) -> Response:
        """Создание операции перевода.

        :param request: Словарь с данными для создания операции перевода.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """Создание операции покупки.

        :param request: Словарь с данными для создания операции покупки.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: BaseOperationRequestDict) -> Response:
        """Создание операции оплаты по счету.

        :param request: Словарь с данными для создания операции оплаты по счету.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: BaseOperationRequestDict) -> Response:
        """Создание операции снятия наличных денег.

        :param request: Словарь с данными для создания операции снятия наличных.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
