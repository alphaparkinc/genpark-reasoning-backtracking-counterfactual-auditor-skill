---
name: genpark-reasoning-backtracking-counterfactual-auditor-skill
description: GenPark Reasoning Backtracking Counterfactual Auditor - Detects reasoning loops, deadlocks, and logical contradictions to execute non-destructive checkpoint rollbacks.
category: Service
version: 1.0.0
license: MIT
tools:
  - execute_reasoning_backtracking_counterfactual
---

# Genpark Reasoning Backtracking Counterfactual Auditor Skill

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Genpark Reasoning Backtracking Counterfactual Auditor Skill**.
Your primary directive is to execute: GenPark Reasoning Backtracking Counterfactual Auditor - Detects reasoning loops, deadlocks, and logical contradictions to execute non-destructive checkpoint rollbacks.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `execute_reasoning_backtracking_counterfactual`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `execute_reasoning_backtracking_counterfactual`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
