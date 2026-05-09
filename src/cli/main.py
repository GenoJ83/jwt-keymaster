import argparse

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="jwt-keymaster", description="JWT tool and keymaster")
    p.add_argument("--version", action="store_true", help="Print version")
    sub = p.add_subparsers(dest="command")
    decode_cmd = sub.add_parser("decode", help="Decode JWT token")
    decode_cmd.add_argument("token", help="Raw JWT string")
    decode_cmd.add_argument("--verify", action="store_true", help="Verify signature")
    gen_cmd = sub.add_parser("generate-secret", help="Generate secure secret")
    gen_cmd.add_argument("--length", type=int, default=32)
    return p

def main(args=None):
    p = build_parser()
    opts = p.parse_args(args)
    if opts.version:
        print("jwt-keymaster v0.1.0")
        return 0
    return 0
