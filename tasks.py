#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# tasks.py
from crewai import Task

class TaskFactory:
    """Creates tasks for the agents"""

    @staticmethod
    def create_booking_task(agent, passenger_name, from_city, to_city, travel_date):
        return Task(
            description=(
                f"Book a flight for a user with the following details:\n"
                f"- Passenger Name: {passenger_name}\n"
                f"- From: {from_city}\n"
                f"- To: {to_city}\n"
                f"- Date: {travel_date}\n"
                "Return a confirmation message with the provided details."
            ),
            agent=agent,
            expected_output="A string message confirming the booking"
        )

    @staticmethod
    def create_processing_task(agent, user_input):
        return Task(
            description=(
                f"Use the given tool-booking_tool to process this info: {user_input}. "
                "Return the formatted result."
            ),
            agent=agent,
            expected_output="Formatted booking information"
        )
