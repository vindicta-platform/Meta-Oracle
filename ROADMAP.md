# Meta-Oracle Roadmap

> **Vision**: 5-agent AI Council for meta predictions and upset detection  
> **Status**: Active Development  
> **Last Updated**: 2026-02-03

---

## v1.0 Target: April 2026

### Mission Statement
Deliver a production-ready AI debate engine where 5 specialized agents collaboratively analyze army lists, predict tournament outcomes, and identify meta upsets through adversarial reasoning.

---

## Milestone Timeline

```
┌─────────────────────────────────────────────────────────────────┐
│  Feb 2026          Mar 2026          Apr 2026                   │
│  ─────────────────────────────────────────────────────────────  │
│  [v0.1.0]          [v0.2.0]          [v0.3.0]      [v1.0.0]     │
│  Foundation        Agents           Features       Production   │
│                                                                  │
│  Week 1-2          Week 3-4          Week 5-6      Week 7-8     │
└─────────────────────────────────────────────────────────────────┘
```

---

## v0.1.0 — Foundation (Target: Feb 14, 2026)

### Deliverables
- [ ] Extract meta_oracle module from platform-core
- [ ] Define OracleAgent protocol
- [ ] Implement DebateEngine core
- [ ] Create stub agents (hardcoded responses)
- [ ] Debate transcript serialization

### Key Measurable Results
| Metric | Target | Measurement |
|--------|--------|-------------|
| **Debate Execution** | Complete 5-round debate | Integration test |
| **Transcript Format** | JSON serializable | Schema validation |
| **Agent Protocol** | All 5 agents implement interface | Type checking |

### Exit Criteria
- [ ] Run mock debate with stub agents
- [ ] Transcript viewable as JSON
- [ ] Agent interface documented

---

## v0.2.0 — Agent Implementation (Target: Feb 28, 2026)

### Deliverables
- [ ] Home agent (Gemini-powered)
- [ ] Adversary agent
- [ ] Arbiter agent with DuckDB backend
- [ ] Rule-Sage agent with WARScribe-Core validation
- [ ] Council synthesizer
- [ ] Agent-Auditor-SDK integration

### Key Measurable Results
| Metric | Target | Measurement |
|--------|--------|-------------|
| **Real Debates** | 10+ debates with live agents | Manual review |
| **Quota Usage** | <10 tokens per debate | Agent-Auditor logs |
| **Rule-Sage Accuracy** | 95%+ correct rule citations | Manual audit |

### Exit Criteria
- [ ] Full 5-agent debate on real query
- [ ] Debates execute within quota budget
- [ ] Rule citations validated

---

## v0.3.0 — User-Facing Features (Target: Mar 14, 2026)

### Deliverables
- [ ] Meta Snapshot API (`/api/meta/snapshot`)
- [ ] List Grader API (`/api/meta/grade`)
- [ ] Upset Detector API (`/api/meta/upsets`)
- [ ] Debate Transcript UI component
- [ ] Stat Check integration

### Key Measurable Results
| Metric | Target | Measurement |
|--------|--------|-------------|
| **API Response Time** | <5 seconds for grade | Performance test |
| **Upset Detection** | Surface 10+ upsets | Query test data |
| **UI Integration** | Viewable in Portal | E2E test |

### Exit Criteria
- [ ] Grade a list via API
- [ ] View debate transcript in Portal
- [ ] Upset detector returns valid results

---

## v1.0.0 — Production Release (Target: Apr 15, 2026)

### Deliverables
- [ ] Tournament prediction tracking
- [ ] Public accuracy dashboard
- [ ] Community feedback integration
- [ ] PyPI publication
- [ ] Agent personality refinement

### Key Measurable Results
| Metric | Target | Measurement |
|--------|--------|-------------|
| **Prediction Accuracy** | 70%+ correct | Tracked predictions |
| **Predictions Tracked** | 50+ predictions | Database count |
| **API Uptime** | 99%+ | Monitoring |
| **User Satisfaction** | 4+ star rating | Feedback survey |

### Exit Criteria
- [ ] 50+ tracked predictions
- [ ] 70%+ accuracy documented
- [ ] No critical bugs for 2 weeks

---

## Key Data Sources

### Internal
- WARScribe Transcripts
- Primordia AI game analysis
- Tournament results (BCP, ITC scraping)

### External
- **Stat Check**: Tournament statistics
- **Goonhammer**: Weekly meta reports
- **Podcasts**: Community meta discussion
- **Warmasters**: Team tournament data
- **WTC Results**: World Team Championship

---

## Council Agents

| Agent | Role | Personality |
|-------|------|-------------|
| 🏠 **Home** | Advocate | Optimistic, finds strengths |
| ⚔️ **Adversary** | Devil's Advocate | Skeptical, finds weaknesses |
| 📊 **Arbiter** | Data Scientist | Neutral, cites statistics |
| 📜 **Rule-Sage** | Rules Lawyer | Precise, validates claims |
| 👑 **Council** | Judge | Synthesizing, final verdict |

---

## Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| Agent-Auditor-SDK | 🔄 Parallel | Quota management |
| WARScribe-Core | 🔄 Parallel | Rule validation |
| DuckDB | ✅ Available | Statistics backend |
| Gemini API | ✅ Available | Agent LLM |

---

## Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| AI hallucinations | Medium | High | Rule-Sage validation |
| Token costs too high | Medium | Medium | Agent-Auditor quota |
| Predictions wrong publicly | Medium | High | Transparent accuracy tracking |

---

## Success Criteria for v1

1. **Accuracy**: 70%+ prediction accuracy tracked publicly
2. **Trust**: Users can view full debate reasoning
3. **Adoption**: 100+ debates run per month
4. **Differentiation**: "Giant killer" lists identified monthly

---

*Maintained by: Vindicta Platform Team*
