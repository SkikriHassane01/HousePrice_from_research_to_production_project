from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from regression_model.config.core import config


def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for na values and filter."""
    validated_data = input_data.copy()
    new_vars_with_na = [
        var
        for var in config.model_config.features
        if var
        not in config.model_config.categorical_vars_with_na_frequent
        + config.model_config.numerical_vars_with_na
        and validated_data[var].isnull().sum() > 0
    ]
    validated_data.dropna(subset=new_vars_with_na, inplace=True)

    return validated_data


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    # convert syntax error field names (beginning with numbers)
    input_data.rename(columns=config.model_config.variables_to_rename, inplace=True)
    input_data["MSSubClass"] = input_data["MSSubClass"].astype("O")
    relevant_data = input_data[config.model_config.features].copy()
    validated_data = drop_na_inputs(input_data=relevant_data)
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        MultipleHouseDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class HouseDataInputSchema(BaseModel):
    MSSubClass: Optional[int]
    MSZoning: Optional[str]
    LotArea: Optional[int]
    LotShape: Optional[str]
    LandContour: Optional[str]
    LotConfig: Optional[str]
    Neighborhood: Optional[str]
    Condition1: Optional[str]
    HouseStyle: Optional[str]
    OverallQual: Optional[int]
    YearRemodAdd: Optional[int]
    RoofStyle: Optional[str]
    Exterior1st: Optional[str]
    ExterQual: Optional[str]
    Foundation: Optional[str]
    BsmtQual: Optional[str]
    BsmtCond: Optional[str]
    BsmtExposure: Optional[str]
    BsmtFinType1: Optional[str]
    BsmtFinSF1: Optional[float]
    BsmtUnfSF: Optional[float]
    HeatingQC: Optional[str]
    CentralAir: Optional[str]
    FirstFlrSF: Optional[int]  # Renamed from '1stFlrSF'
    GrLivArea: Optional[int]
    BsmtFullBath: Optional[int]
    HalfBath: Optional[int]
    KitchenQual: Optional[str]
    TotRmsAbvGrd: Optional[int]
    Functional: Optional[str]
    Fireplaces: Optional[int]
    GarageYrBlt: Optional[int]
    GarageFinish: Optional[str]
    GarageCars: Optional[int]
    GarageArea: Optional[float]
    PavedDrive: Optional[str]
    WoodDeckSF: Optional[int]
    OpenPorchSF: Optional[int]
    ScreenPorch: Optional[int]
    SaleCondition: Optional[str]
    YrSold: Optional[int]


class MultipleHouseDataInputs(BaseModel):
    inputs: List[HouseDataInputSchema]
