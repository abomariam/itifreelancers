from django.db import models
# Create your models here.


class Intake(models.Model):
    name = models.CharField(max_length=150)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=150)
    site = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class Freelancer(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    city = models.ForeignKey(City, related_name='freelancers')

    is_from_cs_background = models.BooleanField(default=False)

    intake = models.ForeignKey(Intake, blank=True, null=True, related_name='freelancers')

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class WorkingField(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Profile(models.Model):
    url = models.URLField()

    STATUS_INREVIEW = 'in-review'
    STATUS_APPROVED = 'approved'
    STATUS_SUSPENDED = 'suspended'

    STATUS_CHOICES = (
        (STATUS_INREVIEW, 'In Review'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_SUSPENDED, 'Suspended'),
    )

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_INREVIEW)
    working_field = models.ForeignKey(WorkingField, related_name='profiles')

    platform = models.ForeignKey(Platform, related_name='profiles')
    freelancer = models.ForeignKey(Freelancer, related_name='profiles')

    joined_at = models.DateField(blank=True, null=True)

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{} ({})'.format(self.freelancer.name, self.platform.name)


class Country(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class Job(models.Model):
    profile = models.ForeignKey(Profile, related_name='jobs')
    url = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)

    working_field = models.ForeignKey(WorkingField, blank=True, null=True, related_name='jobs')

    cover_letter = models.TextField(blank=True, null=True)

    JOB_TYPE_CHOICES = (
        ('hourly', 'Hourly'),
        ('fixed-price', 'Fixed Price'),
    )
    job_type = models.CharField(max_length=150, blank=True, null=True, choices=JOB_TYPE_CHOICES)

    rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    client_country = models.ForeignKey(Country, blank=True, null=True)
    applied_at = models.DateField(blank=True, null=True)

    is_interviewed = models.NullBooleanField(blank=True, null=True)
    interviewed_at = models.DateField(blank=True, null=True)
    INTERVIEW_CHANNEL_CHOICES = (
        ('chat', 'Text Chat'),
        ('voice', 'Voice Chat'),
        ('video', 'Video Chat'),
    )

    interview_channel = models.CharField(max_length=150, blank=True, null=True, choices=INTERVIEW_CHANNEL_CHOICES)

    interview_notes = models.TextField(blank=True, null=True)

    is_hired = models.NullBooleanField(blank=True, null=True)
    hired_at = models.DateField(blank=True, null=True)

    hiring_notes = models.TextField(blank=True, null=True)

    is_completed_successfully = models.NullBooleanField(blank=True, null=True)
    is_disputed = models.NullBooleanField(blank=True, null=True)

    dispute_notes = models.TextField(blank=True, null=True)

    total_working_hours = models.IntegerField(blank=True, null=True)
    total_job_income = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    notes = models.TextField(blank=True, null=True)

    closed_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.title or self.id, self.profile.freelancer.name)

