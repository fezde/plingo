from plingo import Plingo


def test_method_names_match_command_id():
    lingo = Plingo()

    for idx, cmd in enumerate(lingo._command_names):
        parts = cmd.split("_")
        print(parts)
        assert idx == int(parts[2])
