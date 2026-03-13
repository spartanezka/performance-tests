from typing import TypedDict

from httpx import QueryParams, Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """Описание структуры операции."""

    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    """Описание структуры чека операции."""

    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    """Описание структуры сводки по операциям."""

    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class BaseOperationRequestDict(TypedDict):
    """Базовая структура данных для операций."""

    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(BaseOperationRequestDict):
    """Структура данных для создания операции комиссии."""


class MakeTopUpOperationRequestDict(BaseOperationRequestDict):
    """Структура данных для создания операции пополнения."""


class MakeCashbackOperationRequestDict(BaseOperationRequestDict):
    """Структура данных для создания операции кэшбэка."""


class MakeTransferOperationRequestDict(BaseOperationRequestDict):
    """Структура данных для создания операции перевода."""


class MakeBillPaymentOperationRequestDict(BaseOperationRequestDict):
    """Структура данных для создания операции оплаты по счету."""


class MakeCashWithdrawalOperationRequestDict(BaseOperationRequestDict):
    """Структура данных для создания операции снятия наличных денег."""


class MakePurchaseOperationRequestDict(BaseOperationRequestDict):
    """Структура данных для создания операции покупки."""

    category: str


class GetOperationsQueryDict(TypedDict):
    """Структура параметров запроса для получения списка операций."""

    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """Структура параметров запроса для получения статистики по операциям для определенного счета"""

    accountId: str


class GetOperationResponseDict(TypedDict):
    """Описание структуры ответа получения операции."""

    operation: OperationDict


class GetOperationReceiptResponseDict(TypedDict):
    """Описание структуры ответа получения чека операции."""

    receipt: OperationReceiptDict


class GetOperationsResponseDict(TypedDict):
    """Описание структуры ответа получения списка операций."""

    operations: list[OperationDict]


class GetOperationsSummaryResponseDict(TypedDict):
    """Описание структуры ответа получения сводки по операциям."""

    summary: OperationsSummaryDict


class MakeFeeOperationResponseDict(TypedDict):
    """Описание структуры ответа создания операции комиссии."""

    operation: OperationDict


class MakeTopUpOperationResponseDict(TypedDict):
    """Описание структуры ответа создания операции пополнения."""

    operation: OperationDict


class MakeCashbackOperationResponseDict(TypedDict):
    """Описание структуры ответа создания операции кэшбэка."""

    operation: OperationDict


class MakeTransferOperationResponseDict(TypedDict):
    """Описание структуры ответа создания операции перевода."""

    operation: OperationDict


class MakePurchaseOperationResponseDict(TypedDict):
    """Описание структуры ответа создания операции покупки."""

    operation: OperationDict


class MakeBillPaymentOperationResponseDict(TypedDict):
    """Описание структуры ответа создания операции оплаты по счету."""

    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """Описание структуры ответа создания операции снятия наличных."""

    operation: OperationDict


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

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """Получение статистики по операциям для определенного счета.

        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """Создание операции комиссии.

        :param request: Словарь с данными для создания операции комиссии.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """Создание операции пополнения.

        :param request: Словарь с данными для создания операции пополнения.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """Создание операции кэшбэка.

        :param request: Словарь с данными для создания операции кэшбэка.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
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

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """Создание операции оплаты по счету.

        :param request: Словарь с данными для создания операции оплаты по счету.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """Создание операции снятия наличных денег.

        :param request: Словарь с данными для создания операции снятия наличных.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=1500.11,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=100.50,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=200.00,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=50.25,
            cardId=card_id,
            accountId=account_id,
            category="food",
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=1000.00,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=500.00,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
