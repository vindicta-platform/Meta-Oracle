"""Oracle Agent protocol - interface for all council agents."""
from typing import Protocol

from meta_oracle.models import Argument, DebateContext, DebateTranscript, Vote


class OracleAgent(Protocol):
    """Interface that all council agents must implement."""
    
    @property
    def role(self) -> str:
        """The agent's role identifier."""
        ...
    
    @property
    def personality(self) -> str:
        """Description of the agent's debate style."""
        ...
    
    def analyze(self, context: DebateContext) -> str:
        """Perform initial analysis of the matchup."""
        ...
    
    def respond(self, transcript: DebateTranscript, round_num: int) -> Argument:
        """Generate a response based on debate history."""
        ...
    
    def vote(self, transcript: DebateTranscript) -> Vote:
        """Cast final prediction vote after debate concludes."""
        ...
