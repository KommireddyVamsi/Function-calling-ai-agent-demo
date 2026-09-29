# Azure Domino AI Agent Demo

## Overview

This project demonstrates a simple AI Agent built using Azure OpenAI and Python.

The agent can:

* Accept natural language questions from users
* Decide whether external server information is required
* Call a custom tool to retrieve Domino server details
* Send tool results to Azure OpenAI
* Generate intelligent, context-aware responses

This example illustrates the core concepts behind Agentic AI:

* Reasoning
* Tool Calling
* Decision Making
* LLM + External Data Integration

---

## Architecture

User Question

↓

AI Agent

↓

Decision Engine

↓

Tool Execution (Domino Server Status)

↓

Azure OpenAI (GPT-4.1)

↓

Final Response

---

## Features

### Intelligent Decision Making

The agent analyzes the user question and determines whether server information is required.

Examples:

* "What is the status of my Domino server?"
* "How many users are connected?"
* "Is the Domino environment healthy?"

When such questions are detected, the agent automatically invokes a monitoring tool.

### Tool Calling

The project contains a sample tool:

`get_domino_server_status()`

The tool returns:

* Server Name
* Current Status
* Connected Users
* Mail Queue Size
* Last Backup Time

In a production environment, this tool could connect to:

* HCL Domino REST APIs
* Domino Administrator APIs
* SQL Databases
* Monitoring Platforms
* ServiceNow
* Splunk
* Custom Internal Services

### Azure OpenAI Integration

The agent sends both:

* User question
* Tool results

to Azure OpenAI GPT-4.1 for intelligent response generation.

---

## Technologies Used

* Python
* Azure OpenAI
* GPT-4.1
* OpenAI Python SDK
* JSON

---

## Project Structure

```text
azure-domino-ai-agent-demo/
│
├── AI-Functioncalling.py
├── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/azure-domino-ai-agent-demo.git

cd azure-domino-ai-agent-demo
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Azure OpenAI Configuration

Update the following values:

```python
API_KEY = "YOUR_AZURE_OPENAI_KEY"

BASE_URL = "YOUR_AZURE_OPENAI_ENDPOINT"

MODEL_NAME = "gpt-4.1"
```

Example:

```python
BASE_URL = "https://your-resource.openai.azure.com/openai/v1/"
```

---

## Run Application

```bash
python agent.py
```

Example:

```text
Ask: What is the status of my Domino server?
```

Output:

```text
Agent Decision:
Need server information -> Calling Tool

AI Agent:
The Domino server DOMINO-PROD-01 is currently running successfully. There are 450 active users connected, the mail queue contains 5 pending messages, and the most recent backup was completed on 2026-07-29 at 02:00 AM.
```

---

## Learning Objectives

This project helps beginners understand:

* Agentic AI Fundamentals
* Tool Calling Workflows
* Function Integration with LLMs
* Azure OpenAI Usage
* AI-Powered IT Support Automation
* Domino Monitoring Use Cases

---

## Future Enhancements

* Real Domino Server Integration
* REST API Connectivity
* SQL Database Queries
* Multi-Tool Agent Architecture
* ServiceNow Integration
* Splunk Log Analysis
* Backup Monitoring
* Health Check Dashboard
* Autonomous Troubleshooting Agent

---

## Disclaimer

This is a learning and demonstration project. The current server data is simulated and intended to showcase Agentic AI concepts using Azure OpenAI and Python.
