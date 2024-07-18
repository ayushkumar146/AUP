from django.db import models

class CodeSubmission(models.Model):
    language = models.CharField(max_length=10)
    code = models.TextField()
    input_data = models.TextField(blank=True, null=True)
    output_data = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    desired_output = models.TextField(blank=True, null=True)  # Add this line

    def __str__(self):
        return f"Submission in {self.language}"
