from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


""" 
"la fonction qui nous permetra de genere un token
"""

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, User, timestamp: int): 
        return (
            text_type(User.pk)+text_type(timestamp)
        )
        
generatorToken= TokenGenerator()