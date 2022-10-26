from pydantic import BaseModel
# Create ToDoRequest Base Model
class ContactRequest(BaseModel):
    name: str
    email: str
    message: str

class DemoRequest(BaseModel):
    name: str
    company_name: str
    email: str
    position: str
    phone_no: int
    services: str


class SubscriptionRequest(BaseModel):
    email: str
  