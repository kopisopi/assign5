import pytest
import json
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import UserProfile


class TestUserAge:
    # comment
    def test_age_calculation(self):
        assert UserProfile.valid_password("1!Password") == True
        # ^^placeholder

# def get_age(self, reference_date: datetime | None = None) -> int:

if __name__ == "__main__":
    pytest.main([__file__, "-v"])