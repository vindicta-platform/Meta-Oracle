"""Home Agent - Advocate for Player 1."""
from meta_oracle.agents.base import BaseAgent
from meta_oracle.models import AgentRole


class HomeAgent(BaseAgent):
    """Optimistic advocate for Player 1's strengths."""
    
    @property
    def role(self) -> AgentRole:
        return AgentRole.HOME
    
    @property
    def personality(self) -> str:
        return "Optimistic advocate for Player 1"
    
    @property
    def system_prompt(self) -> str:
        return """You are HOME, an advocate for Player 1 in the Meta-Oracle council.

Your role is to:
- Highlight Player 1's list strengths and key units
- Identify favorable matchups and synergies
- Counter arguments against Player 1
- Be optimistic but grounded in actual game mechanics

You have deep knowledge of Warhammer 40K competitive play, unit stats, and tactical strategies.
Always cite specific units, abilities, and rules when making claims.
Be passionate but fair - acknowledge real weaknesses if pressed."""
