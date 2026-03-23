from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

from tools.fakers import fake


class OperationType(StrEnum):
    """Тип операции."""

    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    """Статус операции."""

    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """Описание структуры операции."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """Описание структуры чека операции."""

    model_config = ConfigDict(populate_by_name=True)

    url: str
    document: str


class OperationsSummarySchema(BaseModel):
    """Описание структуры сводки по операциям."""

    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class BaseOperationRequestSchema(BaseModel):
    """Базовая структура данных для операций."""

    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(BaseOperationRequestSchema):
    """Структура данных для создания операции комиссии."""


class MakeTopUpOperationRequestSchema(BaseOperationRequestSchema):
    """Структура данных для создания операции пополнения."""


class MakeCashbackOperationRequestSchema(BaseOperationRequestSchema):
    """Структура данных для создания операции кэшбэка."""


class MakeTransferOperationRequestSchema(BaseOperationRequestSchema):
    """Структура данных для создания операции перевода."""


class MakeBillPaymentOperationRequestSchema(BaseOperationRequestSchema):
    """Структура данных для создания операции оплаты по счету."""


class MakeCashWithdrawalOperationRequestSchema(BaseOperationRequestSchema):
    """Структура данных для создания операции снятия наличных денег."""


class MakePurchaseOperationRequestSchema(BaseOperationRequestSchema):
    """Структура данных для создания операции покупки."""

    model_config = ConfigDict(populate_by_name=True)

    category: str = Field(default_factory=fake.category)


class GetOperationsQuerySchema(BaseModel):
    """Структура параметров запроса для получения списка операций."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    """Структура параметров запроса для получения статистики по операциям для определенного счета."""

    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationResponseSchema(BaseModel):
    """Описание структуры ответа получения операции."""

    model_config = ConfigDict(populate_by_name=True)

    operation: OperationSchema


class GetOperationReceiptResponseSchema(BaseModel):
    """Описание структуры ответа получения чека операции."""

    model_config = ConfigDict(populate_by_name=True)

    receipt: OperationReceiptSchema


class GetOperationsResponseSchema(BaseModel):
    """Описание структуры ответа получения списка операций."""

    model_config = ConfigDict(populate_by_name=True)

    operations: list[OperationSchema]


class GetOperationsSummaryResponseSchema(BaseModel):
    """Описание структуры ответа получения сводки по операциям."""

    model_config = ConfigDict(populate_by_name=True)

    summary: OperationsSummarySchema


class MakeFeeOperationResponseSchema(BaseModel):
    """Описание структуры ответа создания операции комиссии."""

    model_config = ConfigDict(populate_by_name=True)

    operation: OperationSchema


class MakeTopUpOperationResponseSchema(BaseModel):
    """Описание структуры ответа создания операции пополнения."""

    model_config = ConfigDict(populate_by_name=True)

    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    """Описание структуры ответа создания операции кэшбэка."""

    model_config = ConfigDict(populate_by_name=True)

    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    """Описание структуры ответа создания операции перевода."""

    model_config = ConfigDict(populate_by_name=True)

    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    """Описание структуры ответа создания операции покупки."""

    model_config = ConfigDict(populate_by_name=True)

    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """Описание структуры ответа создания операции оплаты по счету."""

    model_config = ConfigDict(populate_by_name=True)

    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """Описание структуры ответа создания операции снятия наличных."""

    model_config = ConfigDict(populate_by_name=True)

    operation: OperationSchema
