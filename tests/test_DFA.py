from pyAutomataKit import DFA
def test_dfa():
    # Test DFA 1
    alphabet1 = ['0', '1']
    transitions1 = {
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q1'},
        'q2': {'0': 'q0', '1': 'q1'}
    }
    start_state1 = 'q0'
    accepting_states1 = ['q1']
    dfa1 = DFA(alphabet1, transitions1, start_state1, accepting_states1)

    # Test reset method for DFA 1
    dfa1.current_state = 'q1'
    dfa1.execution_history = [{'state': 'q0', 'next_symbol': '0'}]
    dfa1.reset()
    assert dfa1.current_state == start_state1
    assert dfa1.execution_history == []

    # Test in_accepting_state method for DFA 1
    assert not dfa1.in_accepting_state()
    dfa1.current_state = 'q1'
    assert dfa1.in_accepting_state()

    # Test transition method for DFA 1
    assert dfa1.transition('0') == 'q0'
    assert dfa1.transition('1') == 'q1'

    # Test execute method for DFA 1
    assert dfa1.execute('0101') == (True, [
        {'state': 'q0', 'next_symbol': '1'},
        {'state': 'q1', 'next_symbol': '0'},
        {'state': 'q2', 'next_symbol': '1'},
        {'state': 'q1', 'next_symbol': 'None'}
    ])

    # Test DFA 2
    alphabet2 = ['a', 'b', 'c']
    transitions2 = {
        'q0': {'a': 'q1', 'b': 'q2', 'c': 'q3'},
        'q1': {'a': 'q1', 'b': 'q2', 'c': 'q3'},
        'q2': {'a': 'q1', 'b': 'q2', 'c': 'q3'},
        'q3': {'a': 'q1', 'b': 'q2', 'c': 'q3'}
    }
    start_state2 = 'q0'
    accepting_states2 = ['q1', 'q2', 'q3']
    dfa2 = DFA(alphabet2, transitions2, start_state2, accepting_states2)

    # Test reset method for DFA 2
    dfa2.current_state = 'q2'
    dfa2.execution_history = [{'state': 'q0', 'next_symbol': 'a'}]
    dfa2.reset()
    assert dfa2.current_state == start_state2
    assert dfa2.execution_history == []

    # Test in_accepting_state method for DFA 2
    assert not dfa2.in_accepting_state()
    dfa2.current_state = 'q1'
    assert dfa2.in_accepting_state()
    dfa2.current_state = 'q2'
    assert dfa2.in_accepting_state()
    dfa2.current_state = 'q3'
    assert dfa2.in_accepting_state()

    # Test transition method for DFA 2
    assert dfa2.transition('a') == 'q1'
    assert dfa2.transition('b') == 'q2'
    assert dfa2.transition('c') == 'q3'

    # Test execute method for DFA 2
    assert dfa2.execute('abcabc') == (True, [
        {'state': 'q1', 'next_symbol': 'b'},
        {'state': 'q2', 'next_symbol': 'c'},
        {'state': 'q3', 'next_symbol': 'a'},
        {'state': 'q1', 'next_symbol': 'b'},
        {'state': 'q2', 'next_symbol': 'c'},
        {'state': 'q3', 'next_symbol': 'None'}
    ])

    # Test DFA 3 (edge case with empty alphabet and no accepting states)
    alphabet3 = []
    transitions3 = {
        'q0': {}
    }
    start_state3 = 'q0'
    accepting_states3 = []
    dfa3 = DFA(alphabet3, transitions3, start_state3, accepting_states3)

    # Test reset method for DFA 3
    dfa3.current_state = 'q0'
    dfa3.execution_history = [{'state': 'q0', 'next_symbol': 'None'}]
    dfa3.reset()
    assert dfa3.current_state == start_state3
    assert dfa3.execution_history == []

    # Test in_accepting_state method for DFA 3
    assert not dfa3.in_accepting_state()

    # Test transition method for DFA 3
    assert dfa3.transition('None') == []

    # Test execute method for DFA 3
    assert dfa3.execute('') == (True, [
        {'state': 'q0', 'next_symbol': 'None'}
    ])