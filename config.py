#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# config.py
import os
from dotenv import load_dotenv
from crewai import LLM

class Config:
    """Loads environment variables and configures the LLM"""

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("MISTRAL_API_KEY")
        self.model = os.getenv("MISTRAL_MODEL_NAME")
        os.environ["MISTRAL_API_KEY"] = self.api_key
        os.environ["MISTRAL_MODEL_NAME"] = self.model

    def get_llm(self):
        """Returns initialized LLM"""
        return LLM(api_key=self.api_key, model=self.model)
