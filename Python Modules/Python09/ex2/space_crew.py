from datetime import datetime
from typing import List
from enum import Enum

try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ImportError:
    print("[ERROR] pydantic not installed. Install it with:"
          " pip install pydantic")
    exit()


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_fields(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with \"M\"")
        experienced = 0
        active = True
        commander = False
        for member in self.crew:
            if member.years_experience >= 5:
                experienced += 1
            if member.is_active is False:
                active = False
            if member.rank == Rank.commander or member.rank == Rank.captain:
                commander = True
        if commander is False:
            raise ValueError("Mission must have at least one"
                             " Commander or Captain")
        if self.duration_days > 365:
            if experienced < (len(self.crew) / 2):
                raise ValueError("Long missions (> 365 days) need 50%"
                                 " experienced crew (5+ years)")
        if active is False:
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("====================================")
    try:
        crew_list = [
            CrewMember(
                member_id="M100",
                name="Sarah Connor",
                rank=Rank.commander,
                age=30,
                specialization="Mission Command",
                years_experience=10,
                is_active=True
            ),
            CrewMember(
                member_id="M101",
                name="John Smith",
                rank=Rank.lieutenant,
                age=30,
                specialization="Navigation",
                years_experience=10,
                is_active=True
            ),
            CrewMember(
                member_id="M102",
                name="Alice Johnson",
                rank=Rank.officer,
                age=30,
                specialization="Engineering",
                years_experience=10,
                is_active=True
            )
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 3, 22, 14, 30, 0),
            duration_days=900,
            crew=crew_list,
            mission_status="planned",
            budget_millions=2500.0
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(crew_list)}")
        print("Crew members:")
        for member in crew_list:
            print(f"- {member.name} ({member.rank.value})"
                  f" - {member.specialization}")
    except ValidationError as e:
        for error in e.errors():
            print(f"[ERROR] {error['msg']}")
    print()
    print("====================================")
    print("Expected validation error:")
    try:
        crew_list = [
            CrewMember(
                member_id="M100",
                name="Sarah Connor",
                rank=Rank.cadet,
                age=30,
                specialization="Mission Command",
                years_experience=10,
                is_active=True
            ),
            CrewMember(
                member_id="M101",
                name="John Smith",
                rank=Rank.lieutenant,
                age=30,
                specialization="Navigation",
                years_experience=10,
                is_active=True
            ),
            CrewMember(
                member_id="M102",
                name="Alice Johnson",
                rank=Rank.officer,
                age=30,
                specialization="Engineering",
                years_experience=10,
                is_active=True
            )
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 3, 22, 14, 30, 0),
            duration_days=900,
            crew=crew_list,
            mission_status="planned",
            budget_millions=2500.0
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"[ERROR] {error['msg']}")


if __name__ == "__main__":
    main()
