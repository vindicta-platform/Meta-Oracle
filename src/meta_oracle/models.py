"""Meta-Oracle data models for the 5-agent debate council."""
from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class AgentRole(str, Enum):
    """The five council agent roles."""
    HOME = "home"           # Advocate for Player 1
    ADVERSARY = "adversary" # Advocate for Player 2
    ARBITER = "arbiter"     # Data-driven referee
    RULE_SAGE = "rule_sage" # Rules validator
    CHAOS = "chaos"         # Upset detector / devil's advocate


class ArgumentType(str, Enum):
    """Types of arguments agents can make during debate."""
    CLAIM = "claim"
    EVIDENCE = "evidence"
    REBUTTAL = "rebuttal"
    CONCESSION = "concession"
    QUESTION = "question"


class Argument(BaseModel):
    """A single argument made by an agent during debate."""
    id: UUID = Field(default_factory=uuid4)
    agent_role: AgentRole
    round: int
    argument_type: ArgumentType
    content: str
    in_response_to: UUID | None = None
    confidence: float = 0.5
    timestamp: datetime = Field(default_factory=datetime.now)


class Vote(BaseModel):
    """Final prediction vote from an agent."""
    agent_role: AgentRole
    prediction: str        # e.g., "Player 1 wins", "Player 2 wins", "Draw"
    win_probability: float # 0.0 to 1.0
    confidence: float      # How confident in this vote
    reasoning: str


class DebateContext(BaseModel):
    """Context for a debate matchup."""
    player1_faction: str
    player1_list: str
    player2_faction: str
    player2_list: str
    mission: str | None = None
    terrain: str | None = None
    additional_context: str | None = None


class DebateTranscript(BaseModel):
    """Full transcript of a council debate session."""
    id: UUID = Field(default_factory=uuid4)
    context: DebateContext
    rounds: list[list[Argument]] = Field(default_factory=list)
    votes: list[Vote] = Field(default_factory=list)
    consensus: str | None = None
    consensus_confidence: float = 0.0
    created_at: datetime = Field(default_factory=datetime.now)
