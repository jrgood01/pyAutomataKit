import sys

class DFA:
    def __init__(self, alphabet, transitions, start_state, accepting_states):
        self.states = list(transitions.keys())

        assert len(self.states) > 0, "DFA must have at least one state"
        assert start_state in self.states, "Start state must be in the set of states"
        assert len(accepting_states) > 0, "DFA must have at least one accepting state"
        assert len(accepting_states) <= len(self.states), "DFA cannot have more accepting states than total states"
        assert all(state in self.states for state in accepting_states), "All accepting states must be in the set of states"

        for state in self.states:
            assert len(transitions[state]) == len(alphabet), "Each state must have a transition for each symbol in the alphabet"
            assert all(symbol in alphabet for symbol in transitions[state]), "All symbols in transitions must be in the alphabet"
            assert all(next_state in self.states for next_state in transitions[state].values()), "All next states in transitions must be in the set of states"
        
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accepting_states = accepting_states
        self.current_state = start_state
        self.execution_history = []
    
    def __str__(self):
        summary_str =  "DFA Summary N=(Q, ∑, δ, q0, F)):\n\t Q="

        for state in self.states:
            summary_str += " " + state
            if state != self.states[-1]:
                summary_str += ","

        summary_str += "\n\t ∑="
        for symbol in self.alphabet:
            summary_str += " " + symbol
            if symbol != self.alphabet[-1]:
                summary_str += ","
        
        summary_str += "\n\t δ="
        for state in self.states:
            summary_str += "\n\t\t" + state + ":"
            for symbol in self.alphabet:
                summary_str += " " + self.transitions[state][symbol]
                if symbol != self.alphabet[-1]:
                    summary_str += ","

        summary_str += "\n\t q0=" + self.start_state
        summary_str += "\n\t F="
        for state in self.accepting_states:
            summary_str += " " + state
            if state != self.accepting_states[-1]:
                summary_str += ","

        return summary_str
            
    def reset(self):
        self.current_state = self.start_state
        self.execution_history = []

    def in_accepting_state(self):
        return self.current_state in self.accepting_states
    
    def transition(self, symbol):
        self.current_state = self.transitions[self.current_state][symbol]
        return self.current_state

    def execute(self, inStr):
        self.reset()
        self.execution_history.append({'state': self.current_state, 'next_symbol':inStr[0]})
        for i in range(0, len(inStr)):
            self.execution_history.append({'state': self.transition(inStr[i]), 'next_symbol':inStr[i+1] if i+1 < len(inStr) else None})
        return (self.in_accepting_state(), self.execution_history)