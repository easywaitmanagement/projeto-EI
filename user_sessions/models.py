from django.db import models
from django.contrib.auth.models import User

class UserSession(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='session_data')
    preferences = models.JSONField(default=dict)  # Store JSON-formatted settings
    last_login_time = models.DateTimeField(auto_now_add=True)
    data = models.TextField(blank=True, null=True)  # General-purpose data field

    def __str__(self):
        return f"Session for {self.user.username}"
    

class Senhas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="senhas")
    number = models.CharField(max_length=4)  # Store the generated number as a 4-digit string
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the number was created

    def __str__(self):
        return f"{self.number} (User: {self.user.username})"

