#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# main.py
from config import Config
from agents import AgentFactory
from tasks import TaskFactory
from crew_manager import CrewManager

def collect_user_input():
    """Takes user input for booking"""
    print("Hi! I am an AI Travel Assistant. Please input the following information.")
    return {
        "passenger_name": input("Enter passenger name: "),
        "from_city": input("Enter departure city: "),
        "to_city": input("Enter destination city: "),
        "travel_date": input("Enter travel date (YYYY-MM-DD): ")
    }

def main():
    # Load config and LLM
    config = Config()
    llm = config.get_llm()

    # Initialize agents
    factory = AgentFactory(llm)
    booking_agent = factory.create_booking_agent()
    processing_agent = factory.create_processing_agent()

    # Collect input
    user_input = collect_user_input()

    # Create tasks
    tasks = [
        TaskFactory.create_booking_task(
            booking_agent,
            user_input["passenger_name"],
            user_input["from_city"],
            user_input["to_city"],
            user_input["travel_date"]
        ),
        TaskFactory.create_processing_task(processing_agent, user_input)
    ]

    # Run crew
    crew_manager = CrewManager(agents=[booking_agent, processing_agent], tasks=tasks)
    result = crew_manager.run()

    print("\nResult:\n", result)

if __name__ == "__main__":
    main()
