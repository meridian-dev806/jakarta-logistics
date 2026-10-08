#!/usr/bin/env python3
"""Parse simple route exports."""
import sys
for line in sys.stdin:
    parts = [p.strip() for p in line.split(",")]
    if len(parts) >= 3:
        print(f"{parts[0]} -> {parts[1]}: {parts[2]} days")
