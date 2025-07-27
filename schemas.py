# In schemas.py

from pydantic import BaseModel
from typing import Dict, Any

# This describes the nested "fields" object in the request.
class WheelSpecFields(BaseModel):
    treadDiameterNew: str
    lastShopIssueSize: str
    condemningDia: str
    wheelGauge: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelProfile: str
    intermediateWWP: str
    bearingSeatDiameter: str
    rollerBearingOuterDia: str
    rollerBearingBoreDia: str
    rollerBearingWidth: str
    axleBoxHousingBoreDia: str
    wheelDiscWidth: str

# This describes the entire POST request body.
class WheelSpecCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: WheelSpecFields

# This describes the "data" object in the successful response.
class WheelSpecResponseData(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    status: str

# This describes the top-level API response.
class WheelSpecResponse(BaseModel):
    success: bool
    message: str
    data: WheelSpecResponseData