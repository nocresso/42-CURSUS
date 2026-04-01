from datetime import datetime
from typing import Optional
from enum import Enum

try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ImportError:
    print("[ERROR] pydantic not installed. Install it with:"
          " pip install pydantic")
    exit()


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def check_fields(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start"
                             " with \"AC\" (Alien Contact)")
        if (self.contact_type == ContactType.physical
                and self.is_verified is False):
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError("Telepathic contact requires"
                             " at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should"
                             " include received messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("====================================")
    try:
        alien_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 3, 22, 14, 30, 0),
            location="Area 51, Nevada",
            contact_type="radio",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="'Greetings from Zeta Reticuli'",
            is_verified=True
        )
        print("Valid contact report:")
        print(f"ID: {alien_contact.contact_id}")
        print(f"Type: {alien_contact.contact_type.value}")
        print(f"Location: {alien_contact.location}")
        print(f"Signal: {alien_contact.signal_strength}/10.0")
        print(f"Duration: {alien_contact.duration_minutes} minutes")
        print(f"Witnesses: {alien_contact.witness_count}")
        print(f"Message: {alien_contact.message_received}")
    except ValidationError as e:
        for error in e.errors():
            print(f"[ERROR] {error['msg']}")
    print()
    print("====================================")
    print("Expected validation error:")
    try:
        alien_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 3, 22, 14, 30, 0),
            location="Area 51, Nevada",
            contact_type="telepathic",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="'Greetings from Zeta Reticuli'",
            is_verified=True
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"[ERROR] {error['msg']}")


if __name__ == "__main__":
    main()
