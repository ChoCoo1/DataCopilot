# app/views.py
from rest_framework import generics
from .serializers import *
from .models import *
from langchain.chains import create_sql_query_chain
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from translate import Translator

from rest_framework.decorators import api_view
import pymysql
import os

# 初始化 OpenAI 客户端

API_SECRET_KEY = "sk-4wJ2VKu3VL1fegJz5e3e930971B74e588343Cb774f9eB936"
BASE_URL = "https://api.gpts.vin/v1"

os.environ["OPENAI_API_KEY"] = API_SECRET_KEY
os.environ["OPENAI_API_BASE"] = BASE_URL
