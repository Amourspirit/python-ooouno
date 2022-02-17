#!/usr/bin/env python
import argparse
from config import AppConfig, read_config
from cmd.build_lo_test import builder

def _create_parser(name: str) -> argparse.ArgumentParser:
    return argparse.ArgumentParser(description=name)

def _args_test(parser: argparse.ArgumentParser, config: AppConfig) -> None:
    parser.add_argument(
        '-w', '--write-test',
        help=f"Writes stickytape version of lo_test.py into tmp dir",
        action='store_true',
        dest='stick_write',
        default=False
    )

def _args_action_test(args: argparse.Namespace, config: AppConfig) -> None:
    if not args.stick_write:
        return
    build = builder(config=config)
    build.build()
    

def _args_process_cmd(args: argparse.Namespace, config: AppConfig) -> None:
    if args.command == 'test':
        _args_action_test(args=args, config=config)

def main():
    global logger
    # region Config
    config = read_config('./config.json')
    parser = _create_parser('main')
    subparser = parser.add_subparsers(dest='command')
    
    test_parser = subparser.add_parser(
        name='test', help=f"Build lo_test.py into tmp dir using stickytape.")
    _args_test(parser=test_parser, config=config)

    args = parser.parse_args()

    _args_process_cmd(args=args, config=config)

if __name__ == '__main__':
    main()