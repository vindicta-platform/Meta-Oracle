# Tasks: DebateEngine Async Core

**Input**: specs/017-debate-engine/ | **Prerequisites**: spec.md, plan.md

## Phase 1: Setup

- [ ] T001 Create `src/engine/` directory structure
- [ ] T002 [P] Create `src/models/debate.py`

---

## Phase 2: Foundational

- [ ] T003 Define DebateSession Pydantic model
- [ ] T004 [P] Define DebateRound Pydantic model
- [ ] T005 Create base DebateEngine class

---

## Phase 3: User Story 1 - Run Async Debate (P1) 🎯 MVP

- [ ] T006 [US1] Implement `async run_debate()` method
- [ ] T007 [US1] Orchestrate multiple agent rounds
- [ ] T008 [US1] Collect agent responses per round
- [ ] T009 [US1] Build structured transcript
- [ ] T010 [US1] Return consensus with transcript
- [ ] T011 [US1] Add timeout configuration

---

## Phase 4: User Story 2 - Cancel Long-Running Debate (P2)

- [ ] T012 [US2] Add cancellation token support
- [ ] T013 [US2] Implement graceful termination
- [ ] T014 [US2] Return partial transcript on cancel

---

## Phase 5: Polish

- [ ] T015 [P] Write async unit tests
- [ ] T016 [P] Add logging for debugging
