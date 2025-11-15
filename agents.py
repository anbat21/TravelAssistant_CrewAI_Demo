#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# agents.py
from crewai import Agent
from flightbook_utility import BookFlightTool

class AgentFactory:
    """Factory to create agents used in the flight booking crew"""

    def __init__(self, llm):
        self.llm = llm

    def create_booking_agent(self):
        return Agent(
            llm=self.llm,
            role="Flight Booking Agent",
            goal="Help users book flights efficiently",
            backstory="You work for a travel agency that specializes in booking domestic and international flights.",
            verbose=True,
            allow_delegation=False
        )

    def create_processing_agent(self):
        return Agent(
            llm=self.llm,
            role="Flight Booker",
            goal="You will use the tool to book a flight using all the information given by the user.",
            backstory="""You will use the given tool to book a flight for the user. 
            Call this whenever a customer asks 'I want to book a flight from Los Angeles to New York'""",
            tools=[BookFlightTool],
            verbose=False
        )
