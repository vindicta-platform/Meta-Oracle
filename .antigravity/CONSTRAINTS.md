# Meta-Oracle Constraints

> Critical rules agents MUST follow when modifying this repository.

## ⛔ Hard Constraints

1. **All AI Calls via Agent-Auditor-SDK** - Never call Gemini API directly
2. **Quota-Aware Operations** - Check quota before initiating debates
3. **Async-First** - All debate operations must be async
4. **Deterministic Fallbacks** - Provide fallback when AI unavailable

## 🤖 Council Rules

### Agent Behavior
- Agents must NOT share internal state during debates
- Each agent response must be independently generated
- Arbiter cannot override unanimous dissent

### Debate Protocol
```
MAX_ROUNDS = 3
MIN_AGENTS = 2
CONSENSUS_THRESHOLD = 0.66
TIMEOUT_SECONDS = 30
```

### Response Format
All agent responses must include:
- `position: string` - Clear stance
- `confidence: float` - 0.0-1.0
- `reasoning: string[]` - Supporting arguments
- `citations: string[]` - Data references

## ⚠️ Schema Compatibility

### List Grader Output
```python
{
    "grade": "A" | "B" | "C" | "D" | "F",
    "score": float,  # 0-100
    "qualitative": {...},  # Council consensus (60%)
    "quantitative": {...}  # Heuristic eval (40%)
}
```

## 🔒 Security Rules

- No PII in debate transcripts
- API keys via environment variables only
- Rate limit: 10 debates/minute

## 🧪 Testing Requirements

Before merging:
- [ ] `pytest` passes
- [ ] Async tests complete within timeout
- [ ] Mock AI responses for unit tests
- [ ] Integration tests use sandbox quotas
