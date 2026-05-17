import pytest
import json
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import UserProfile
from src import UserProfileManager

class TestUserAge:
    # comment
    # def test_age_calculation(self):
    #     assert UserProfile.valid_password("1!Password") == True
        # ^^placeholder

  
    def test_age_calculation(self):
        user = UserProfile(
            name="Alice Marie Johnson",
            email="alice.johnson@email.com",
            password="Password1!",
            dob="05/16/2000",
            location={
                "city": "Seattle",
                "state": "WA",
                "country": "US"
            }
        )
        today = datetime(2026, 5, 16)
        
        calculated_age = user.get_age(reference_date=today)
        

        assert calculated_age == 26

# def get_age(self, reference_date: datetime | None = None) -> int:

if __name__ == "__main__":
    pytest.main([__file__, "-v"])