# TravelAssistant — Multi-Agent AI & Tool-Calling Demo

**An agentic AI workflow built with CrewAI, Python, Mistral LLMs, and custom tool calling.**

TravelAssistant is a multi-agent AI application that demonstrates how specialized LLM agents can collaborate to process a travel request and execute an action through a custom tool.

Instead of relying on a single prompt-response interaction, the project separates responsibilities across multiple AI agents and tasks. CrewAI orchestrates the workflow, while a custom Python tool simulates sending flight-booking information to an external backend service.

The project was built to explore practical **agent orchestration, role-based AI workflows, tool calling, task decomposition, and modular agent architecture**.

---

## Why This Project

Traditional LLM applications often follow a simple pattern:

```text
User Input → LLM → Text Response
```

TravelAssistant explores a more agentic approach:

```text
User Input
    ↓
Specialized AI Agents
    ↓
Structured Tasks
    ↓
CrewAI Orchestration
    ↓
Tool Selection & Execution
    ↓
Simulated External Action
    ↓
Booking Result
```

The goal is to demonstrate how an AI system can go beyond generating text and instead coordinate specialized components to perform a workflow and invoke tools.

---

## Key Features

### Multi-Agent Architecture

The system uses multiple CrewAI agents with different responsibilities.

**Flight Booking Agent**

* Receives structured passenger and travel information
* Handles the booking-related reasoning task
* Produces a booking confirmation based on the supplied information

**Flight Booker / Processing Agent**

* Handles the action-oriented part of the workflow
* Has access to the custom `BookFlightTool`
* Uses tool calling to process booking information

This separation demonstrates how responsibilities can be distributed across specialized agents instead of placing the entire workflow inside one prompt.

---

### Custom Tool Calling

The project implements a custom CrewAI tool:

```python
@tool("BookFlightTool")
def BookFlightTool(user_input):
    ...
```

The tool simulates interaction with an external booking backend and returns booking confirmation data.

This demonstrates an important agentic AI pattern:

```text
LLM decides what needs to happen
            ↓
Agent selects an available tool
            ↓
Tool executes application logic
            ↓
Result returns to the workflow
```

In a production system, the simulated booking tool could be replaced with a real REST API, database operation, CRM action, or another external service.

---

## Agent Workflow

The application follows this high-level process:

### 1. Collect User Input

The command-line interface collects:

* Passenger name
* Departure city
* Destination city
* Travel date

```text
Passenger Name
Departure City
Destination City
Travel Date
      ↓
Travel Request
```

### 2. Create Specialized Tasks

`TaskFactory` converts the request into separate CrewAI tasks.

The booking task provides the travel information to the Flight Booking Agent.

The processing task provides the request to the tool-enabled processing agent.

### 3. Assemble the Crew

`CrewManager` receives the agents and their corresponding tasks and creates a CrewAI `Crew`.

```text
Agents + Tasks
      ↓
CrewManager
      ↓
CrewAI Crew
```

### 4. Execute the Agent Workflow

The crew is started using:

```python
crew.kickoff()
```

CrewAI coordinates the agents and tasks through the workflow.

### 5. Invoke the Booking Tool

The processing agent has access to `BookFlightTool`, allowing the workflow to move from LLM reasoning to an application action.

### 6. Return the Result

The final result is returned to the command-line interface.

---

## Architecture

```text
┌─────────────────────────────┐
│          User Input         │
│                             │
│  Passenger                  │
│  Departure City             │
│  Destination City           │
│  Travel Date                │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│         TaskFactory         │
│                             │
│  Booking Task               │
│  Processing Task            │
└──────────────┬──────────────┘
               │
               ▼
┌──────────────────────────────────────────────┐
│                  CrewAI Crew                 │
│                                              │
│  ┌──────────────────┐   ┌─────────────────┐ │
│  │ Flight Booking   │   │ Flight Booker   │ │
│  │ Agent            │   │ Agent           │ │
│  │                  │   │                 │ │
│  │ Booking Logic    │   │ Tool Execution  │ │
│  └──────────────────┘   └────────┬────────┘ │
│                                  │          │
└──────────────────────────────────┼──────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │  BookFlightTool   │
                         │                   │
                         │ Simulated Backend │
                         │ Action            │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │  Booking Result   │
                         └───────────────────┘
```



## Tech Stack

### Agentic AI

* CrewAI
* Multi-agent orchestration
* Role-based agents
* Task-based workflows
* Custom tool calling

### Artificial Intelligence

* Mistral LLM
* LLM-driven agents
* Tool-enabled AI workflows

### Development

* Python
* python-dotenv
* Git
* GitHub

---

## Project Structure

```text
TravelAssistant_CrewAI_Demo/
│
├── main.py
│   └── Application entry point and user-input workflow
│
├── agents.py
│   └── Creates specialized CrewAI agents
│
├── tasks.py
│   └── Defines tasks assigned to the agents
│
├── crew_manager.py
│   └── Builds and executes the CrewAI crew
│
├── flightbook_utility.py
│   └── Custom BookFlightTool implementation
│
├── config.py
│   └── Environment configuration and Mistral LLM setup
│
├── ClassDiagram _ Mermaid Chart.png
│   └── Architecture/class diagram
│
└── README.md
```

---

## Design Decisions

### Separation of Agent Responsibilities

Rather than creating one large agent responsible for the entire workflow, the application separates booking and processing responsibilities.

This makes the architecture easier to understand and provides a foundation for adding more specialized agents later.

For example:

```text
Travel Request
     │
     ├── Flight Search Agent
     ├── Booking Agent
     ├── Validation Agent
     └── Communication Agent
```

---

### Factory Pattern for Agents

`AgentFactory` centralizes the creation of CrewAI agents.

```python
factory = AgentFactory(llm)

booking_agent = factory.create_booking_agent()
processing_agent = factory.create_processing_agent()
```

This separates agent configuration from the application entry point and makes the system easier to extend.

---

### Factory Pattern for Tasks

`TaskFactory` follows a similar approach for workflow tasks.

This keeps task definitions separate from orchestration logic and allows agent responsibilities and prompts to evolve independently.

---

### Dedicated Crew Orchestration

`CrewManager` encapsulates the creation and execution of the CrewAI crew.

Instead of putting orchestration logic directly inside `main.py`, the project separates:

```text
Configuration
      ↓
Agent Creation
      ↓
Task Creation
      ↓
Crew Orchestration
      ↓
Execution
```

This creates clearer boundaries between application components.

---

### Tools as an Action Layer

The `BookFlightTool` represents the boundary between AI reasoning and application behavior.

The agent does not directly contain the booking implementation. Instead, it receives access to a tool that performs the action.

This pattern can be extended to real-world integrations such as:

* REST APIs
* databases
* internal business systems
* CRM platforms
* search services
* communication systems

---

## Getting Started

### Prerequisites

* Python 3
* pip
* A Mistral API key

---

### 1. Clone the Repository

```bash
git clone https://github.com/anbat21/TravelAssistant_CrewAI_Demo.git
cd TravelAssistant_CrewAI_Demo
```

---

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install crewai python-dotenv
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project directory.

```env
MISTRAL_API_KEY=your_mistral_api_key
MISTRAL_MODEL_NAME=your_model_name
```

Do not commit API keys or other secrets to GitHub.

---

### 5. Run the Application

```bash
python main.py
```

The application will request the travel information required for the workflow:

```text
Hi! I am an AI Travel Assistant.

Enter passenger name:
Enter departure city:
Enter destination city:
Enter travel date:
```

The information is then passed into the CrewAI workflow.

---

## What This Project Demonstrates

This project focuses on several concepts that are increasingly important when building agentic AI applications:

**Agent specialization**
Different agents receive different roles, goals, and responsibilities.

**Task decomposition**
A larger workflow is divided into explicit tasks rather than handled by one monolithic prompt.

**Agent orchestration**
CrewAI coordinates agents and their assigned tasks.

**Tool calling**
An AI agent is given access to application functionality through a custom tool.

**Separation of concerns**
Configuration, agents, tasks, tools, orchestration, and application entry-point logic are separated into dedicated modules.

**Extensibility**
The simulated tool layer provides a clear path toward integrating real APIs and business systems.

---

## From Demo to Production

TravelAssistant is intentionally a demonstration of agent orchestration and tool calling rather than a production flight-booking service.

A production version could extend the architecture with:

* Real flight-search and booking APIs
* REST API backend
* Persistent database storage
* Authentication and authorization
* Input validation
* Structured tool schemas
* Error handling and retry strategies
* Agent guardrails
* Observability and tracing
* Automated testing
* Human approval before final booking
* Web or mobile frontend
* Cloud deployment

The same architectural pattern could also be adapted beyond travel.

For example:

```text
Investor Research
      ↓
Research Agent
      ↓
Qualification Agent
      ↓
CRM Tool
      ↓
Communication Workflow
```

or:

```text
Customer Request
      ↓
Classification Agent
      ↓
Specialized Agent
      ↓
Business Tool / API
      ↓
Human Review
```

---

## What I Learned

Building TravelAssistant helped me explore how LLM applications can move beyond basic chat interfaces.

The project gave me hands-on experience with:

* Designing specialized AI agents
* Defining agent roles and goals
* Breaking workflows into tasks
* Orchestrating multiple agents with CrewAI
* Connecting agents to custom Python tools
* Separating AI reasoning from application actions
* Structuring an agentic AI project into modular components
* Configuring external LLMs using environment variables

The most important takeaway was that an agentic system is not only about prompting an LLM. The surrounding architecture — **agents, tools, task boundaries, orchestration, application logic, and external integrations** — determines what the system can actually accomplish.

---

## Future Improvements

Planned areas for further development include:

* Replace simulated booking with a real travel API
* Add structured validation for booking data
* Improve tool input/output schemas
* Add automated unit and integration tests
* Implement exception handling and fallback logic
* Add human-in-the-loop booking approval
* Expose the agent workflow through a REST API
* Build a web interface
* Add persistent booking history
* Add workflow observability and execution tracing


LinkedIn:
https://www.linkedin.com/in/batandinh
