"""
Meta-Oracle: 5-agent AI Council for meta predictions.

Implements adversarial reasoning through structured debates
between specialized AI agents.
"""

from meta_oracle.protocol import OracleAgent, AgentRole, DebateRound
from meta_oracle.engine import DebateEngine
from meta_oracle.transcript import DebateTranscript

__version__ = "0.1.0"

__all__ = [
    "AgentRole",
    "DebateEngine",
    "DebateRound",
    "DebateTranscript",
    "OracleAgent",
]
