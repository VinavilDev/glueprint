#!/usr/bin/env python3
import argparse
import sys

from .core import GluePrint
from .utils.output import print_banner, print_results, print_error, print_success, Colors


def main():
    parser = argparse.ArgumentParser(
        prog="glueprint",
        description="GluePrint - Web Technology Fingerprinter"
    )
    
    parser.add_argument("--url", "-u", required=True, help="Target URL")
    parser.add_argument("--deep", "-d", action="store_true", help="Deep scan")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show evidence")
    parser.add_argument("--json", "-j", action="store_true", help="JSON output")
    parser.add_argument("--output", "-o", help="Save to file")
    parser.add_argument("--timeout", "-t", type=int, default=10)
    parser.add_argument("--no-verify", action="store_true", help="Skip SSL verification")
    parser.add_argument("--header", "-H", action="append", help='Header: "Name: Value"')
    parser.add_argument("--cookie", "-c", action="append", help='Cookie: "name=value"')
    parser.add_argument("--user-agent", help="Custom User-Agent")
    
    args = parser.parse_args()

    # Parse custom headers
    headers = {}
    if args.header:
        for h in args.header:
            if ':' in h:
                key, value = h.split(':', 1)
                headers[key.strip()] = value.strip()

    # Parse cookies
    cookies = {}
    if args.cookie:
        for c in args.cookie:
            if '=' in c:
                key, value = c.split('=', 1)
                cookies[key.strip()] = value.strip()

    # Print banner unless JSON output
    if not args.json:
        print_banner()

    try:
        scanner = GluePrint(
            url=args.url,
            timeout=args.timeout,
            verify_ssl=not args.no_verify,
            user_agent=args.user_agent,
            headers=headers,
            cookies=cookies
        )
        
        result = scanner.scan(deep=args.deep)

        if args.json:
            print(scanner.to_json())
        else:
            print_results(result, verbose=args.verbose)

        if args.output:
            with open(args.output, 'w') as f:
                f.write(scanner.to_json())
            
            if not args.json:
                print_success(f"Saved to {args.output}")

    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Interrupted{Colors.RESET}")
        sys.exit(1)
    except Exception as e:
        print_error(str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
