from django.db import models

# Create your models here.
class Agentname(models.Model):
    name_id = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=2000, blank=True, null=True)
    lastname = models.CharField(max_length=2000, blank=True, null=True)
    email = models.CharField(max_length=2000, blank=True, null=True)
    phone = models.CharField(max_length=2000, blank=True, null=True)
    pollingunit_uniqueid = models.IntegerField(blank=True, null=True)

class AnnouncedLgaResults(models.Model):
    result_id = models.IntegerField(blank=True, null=True)
    lga_name = models.CharField(max_length=2000, blank=True, null=True)
    party_abbreviation = models.CharField(max_length=2000, blank=True, null=True)
    party_score = models.IntegerField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=2000, blank=True, null=True)
    date_entered = models.DateField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=2000, blank=True, null=True)

class AnnouncedPuResults(models.Model):
    result_id = models.IntegerField(blank=True, primary_key=True)
    polling_unit_uniqueid = models.IntegerField(blank=True, null=True)
    party_abbreviation = models.CharField(max_length=2000, blank=True, null=True)
    party_score = models.IntegerField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=2000, blank=True, null=True)
    date_entered = models.CharField(max_length=2000, blank=True, null=True)
    user_ip_address = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
       managed = True
       db_table = 'announced_pu_results'

class AnnouncedStateResults(models.Model):
    result_id = models.IntegerField(blank=True, null=True)
    state_name = models.CharField(max_length=2000, blank=True, null=True)
    party_abbreviation = models.CharField(max_length=2000, blank=True, null=True)
    party_score = models.IntegerField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=2000, blank=True, null=True)
    date_entered = models.CharField(max_length=2000, blank=True, null=True)
    user_ip_address = models.CharField(max_length=2000, blank=True, null=True)


class AnnouncedWardResults(models.Model):
    result_id = models.IntegerField(blank=True, null=True)
    ward_name = models.CharField(max_length=2000, blank=True, null=True)
    party_abbreviation = models.CharField(max_length=2000, blank=True, null=True)
    party_score = models.IntegerField(blank=True, null=True)
    entered_by_user = models.CharField(max_length=2000, blank=True, null=True)
    date_entered = models.CharField(max_length=2000, blank=True, null=True)
    user_ip_address = models.CharField(max_length=2000, blank=True, null=True)

class Lga(models.Model):
    uniqueid = models.IntegerField(blank=True, null=True)
    lga_id = models.IntegerField(blank=True, primary_key=True)
    lga_name = models.CharField(max_length=2000, blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    lga_description = models.CharField(max_length=2000, blank=True, null=True)
    entered_by_user = models.CharField(max_length=2000, blank=True, null=True)
    date_entered = models.CharField(max_length=2000, blank=True, null=True)
    user_ip_address = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lga'

class Party(models.Model):
    id = models.IntegerField(primary_key=True)
    partyid = models.IntegerField(blank=True, null=True)
    partyname = models.CharField(max_length=2000, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'party'


class PollingUnit(models.Model):
    uniqueid = models.IntegerField(blank=True, primary_key=True)
    polling_unit_id = models.IntegerField(blank=True, null=True)
    ward_id = models.IntegerField(blank=True, null=True)
    lga_id = models.IntegerField(blank=True, null=True)
    uniquewardid = models.IntegerField(blank=True, null=True)
    polling_unit_number = models.IntegerField(blank=True, null=True)
    polling_unit_name = models.CharField(max_length=2000, blank=True, null=True)
    polling_unit_description = models.CharField(max_length=2000, blank=True, null=True)
    lat = models.CharField(max_length=2000, blank=True, null=True)
    long = models.CharField(max_length=2000, blank=True, null=True)
    entered_by_user = models.CharField(max_length=2000, blank=True, null=True)
    date_entered = models.DateField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'polling_unit'


class States(models.Model):
    state_id = models.IntegerField(blank=True, null=True)
    state_name = models.CharField(max_length=2000, blank=True, null=True)


class Ward(models.Model):
    uniqueid = models.IntegerField(blank=True, null=True)
    ward_id = models.IntegerField(blank=True, primary_key=True)
    ward_name = models.CharField(max_length=2000, blank=True, null=True)
    lga_id = models.IntegerField(blank=True, null=True)
    ward_description = models.CharField(max_length=2000, blank=True, null=True)
    entered_by_user = models.CharField(max_length=2000, blank=True, null=True)
    date_entered = models.CharField(max_length=2000, blank=True, null=True)
    user_ip_address = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ward'



