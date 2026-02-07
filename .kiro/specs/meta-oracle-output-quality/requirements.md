# Requirements Document

## Introduction

The Meta-Oracle currently produces highly speculative and often hallucinated tabletop wargaming predictions with no grounding in actual rules or stats. This feature establishes a **Correctness Framework**—a multi-layered system for grounding, verifying, and measuring the factual accuracy of predictions. It transforms the Meta-Oracle from an "interesting idea" into a **trustworthy, rules-verified prediction engine** for competitive Warhammer 40,000.

This requirements document covers:
1. **Data Grounding**: Connecting agents to verified rule data via WARScribe-Core
2. **Structured Claims**: Enforcing machine-parseable outputs from all agents
3. **Verification Pipeline**: A dedicated Rule-Sage audit loop to validate claims
4. **Correctness Measurement**: OKRs and metrics for factuality, hallucination, and prediction accuracy
5. **Platform Integration**: Hooks into Agent-Auditor-SDK, Primordia-AI, and DuckDB for enterprise-grade operation

## Glossary

- **Meta-Oracle**: The prediction engine system that generates tactical predictions for Warhammer 40K competitive play
- **Agent**: An AI component within Meta-Oracle that generates arguments and claims (e.g., HomeAgent, AwayAgent, Rule-Sage)
- **Claim**: An atomic, machine-parseable tactical argument made by an agent
- **WARScribe-Core**: The authoritative source for Warhammer 40K 10th Edition rules data
- **Rule-Sage**: A specialized verification agent that audits claims against the knowledge base
- **Knowledge_Base**: The DuckDB database containing indexed rules, units, abilities, and stratagems from WARScribe-Core
- **Debate_Engine**: The orchestration system that manages multi-agent debates
- **Hallucination**: A claim that references non-existent rules, units, or abilities
- **Factuality_Score**: A calculated metric measuring the accuracy of claims in a debate session
- **Agent-Auditor-SDK**: The platform service managing API quotas and token tracking
- **Primordia-AI**: The tactical evaluation system providing heuristic scores for matchups
- **Structured_Claim**: A Pydantic schema enforcing machine-parseable claim format
- **Verification_Result**: An audit log entry documenting the verification status of a claim
- **Rule_Debate_Round**: A sub-round within the main debate for resolving ambiguous rule interpretations
- **Knowledge_Context**: A dynamically-generated subset of rules and stats injected into agent prompts

## Requirements

### Requirement 1: Knowledge Base Integration

**User Story:** As a tournament player, I want the Oracle agents to reference actual unit stats and abilities in their arguments, so that I can trust the tactical reasoning.

#### Acceptance Criteria

1. THE Meta-Oracle SHALL integrate read-only access to WARScribe-Core rules data via a shared DuckDB database
2. WHEN the system initializes, THE Knowledge_Base SHALL index all competitive 10th Edition units, abilities, stratagems, and keywords from WARScribe-Core format
3. WHEN an Agent formulates a claim, THE System SHALL provide a Knowledge_Context object populated via Just-In-Time RAG queries
4. THE Knowledge_Context SHALL support filtering by faction, detachment, and unit keywords to minimize prompt size
5. THE System SHALL expose a function to check if unit data is indexed before agents make claims

### Requirement 2: Verifiable Rules References

**User Story:** As a tournament player, I want every mechanical claim to include traceable rule references, so that I can verify the reasoning independently.

#### Acceptance Criteria

1. WHEN a Space Marine list is provided AND the HomeAgent makes a claim about a specific unit, THEN THE Claim SHALL include a RuleRef or UnitRef to the unit's abilities from the Knowledge_Base
2. WHEN an Agent makes a mechanical claim, THEN THE Rule-Sage SHALL audit the claim against the Knowledge_Base
3. IF a claim references data not present in the Knowledge_Base, THEN THE Rule-Sage SHALL flag the claim as UNVERIFIED
4. WHEN a unit is not indexed in the Knowledge_Base, THEN THE Agent SHALL structure the claim with EvidencePath set to "DATA_MISSING"
5. WHEN a unit is not indexed in the Knowledge_Base, THEN THE Agent SHALL NOT fabricate stats or abilities

### Requirement 3: Structured Claim Schema

**User Story:** As a platform developer, I want agents to produce structured arguments, so that I can automatically calculate claim factuality and prediction accuracy.

#### Acceptance Criteria

1. WHEN an Agent generates a response, THEN THE Response SHALL conform to the Pydantic Structured_Claim schema
2. THE Structured_Claim schema SHALL include ClaimID, AgentID, ClaimType, UnitRefs, RuleRefs, EvidencePath, and TacticalScore fields
3. THE EvidencePath field SHALL contain either a valid DuckDB query path or the literal string "DATA_MISSING"
4. WHEN a debate transcript is generated, THEN THE Argument objects SHALL contain a list of Structured_Claim objects instead of raw strings
5. WHEN the validation script runs on a debate transcript, THEN THE System SHALL output a Factuality Report containing overall score and per-claim breakdowns

### Requirement 4: Verification Pipeline

**User Story:** As a platform developer, I want unverified claims to trigger a retry loop, so that agents can self-correct and improve factuality scores.

#### Acceptance Criteria

1. WHEN the Rule-Sage processes a debate round, THEN THE Rule-Sage SHALL verify all claims against the Knowledge_Base
2. FOR each claim, THE Rule-Sage SHALL produce a Verification_Result with status VERIFIED, STAT_ERROR, AMBIGUOUS, UNVERIFIED, or HALLUCINATED
3. WHEN the Rule-Sage flags a claim as UNVERIFIED AND the retry limit has not been reached, THEN THE System SHALL re-prompt the originating Agent with structured error feedback
4. THE System SHALL allow a maximum of 3 retry attempts per claim
5. WHEN an Agent fails to provide a valid claim after 3 retries, THEN THE Claim status SHALL be set to HALLUCINATED and logged to the Factuality Report
6. THE Verification_Result schema SHALL include ClaimID, Status, RetryCount, TokenUsage, and ErrorFeedback fields

### Requirement 5: Ambiguous Rule Resolution

**User Story:** As a tournament organizer, I want the system to explicitly flag and debate ambiguous rule interpretations, so that I can see the reasoning behind contentious calls.

#### Acceptance Criteria

1. WHEN the Rule-Sage detects a claim referencing a rule with AmbiguityFlag set to true, THEN THE System SHALL trigger a Rule_Debate_Round sub-routine
2. WHEN a Rule_Debate_Round is initiated, THEN THE Agents SHALL debate the interpretation until consensus is reached or 5 exchanges are completed
3. WHEN a Rule_Debate_Round concludes, THEN THE Resolution SHALL be recorded as a RuleInterpretation object in the transcript
4. THE RuleInterpretation object SHALL include RuleRef, InterpretedMeaning, AgentVotes, and Consensus fields
5. IF no consensus is reached after 5 exchanges, THEN THE Arbiter SHALL make the final call and the Consensus field SHALL be set to false

### Requirement 6: Factuality Measurement

**User Story:** As a community manager, I want a visual dashboard showing the Oracle's factuality scores over time, so I can build trust with users.

#### Acceptance Criteria

1. WHEN a debate session completes, THE System SHALL calculate a Factuality_Score using the formula: 100 minus (Hallucination count times 10) minus (StatError count times 5) minus (Ambiguity count times 2)
2. WHEN a debate session completes, THE System SHALL calculate a Hallucination Rate as the percentage of hallucinated claims divided by total claims
3. WHEN a debate session completes, THE Factuality Report SHALL be embedded in the DebateTranscript JSON under a quality_metrics key
4. WHEN a debate session completes, THE System SHALL output the Factuality Report as a standalone Markdown file alongside the JSON transcript
5. THE System SHALL provide a CLI command to calculate rolling averages across multiple sessions
6. WHEN the aggregate report command runs on 10 or more sessions, THEN THE System SHALL output a summary table with average Factuality_Score, Hallucination Rate, and Prediction Accuracy

### Requirement 7: Primordia-AI Integration

**User Story:** As a platform developer, I want to enrich agent claims with heuristic scores from Primordia-AI, so that predictions are backed by both rules and tactical evaluation.

#### Acceptance Criteria

1. WHEN an Agent formulates a claim about unit matchups, THEN THE System SHALL request a MatchupEvaluation from the Primordia-AI DuckDB opening book
2. WHEN a MatchupEvaluation is available, THEN THE Structured_Claim SHALL include a TacticalScore field populated from Primordia-AI
3. IF Primordia-AI data is unavailable for a matchup, THEN THE TacticalScore field SHALL be set to null and the claim SHALL proceed without heuristic enrichment

### Requirement 8: Agent-Auditor-SDK Integration

**User Story:** As a platform operator, I want all cloud model calls to be managed by the Agent-Auditor-SDK, so that I never exceed my API quotas.

#### Acceptance Criteria

1. THE System SHALL use Agent-Auditor-SDK for all cloud model API calls to Gemini
2. THE Agent-Auditor-SDK integration SHALL include token tracking, rate limiting for RPM and TPM, and quota persistence
3. WHEN the Agent-Auditor-SDK detects RPM or TPM limits approaching during a debate, THEN THE Debate_Engine SHALL receive a signal to pause or slow down
4. WHEN daily RPD limits are exhausted AND a new debate is requested, THEN THE System SHALL queue the request and return a ServiceTemporarilyUnavailable status
5. THE System SHALL integrate with the TaskQueue from Agent-Auditor-SDK to manage background debate requests when foreground quota is exhausted
6. WHERE the configuration flag MODEL_PROVIDER is set to LOCAL, THE System SHALL bypass Agent-Auditor-SDK and use the OllamaClient for Llama models
7. All platform integrations SHALL be asynchronous using async and await patterns

### Requirement 9: WARScribe-Core Plugin Interface

**User Story:** As a platform developer, I want Meta-Oracle to consume WARScribe-Core's EditionPlugin interface, so that the system can validate actions and calculate game mechanics correctly.

#### Acceptance Criteria

1. THE System SHALL consume the EditionPlugin abstract interface from WARScribe-Core
2. THE System SHALL call EditionPlugin validate_action method to verify the legality of tactical actions
3. THE System SHALL call EditionPlugin calculate_hit_rolls method for tactical simulations
4. THE System SHALL instantiate the appropriate EditionPlugin implementation based on the selected game edition
5. THE System SHALL NOT modify or subclass EditionPlugin implementations
6. THE System SHALL handle EditionPlugin instantiation via a factory pattern keyed by edition_name
7. THE System SHALL NOT write to any WARScribe-Core data files

### Requirement 10: Schema Model Consumption

**User Story:** As a platform developer, I want Meta-Oracle to use WARScribe-Core's schema models, so that data structures are consistent across the platform.

#### Acceptance Criteria

1. THE System SHALL import and use the UnitReference model from WARScribe-Core schema
2. THE System SHALL import and use the Action model from WARScribe-Core schema
3. THE System SHALL import and use the ActionType enum from WARScribe-Core schema
4. WHEN creating Structured_Claim objects, THE System SHALL use UnitReference objects in the unit_refs field
5. WHEN validating claims, THE System SHALL pass Action objects to EditionPlugin validate_action method

### Requirement 11: Performance and Quality Standards

**User Story:** As a platform operator, I want the system to meet performance and quality benchmarks, so that it operates reliably in production.

#### Acceptance Criteria

1. THE System SHALL perform all database operations as read-only against shared DuckDB files
2. WHEN running a 5-round debate with 5 agents on local Ollama with Llama 3.2, THE System SHALL complete in less than 120 seconds
3. WHEN running a single debate session, THE System SHALL use less than 2GB of peak memory
4. THE System SHALL pass ruff linting checks
5. THE System SHALL pass mypy strict type checking
6. THE System SHALL achieve at least 85 percent unit test coverage for engine, knowledge, and verification components
7. WHEN processing claims, THE System SHALL average less than 500 tokens per claim
8. THE System SHALL operate within GCP Free Tier limits with zero standing costs

### Requirement 12: Error Handling and Edge Cases

**User Story:** As a platform developer, I want the system to handle edge cases gracefully, so that debates can proceed even when data is incomplete or ambiguous.

#### Acceptance Criteria

1. WHEN a rule is flagged with AmbiguityFlag set to true, THEN THE Rule-Sage SHALL trigger a Structured Rule-Debate sub-round
2. WHEN a unit is not indexed in the Knowledge_Base, THEN THE Agent SHALL set EvidencePath to "DATA_MISSING" and SHALL NOT hallucinate stats
3. WHEN an Agent exceeds the maximum retry limit, THEN THE Claim status SHALL be set to HALLUCINATED and the round SHALL proceed
4. WHEN API quota is exhausted, THEN THE Agent-Auditor-SDK SHALL persist remaining tasks and THE System SHALL return a 503 status until quota resets
5. WHEN an Agent hits rate limits, THEN THE Agent-Auditor-SDK SHALL apply backpressure and pause the Debate_Engine until safe to resume
6. WHEN agents have conflicting rule interpretations AND no consensus is reached after 5 exchanges, THEN THE Arbiter SHALL make the final call and log Consensus as false
7. WHEN Primordia-AI data is unavailable, THEN THE TacticalScore field SHALL be set to null and the claim SHALL proceed without heuristic enrichment
