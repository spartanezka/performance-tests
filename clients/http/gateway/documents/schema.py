from pydantic import BaseModel, ConfigDict, HttpUrl


class DocumentSchema(BaseModel):
    """Описание структуры документа."""

    url: HttpUrl
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """Описание структуры ответа получения тарифного документа."""

    model_config = ConfigDict(populate_by_name=True)

    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """Описание структуры ответа получения контрактного документа."""

    model_config = ConfigDict(populate_by_name=True)

    contract: DocumentSchema
