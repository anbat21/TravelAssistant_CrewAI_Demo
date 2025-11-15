# if you have not installed Crewai_tools use the below command
# pip install crewai[tools]
from crewai.tools import tool

@tool("BookFlightTool")
def BookFlightTool(user_input: dict) -> str:
    # simply returns a string
    """Simulates sending booking data to an external backend and returns confirmationPrints a confirmation message that flight is booked.
    For example 'A June-10-2025 flight has been booked from Los Angeles to London for George.'

        """
    print(f"name: {user_input[0]}")
    print(f"from city: {user_input[1]}")
    print(f"to_city: {user_input[2]}")
    return {"response": f"A {user_input[3]} flight has been booked from {user_input[1]} to {user_input[2]} for {user_input[0]}"}
