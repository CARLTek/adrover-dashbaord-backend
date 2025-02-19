from django.db import models

class AdRecord(models.Model):
    ad_id = models.CharField(max_length=255, unique=True, help_text="Unique identifier for the ad")
    timestamp = models.DateTimeField(help_text="Date and time when the ad was played")
    total_persons = models.IntegerField(help_text="Total persons detected")

    def __str__(self):
        return f"{self.ad_id} - {self.timestamp}"

    class Meta:
        ordering = ["-timestamp"]
        db_table = "ad_record"

    def get_all_ad_analytics(self):
        return self.ad_analytics.all()

class AdAnalytics(models.Model):
    ad_record = models.ForeignKey(AdRecord, on_delete=models.CASCADE, related_name="ad_analytics", help_text="Ad record to which this person belongs")
    person_id = models.IntegerField(help_text="Unique person ID within the context of an ad")
    counted = models.BooleanField(help_text="Whether this person was counted")
    age = models.IntegerField(null=True, blank=True, help_text="Age of the person")
    gender = models.CharField(max_length=10, null=True, blank=True, help_text="Gender of the person")

    def __str__(self):
        return f"Person {self.person_id} - {self.gender} ({self.age})"

    class Meta:
        db_table = "ad_analytics"
