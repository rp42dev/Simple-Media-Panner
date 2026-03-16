# Project Architecture

## Overview
This project uses a modular CrewAI pipeline for dental content generation, with each agent responsible for a single task. The system is designed for extensibility and integration with FastAPI and Next.js.

## Data Flow
Input Topic → Topic Agent → Strategy Agent → Research Agent → Writer Agent → Formatter Agent → Visual Agent → Output JSON

## Agents
- Topic Agent: Generates subtopics
- Strategy Agent: Assigns category/tone
- Research Agent: Gathers key points
- Writer Agent: Produces content
- Formatter Agent: Formats for platforms
- Visual Agent: Suggests visuals

## Orchestration
- Crew and pipeline modules coordinate agent execution and output aggregation.
