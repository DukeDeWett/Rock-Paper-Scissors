import computer

def test_computer_pick():
    options = ["rock", "rock", "rock"]
    computer_pick = computer.pick(options)
    assert computer_pick == "rock"

def test_computer_pick_2():
    options = ["paper", "paper", "paper"]
    computer_pick = computer.pick(options)
    assert computer_pick == "paper"

def test_computer_pick_3():
    options = ["scissors", "scissors", "scissors"]
    computer_pick = computer.pick(options)
    assert computer_pick == "scissors"