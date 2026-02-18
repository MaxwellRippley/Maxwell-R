#!/usr/bin/env python3
"""
Quick examples demonstrating the math_origins tool
Run this to see how different techniques are explained
"""

from math_origins import MathOriginsDatabase


def show_all_examples():
    """Display all available techniques with brief info"""
    print("\n" + "="*70)
    print("MATHEMATICAL ORIGINS - QUICK EXAMPLES")
    print("="*70 + "\n")
    
    db = MathOriginsDatabase()
    
    print("This tool explains the origin and derivation of mathematical techniques.\n")
    print("Available techniques:\n")
    
    for key in db.list_techniques():
        technique = db.get_technique(key)
        print(f"  {key}")
        print(f"    Category: {technique.category}")
        print(f"    Origin: {technique.origin.split('.')[0]}...")
        print()
    
    print("\nTo see a full derivation, run:")
    print("  python math_origins.py <technique-name>")
    print("\nExample:")
    print("  python math_origins.py u-substitution")
    print()


def show_quick_example():
    """Show a quick example of one technique"""
    print("\n" + "="*70)
    print("EXAMPLE: Pythagorean Theorem")
    print("="*70 + "\n")
    
    db = MathOriginsDatabase()
    pythagoras = db.get_technique('pythagorean-theorem')
    
    print(f"Name: {pythagoras.name}")
    print(f"Category: {pythagoras.category}\n")
    print("First line of origin:")
    print(f"  {pythagoras.origin.split(chr(10))[1]}")
    print("\nNumber of derivation steps:", len(pythagoras.derivation))
    print("Number of applications:", len(pythagoras.applications))
    print("\nTo see the full derivation:")
    print("  python math_origins.py pythagorean-theorem")
    print()


if __name__ == "__main__":
    show_all_examples()
    show_quick_example()
    
    print("="*70)
    print("\nTry these commands:")
    print("  python math_origins.py u-substitution")
    print("  python math_origins.py chain-rule")
    print("  python math_origins.py search calculus")
    print("="*70 + "\n")
