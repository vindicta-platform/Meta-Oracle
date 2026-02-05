# Meta-Oracle Roadmap

> **Vision**: Five Minds, One Truth — AI Council for meta predictions  
> **Status**: Active Development  
> **Last Updated**: 2026-02-04

---

## 📅 6-Week Schedule (Feb 4 - Mar 17, 2026)

> **GitHub Project**: https://github.com/orgs/vindicta-platform/projects/4  
> **Master Roadmap**: https://github.com/vindicta-platform/.github/blob/master/ROADMAP.md

### Week 2: Feb 11-17 — Foundation
| Day | Task | Priority |
|-----|------|----------|
| Mon 11 | DebateEngine core implementation | P1 |
| Tue 12 | Stub agent implementations | P1 |
| Wed 13 | Home agent implementation | P1 |
| Thu 14 | Adversary agent implementation | P1 |
| **Sun 17** | **v0.1.0 Foundation Release** | ⭐ |

### Week 4: Feb 25 - Mar 3 — Agent Implementation
| Day | Task | Priority |
|-----|------|----------|
| Mon 25 | Arbiter agent implementation | P1 |
| Tue 26 | Rule-Sage agent implementation | P1 |
| Wed 27 | Council protocol (part 1) | P1 |
| Thu 28 | Council protocol (part 2) | P1 |
| Fri 1 | Integration tests | P1 |
| **Sun 3** | **v0.2.0 Agents Release** | ⭐ |

### Week 6: Mar 11-17 — User Features
| Day | Task | Priority |
|-----|------|----------|
| Mon 11 | List Grader API | P1 |
| Tue 12 | Upset Detector feature | P1 |
| Wed 13 | Integration testing | P1 |
| **Sun 17** | **v0.3.0 User Features Release** | ⭐ |

---

## v1.0 Target: April 15, 2026

### Mission Statement
Deliver a production-ready AI Council that provides meta predictions, army rankings, and upset detection through structured adversarial debate between 5 specialized agents.

---

## Milestone Timeline

```
┌─────────────────────────────────────────────────────────────────┐
│  Feb 2026          Mar 2026          Apr 2026                   │
│  ─────────────────────────────────────────────────────────────  │
│  [v0.1.0]          [v0.2.0]          [v0.3.0]      [v1.0.0]     │
│  Foundation        Agents            Features      Production   │
│                                                                  │
│  Week 2            Week 4            Week 6        Week 10+     │
└─────────────────────────────────────────────────────────────────┘
```

---

## v0.1.0 — Foundation (Target: Feb 17, 2026)

### Deliverables
- [ ] Extract meta_oracle from platform-core
- [ ] Define agent interfaces
- [ ] DebateEngine core implementation
- [ ] Stub agent implementations (all 5)
- [ ] Home agent (advocate for player's list)
- [ ] Adversary agent (argue against)

### Exit Criteria
- [ ] Basic debate flow works
- [ ] 2 agents can exchange arguments
- [ ] Integration with Agent-Auditor-SDK

---

## v0.2.0 — Agent Implementation (Target: Mar 3, 2026)

### Deliverables
- [ ] Arbiter agent (neutral judging)
- [ ] Rule-Sage agent (rules expertise)
- [ ] Observer agent (historical data)
- [ ] Council debate protocol
- [ ] Verdict aggregation

### Exit Criteria
- [ ] All 5 agents participate in debates
- [ ] Structured debate transcripts
- [ ] Reproducible verdicts

---

## v0.3.0 — User Features (Target: Mar 17, 2026)

### Deliverables
- [ ] List Grader API endpoint
- [ ] Upset Detector (identify giant-killer lists)
- [ ] Meta Snapshot display
- [ ] Historical prediction tracking

### Exit Criteria
- [ ] Grade a list via API
- [ ] Surface unexpected high-performers
- [ ] Track prediction accuracy

---

## v1.0.0 — Production (Target: Apr 15, 2026)

### Deliverables
- [ ] Tournament prediction system
- [ ] Accuracy dashboard
- [ ] PyPI publication
- [ ] 70%+ prediction accuracy

### Exit Criteria
- [ ] Public prediction tracking
- [ ] Community-validated accuracy
- [ ] Stable API for Portal integration

---

## The Council: 5 Agents

| Agent | Role | Specialty |
|-------|------|-----------|
| **Home** | Advocate | Argues FOR the player's list |
| **Adversary** | Devil's advocate | Argues AGAINST the list |
| **Arbiter** | Neutral judge | Weighs evidence, makes verdict |
| **Rule-Sage** | Expert | Validates mechanics and rules claims |
| **Observer** | Historian | Provides historical context and precedent |

---

## Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| Agent-Auditor-SDK | 🔄 Parallel | Quota management |
| Primordia AI | 🔄 Parallel | Position evaluation (optional) |
| WARScribe-Core | 🔄 Parallel | List parsing |

---

## Success Criteria for v1

1. **Accuracy**: 70%+ prediction accuracy tracked publicly
2. **Coverage**: Grade any valid army list
3. **Transparency**: Debate transcripts available
4. **Community Trust**: Monthly "Giant Killer" identification

---

*Maintained by: Vindicta Platform Team*
