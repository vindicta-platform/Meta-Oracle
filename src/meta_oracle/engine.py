"""
DebateEngine for Meta-Oracle.

Orchestrates debates between the Oracle Council agents.
"""

from typing import Optional

from meta_oracle.protocol import (
    AgentRole,
    Argument,
    ArgumentType,
    DebateRound,
    OracleAgent,
)
from meta_oracle.transcript import AgentVote, DebateTranscript, Prediction


class DebateEngine:
    """
    Orchestrates structured debates between Oracle agents.
    
    Manages turn order, round progression, and consensus building.
    
    Example:
        engine = DebateEngine()
        engine.register_agent(HomeAgent())
        engine.register_agent(AdversaryAgent())
        transcript = await engine.run_debate(context)
    """
    
    def __init__(self, rounds: int = 3) -> None:
        """
        Initialize the debate engine.
        
        Args:
            rounds: Number of debate rounds.
        """
        self.rounds = rounds
        self.agents: dict[AgentRole, OracleAgent] = {}
    
    def register_agent(self, agent: OracleAgent) -> None:
        """
        Register an agent to participate in debates.
        
        Args:
            agent: The agent to register.
        """
        self.agents[agent.role] = agent
    
    async def run_debate(
        self,
        topic: str,
        player1_faction: str,
        player2_faction: str,
        context: Optional[dict] = None
    ) -> DebateTranscript:
        """
        Run a complete debate session.
        
        Args:
            topic: The debate topic (e.g., "Who will win?")
            player1_faction: Player 1's faction.
            player2_faction: Player 2's faction.
            context: Additional context (lists, history, etc.)
            
        Returns:
            Complete debate transcript.
        """
        context = context or {}
        
        transcript = DebateTranscript(
            topic=topic,
            player1_faction=player1_faction,
            player2_faction=player2_faction
        )
        
        # Run debate rounds
        for round_num in range(1, self.rounds + 1):
            round = await self._run_round(round_num, topic, context, transcript)
            transcript.add_round(round)
        
        # Collect votes
        for agent in self.agents.values():
            vote_result = await agent.vote(transcript)
            vote = AgentVote(
                agent_role=agent.role,
                prediction=Prediction(
                    winner=vote_result.get("winner", 1),
                    confidence=vote_result.get("confidence", 0.5),
                    reasoning=vote_result.get("reasoning", ""),
                    upset_detected=vote_result.get("upset", False)
                )
            )
            transcript.add_vote(vote)
        
        # Calculate consensus
        transcript.calculate_consensus()
        
        return transcript
    
    async def _run_round(
        self,
        round_num: int,
        topic: str,
        context: dict,
        transcript: DebateTranscript
    ) -> DebateRound:
        """Run a single debate round."""
        round = DebateRound(round_number=round_num, topic=topic)
        
        # Collect previous arguments for context
        previous_args: list[Argument] = []
        for prev_round in transcript.rounds:
            previous_args.extend(prev_round.arguments)
        
        # Each agent responds in turn
        for role in [AgentRole.HOME, AgentRole.ADVERSARY, 
                     AgentRole.RULE_SAGE, AgentRole.ARBITER, AgentRole.CHAOS]:
            if role in self.agents:
                agent = self.agents[role]
                argument = await agent.respond(previous_args, topic)
                round.add_argument(argument)
                previous_args.append(argument)
        
        return round
