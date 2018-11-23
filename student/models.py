# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class StudentProfile(User):
	sex=[("M","Male"),("F","Female")]
	age=models.IntegerField()
	gender=models.CharField(max_length=10,choices=sex)

	class Meta:
		db_table="studentprofile"
