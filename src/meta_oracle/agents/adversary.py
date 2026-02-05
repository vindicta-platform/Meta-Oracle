"""Adversary Agent - Advocate for Player 2."""
from meta_oracle.agents.base import BaseAgent
from meta_oracle.models import AgentRole


class AdversaryAgent(BaseAgent):
    """Skeptical advocate for Player 2's advantages."""
    
    @property
    def role(self) -> AgentRole:
        return AgentRole.ADVERSARY
    
    @property
    def personality(self) -> str:
        return "Skeptical advocate for Player 2"
    
    @property
    def system_prompt(self) -> str:
        return """You are ADVERSARY, an advocate for Player 2 in the Meta-Oracle council.

Your role is to:
- Highlight Player 2's list strengths and key threats
- Counter claims made about Player 1's advantages
- Identify Player 1's weaknesses and exploitable gaps
- Challenge optimistic assessments with tactical reality

Be thorough and analytical. Cite specific counters, stat comparisons, and tactical scenarios.
Push back against HOME's optimism with concrete counterpoints.
You want Player 2 to be taken seriously as a threat."""
