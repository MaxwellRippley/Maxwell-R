"""
Test script for math_origins.py
"""

from math_origins import MathOriginsDatabase, MathDerivation


def test_database():
    """Test the database functionality"""
    print("Testing MathOriginsDatabase...")
    
    db = MathOriginsDatabase()
    
    # Test listing techniques
    techniques = db.list_techniques()
    print(f"✓ Found {len(techniques)} techniques")
    
    # Test getting a specific technique
    u_sub = db.get_technique('u-substitution')
    assert u_sub is not None, "U-substitution should exist"
    assert u_sub.name == "U-Substitution (Integration by Substitution)"
    print("✓ Successfully retrieved u-substitution")
    
    # Test search functionality
    calc_results = db.search('calculus')
    assert len(calc_results) > 0, "Should find calculus-related techniques"
    print(f"✓ Search for 'calculus' found {len(calc_results)} results")
    
    # Test integration techniques
    integration_results = db.search('integration')
    print(f"✓ Search for 'integration' found {len(integration_results)} results")
    
    print("\nAll tests passed! ✓")


def demo_display():
    """Demonstrate the display functionality"""
    print("\n" + "="*70)
    print("DEMONSTRATION: Displaying U-Substitution Derivation")
    print("="*70)
    
    db = MathOriginsDatabase()
    u_sub = db.get_technique('u-substitution')
    u_sub.display()


if __name__ == "__main__":
    test_database()
    demo_display()
