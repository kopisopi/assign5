import pytest
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import UserProfile

class TestUserPassword:
    def test_valid_password(self):
        
        assert UserProfile.valid_password("Password1!") == True
        assert UserProfile.valid_password("SecurePass2@") == True
        assert UserProfile.valid_password("MyPass3!") == True
        assert UserProfile.valid_password("StrongPwd4$") == True
        assert UserProfile.valid_password("Emma2024%") == True

        assert UserProfile.valid_password("Secure123!") == True
        assert UserProfile.valid_password("Secure123!!") == True
        assert UserProfile.valid_password("S123ecure!") == True
        
        
        # the following below should be true but doesn't apss the test
        assert UserProfile.valid_password("!Password1") == True
        assert UserProfile.valid_password("1Password!") == True
        assert UserProfile.valid_password("1!Password") == True



if __name__ == "__main__":
    pytest.main([__file__, "-v"])