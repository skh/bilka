#!/usr/bin/env python3
import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(
        prog="bilka",
        description="Scrape news articles from supported sites within an optional date range."
    )
    
    # Required: news site
    parser.add_argument(
        "site",
        type=str,
        help="The identifier for the news site (e.g. 'bbc', 'cnn', 'nyt')"
    )
    
    # Optional: start and end dates
    parser.add_argument(
        "--start",
        type=str,
        help="Start date in YYYY-MM-DD format. If only start is given, range is start → now."
    )
    parser.add_argument(
        "--end",
        type=str,
        help="End date in YYYY-MM-DD format (optional)."
    )

    args = parser.parse_args()

    # Handle dates
    start_date = None
    end_date = None
    if args.start:
        start_date = datetime.strptime(args.start, "%Y-%m-%d").date()
    if args.end:
        end_date = datetime.strptime(args.end, "%Y-%m-%d").date()
    elif args.start:  # if only start given, use today as end
        end_date = datetime.now().date()

    # --- Call your scraping functionality here ---
    print(f"Scraping site: {args.site}")
    if start_date and end_date:
        print(f"Date range: {start_date} → {end_date}")
    else:
        print("No date range specified (scraping latest articles only).")

    # Example call to your existing scraper function:
    # scrape_site(args.site, start_date=start_date, end_date=end_date)


if __name__ == "__main__":
    main()