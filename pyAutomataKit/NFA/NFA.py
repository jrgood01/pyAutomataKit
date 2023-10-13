class NFA:
    def __init__(self, alphabet, transitions, start_state, accepting_states):
        self.current_states = []
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accepting_states = accepting_states
        self.history = []
        
        assert len(self.states) > 0, "DFA must have at least one state"
        assert start_state in self.states, "Start state must be in the set of states"
        assert len(accepting_states) > 0, "DFA must have at least one accepting state"
        assert len(accepting_states) <= len(self.states), "DFA cannot have more accepting states than total states"
        assert all(state in self.states for state in accepting_states), "All accepting states must be in the set of states"

        for state in self.states:
            assert all(symbol in self.alphabet for symbol in self.transitions[state].keys()), "All symbols must be in the alphabet"          

    def reset(self):
        self.current_states = []
        self.history = []

    def in_accepting_state(self):
        return any(state in self.accepting_states for state in self.current_states)
    
    def transition(self, symbol):
        next_states = []
        for state in self.current_states:
            if symbol in self.transitions[state]:
                next_states += self.transitions[state][symbol]
            if None in self.transitions[state]:
                next_states += self.transitions[state][None]
        return next_states

    def execute(self, inStr):
        assert len(inStr) > 0, "input string can not be empty"
        self.reset()
        self.history = [{'current_states': self.start_state, 'next_symbol': inStr[0]}]
        for i in range(0, len(str)):
            symbol = inStr[i]
            self.current_states = self.transition(symbol)
            self.history.append({'current_states': self.current_states, 'next_symbol': inStr[i + 1] if i < len(inStr) - 1 else 'None'})
        return self.in_accepting_state(), self.history
