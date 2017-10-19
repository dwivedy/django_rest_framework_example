# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ecommr_home.models import EcommrHomeModle
from ecommr_home.serializers import EcommrHomeSerializer
from rest_framework import generics

# Create your views here.

class EcommrHomeListView(generics.ListCreateAPIView):
    queryset = EcommrHomeModle.objects.all()
    serializer_class = EcommrHomeSerializer
