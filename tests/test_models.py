from django.test import TestCase
from account.models import CustomUser

# On définit une classe de test qui hérite de TestCase
class CustomUserTestCase(TestCase):

    # Cette méthode est appelée avant chaque test et crée une instance de CustomUser avec des données de test
    def setUp(self):
        self.user = CustomUser.objects.create(
            username='johndoe', email='johndoe@example.com', first_name='John', last_name='Doe', password='test123')

    # On teste la création d'un utilisateur avec les valeurs attendues
    def test_user_creation(self):
        self.assertTrue(isinstance(self.user, CustomUser))  # On vérifie que l'utilisateur créé est bien une instance de CustomUser
        self.assertEqual(self.user.username, 'johndoe')  # On vérifie que le nom d'utilisateur est correct
        self.assertEqual(self.user.email, 'johndoe@example.com')  # On vérifie que l'adresse email est correcte
        self.assertEqual(self.user.first_name, 'John')  # On vérifie que le prénom est correct
        self.assertEqual(self.user.last_name, 'Doe')  # On vérifie que le nom est correct
        self.assertEqual(self.user.password, 'test123')  # On vérifie que le mot de passe est correct
        self.assertFalse(self.user.is_active)  # On vérifie que l'utilisateur n'est pas actif par défaut

    # On teste la méthode __str__ de la classe CustomUser
    def test_user_str_method(self):
        self.assertEqual(str(self.user), 'johndoe')  # On vérifie que la méthode __str__ renvoie bien le nom d'utilisateur

    # On teste les attributs USERNAME_FIELD et REQUIRED_FIELDS de la classe CustomUser
    def test_user_fields(self):
        self.assertEqual(CustomUser.USERNAME_FIELD, 'username')  # On vérifie que l'attribut USERNAME_FIELD est correct
        self.assertEqual(CustomUser.REQUIRED_FIELDS, ['username', 'password', 'first_name', 'last_name'])  # On vérifie que l'attribut REQUIRED_FIELDS est correct
