import sys
sys.path.append('../pyAutomataKit')

from pyAutomataKit import DFA

#Test the language A*B
def test_DFA1():
    alphabet = ['a', 'b']
    transitions = {
        1: {'a': 2, 'b': 3},
        2: {'a': 2, 'b': 4},
        3: {'a': 3, 'b': 3},
        4: {'a': 5, 'b': 5},
        5: {'a': 5, 'b': 5}
    }

    dfa = DFA(alphabet, transitions, 1, [4])

    accepted, _ = dfa.execute("ab")
    assert accepted == True, "Should accept 'ab'"

    accepted, _ = dfa.execute("aaaaab")
    assert accepted == True, "Should accept 'aaaaab'"

    accepted, _ = dfa.execute("abb")
    assert accepted == False, "Should not accept 'abb'"

    try:
        accepted, _ = dfa.execute("abc")
        assert False, "Should raise KeyError for symbol not in alphabet"
    except KeyError:
        pass




