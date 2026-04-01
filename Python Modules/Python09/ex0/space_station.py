from datetime import datetime
from typing import Optional

try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError:
    print("[ERROR] pydantic not installed. Install it with:"
          " pip install pydantic")
    exit()


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("====================================")
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-03-22 14:30:00",
            is_operational=True,
            notes=""
        )
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        status = "Operational" if station.is_operational else "Not operational"
        print(f"Status: {status}")
    except ValidationError as e:
        for error in e.errors():
            print(f"[ERROR] {error['loc'][0]}: {error['msg']}")
    print()
    print("====================================")
    print("Expected validation error:")
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=22,
            power_level=85.5,
            oxygen_level="high",
            last_maintenance="2024-03-22 14:30:00",
            is_operational=False,
            notes=""
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"[ERROR] {error['loc'][0]}: {error['msg']}")


if __name__ == "__main__":
    main()
