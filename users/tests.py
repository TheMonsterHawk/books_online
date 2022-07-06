from xml.dom import ValidationErr
from django.test import TestCase
from django.contrib.auth import get_user_model 

from django.core.exceptions import ValidationError 

from datetime import datetime 
from dateutil.relativedelta import relativedelta 

class UserTest(TestCase): 
    def test_create_user(self): 
        User = get_user_model() 
        user = User.objects.create_user(username='test', email='test@test.com') 
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@test.com') 
        self.assertFalse(user.is_superuser) 
        self.assertTrue(user.is_active) 
        self.assertFalse(user.is_staff)  
    
    def test_create_superuser(self): 
        User = get_user_model() 
        user = User.objects.create_superuser(username='test', email='test@test.com') 
        self.assertEqual(user.username, 'test') 
        self.assertEqual(user.email, 'test@test.com') 
        self.assertTrue(user.is_active) 
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff) 
    
    def test_birth_date_not_in_future_validation_error(self): 
        User = get_user_model() 
        d = datetime.now() + relativedelta(years=1) 
        with self.assertRaises(ValidationError) as cm: 
            user = User.objects.create_superuser(username='test', email='test@test.com', birth_date=d) 
        error = cm.exception 
        self.assertEqual(error.message, 'Birth date can not be in future!') 

    def test_gender_value_not_valid_error(self): 
        User = get_user_model() 
        gender = 'temp' 
        with self.assertRaises(ValidationError) as cm: 
            user = User.objects.create_superuser(username='test', email='test@test.com', gender=gender) 
        error = cm.exception 
        self.assertEqual(error.message, 'Gender value can only be "male", "female" and "wont-say". %s is not allowed.' %gender) 
     
    
    def test_gender_default_value(self): 
        User = get_user_model() 
        gender = 'wont-say' 
        user = User.objects.create(username='temp') 
        self.assertEqual(user.gender, gender) 
        
      