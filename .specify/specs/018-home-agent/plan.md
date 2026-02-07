# Implementation Plan: Home Agent

**Branch**: `018-home-agent` | **Date**: 2026-02-06 | **Spec**: [spec.md](./spec.md)

## Summary

Advocacy agent that argues for the strengths of submitted army lists. Provides counterarguments during debate rounds.

## Technical Context

**Language/Version**: Python 3.11  
**Primary Dependencies**: Gemini API, Pydantic  
**Storage**: N/A (stateless)  
**Testing**: pytest  
**Target Platform**: Meta-Oracle  
**Project Type**: Backend library  

## Project Structure

```text
Meta-Oracle/src/
└── agents/
    ├── home.py              # [NEW] Home agent implementation
    └── prompts/home.md      # [NEW] Agent prompt template
```
