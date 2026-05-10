from src.cli.main import build_parser, main

def test_cli():
    p = build_parser()
    opts = p.parse_args(["decode", "a.b.c", "--verify"])
    assert opts.command == "decode"
    assert opts.token == "a.b.c"
    assert opts.verify is True
    assert main(["--version"]) == 0
