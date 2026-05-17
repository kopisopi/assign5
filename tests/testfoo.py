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

        assert UserProfile.valid_password("SECURE123!") == False
        assert UserProfile.valid_password("secure123!") == False
        assert UserProfile.valid_password("Secureabc!") == False
        assert UserProfile.valid_password("Secure123") == False

        assert UserProfile.valid_password("Ab1!AAAA") == True

        assert UserProfile.valid_password("A1!bcdefg") == True
        assert UserProfile.valid_password("abcdefA1!") == True
        assert UserProfile.valid_password("abcA1!def") == True
        assert UserProfile.valid_password("Aaaaa11!") == True


        assert UserProfile.valid_password(" Secure123!") == False
        assert UserProfile.valid_password("Secure 123") == False
        assert UserProfile.valid_password("Secure12\n!") == False
        assert UserProfile.valid_password("Secure12!\n") == False
        assert UserProfile.valid_password("Secure12\t!") == False

        assert UserProfile.valid_password("Secure12\t!") == False
        


        # the following below should be true but doesn't apss the test
        assert UserProfile.valid_password("!Password1") == True
        assert UserProfile.valid_password("1Password!") == True
        assert UserProfile.valid_password("1!Password") == True
        assert UserProfile.valid_password("123Password!") == True
        assert UserProfile.valid_password("1123!Password") == True
        assert UserProfile.valid_password("!!1Password") == True
        assert UserProfile.valid_password("!!1Password234") == True
        assert UserProfile.valid_password("!!*****1Pd234") == True
        assert UserProfile.valid_password("p111111****jsdfsdfajjasdasodjasdaP") == True

        
        


if __name__ == "__main__":
    pytest.main([__file__, "-v"])