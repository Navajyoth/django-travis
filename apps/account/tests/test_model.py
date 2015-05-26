from django.test import TestCase
from model_mommy import mommy

from apps.account.models import User,UserLog,EmailAddress,PasswordReset,EmailConfirm


class AccountTestModel(TestCase):
    def setUp(self):
        self.travis = mommy.make(User)
        self.person = mommy.make(UserLog)
        self.email = mommy.make(EmailAddress)
        self.password = mommy.make(PasswordReset)
        self.confirm = mommy.make(EmailConfirm)

    def test_account_00(self):
        print 'hello'
        self.assertTrue(isinstance(self.travis, User))

    def test_account_01(self):    
        self.assertTrue(isinstance(self.person, UserLog))

    def test_account_02(self):    
        self.assertTrue(isinstance(self.email, EmailAddress))

    def test_account_03(self):    
        self.assertTrue(isinstance(self.password, PasswordReset))

    def test_account_04(self):    
        self.assertTrue(isinstance(self.confirm, EmailConfirm))