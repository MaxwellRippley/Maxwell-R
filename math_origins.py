"""
Mathematical Origins and Derivations
A tool to understand the origin and derivation of mathematical techniques
"""

from typing import Dict, List
import re


class MathDerivation:
    """Represents a mathematical concept with its derivation and origin"""
    
    def __init__(self, name: str, category: str, origin: str, 
                 derivation: List[str], applications: List[str]):
        self.name = name
        self.category = category
        self.origin = origin
        self.derivation = derivation
        self.applications = applications
    
    def display(self):
        """Display the full derivation and origin"""
        print(f"\n{'='*70}")
        print(f"TECHNIQUE: {self.name}")
        print(f"Category: {self.category}")
        print(f"{'='*70}\n")
        
        print(f"ORIGIN & HISTORY:")
        print(f"{self.origin}\n")
        
        print(f"DERIVATION:")
        for i, step in enumerate(self.derivation, 1):
            print(f"\nStep {i}:")
            print(f"{step}")
        
        print(f"\n\nAPPLICATIONS:")
        for app in self.applications:
            print(f"  • {app}")
        
        print(f"\n{'='*70}\n")


class MathOriginsDatabase:
    """Database of mathematical techniques and their derivations"""
    
    def __init__(self):
        self.techniques = self._load_techniques()
    
    def _load_techniques(self) -> Dict[str, MathDerivation]:
        """Load all mathematical techniques and derivations"""
        
        techniques = {}
        
        # U-Substitution (Integration by Substitution)
        techniques['u-substitution'] = MathDerivation(
            name="U-Substitution (Integration by Substitution)",
            category="Calculus - Integration",
            origin="""
U-substitution was developed as the reverse process of the chain rule for 
derivatives. It emerged in the late 17th century alongside the development of 
calculus by Newton and Leibniz. Leibniz's notation dx made the technique more 
intuitive, as it allows us to treat differentials algebraically.

The technique is fundamentally based on the chain rule: if we know that
d/dx[F(g(x))] = F'(g(x)) · g'(x), then working backwards, we can integrate
F'(g(x)) · g'(x) by recognizing this pattern.
            """,
            derivation=[
                """Starting Point - The Chain Rule:
If F is an antiderivative of f, then by the chain rule:
    d/dx[F(g(x))] = F'(g(x)) · g'(x) = f(g(x)) · g'(x)
                """,
                """Reversing the Chain Rule (Integration):
Taking the integral of both sides:
    ∫ f(g(x)) · g'(x) dx = F(g(x)) + C
    
This is the fundamental theorem that u-substitution exploits.
                """,
                """Making the Substitution:
Let u = g(x), then:
    du/dx = g'(x)
    du = g'(x) dx
    
Now substitute into the integral:
    ∫ f(g(x)) · g'(x) dx = ∫ f(u) du
                """,
                """Simplification:
The integral in terms of u is often simpler:
    ∫ f(u) du = F(u) + C
    
Then substitute back: F(u) + C = F(g(x)) + C
                """,
                """Why it Works - The Intuition:
We're essentially "undoing" a composite function by recognizing that the 
integrand contains both a function and its derivative. The substitution 
transforms a complicated integral into a simpler one by changing variables.
                """,
            ],
            applications=[
                "∫ 2x·cos(x²) dx  [Let u = x², du = 2x dx]",
                "∫ e^(3x) dx  [Let u = 3x, du = 3 dx]",
                "∫ (2x+1)/(x²+x) dx  [Let u = x²+x, du = (2x+1) dx]",
                "Any integral of the form ∫ f(g(x))·g'(x) dx"
            ]
        )
        
        # Chain Rule
        techniques['chain-rule'] = MathDerivation(
            name="Chain Rule",
            category="Calculus - Differentiation",
            origin="""
The chain rule was first stated by Leibniz in 1676, though implicit uses appear 
earlier. It's one of the fundamental rules of calculus, allowing us to 
differentiate composite functions.

The rule emerges from the fundamental question: "What is the rate of change of 
a composition of functions?" If y changes with respect to u, and u changes with 
respect to x, how does y change with respect to x?
            """,
            derivation=[
                """Intuitive Foundation:
Suppose y = f(u) and u = g(x), so y = f(g(x)).
We want to find dy/dx (how y changes as x changes).
                """,
                """The Rate of Change Composition:
Think of it as a chain of changes:
- When x changes by Δx, u changes by Δu
- When u changes by Δu, y changes by Δy

The rates multiply:
    Δy/Δx = (Δy/Δu) · (Δu/Δx)
                """,
                """Taking the Limit:
As Δx → 0:
    dy/dx = lim(Δx→0) Δy/Δx
          = lim(Δx→0) [(Δy/Δu) · (Δu/Δx)]
          = [lim(Δu→0) Δy/Δu] · [lim(Δx→0) Δu/Δx]
          = (dy/du) · (du/dx)
                """,
                """The Chain Rule Formula:
If y = f(u) and u = g(x), then:
    dy/dx = dy/du · du/dx
    
Or in function notation:
    d/dx[f(g(x))] = f'(g(x)) · g'(x)
                """,
                """Why it Works - The Intuition:
The chain rule says that the rate of change of a composition is the product 
of the rates of change. This makes intuitive sense: if u changes twice as 
fast as x, and y changes three times as fast as u, then y changes 
2 × 3 = 6 times as fast as x.
                """,
            ],
            applications=[
                "d/dx[sin(x²)] = cos(x²) · 2x",
                "d/dx[(3x+1)⁵] = 5(3x+1)⁴ · 3",
                "d/dx[e^(x²)] = e^(x²) · 2x",
                "Used whenever differentiating composite functions"
            ]
        )
        
        # Integration by Parts
        techniques['integration-by-parts'] = MathDerivation(
            name="Integration by Parts",
            category="Calculus - Integration",
            origin="""
Integration by parts was developed as the reverse of the product rule for 
derivatives. Like u-substitution reverses the chain rule, integration by parts 
reverses the product rule. It was formalized in the 17th century as calculus 
developed.

The technique is essential for integrating products of functions where neither 
function is the derivative of the other.
            """,
            derivation=[
                """Starting with the Product Rule:
For two functions u(x) and v(x):
    d/dx[u·v] = u·(dv/dx) + v·(du/dx)
                """,
                """Integrating Both Sides:
    ∫ d/dx[u·v] dx = ∫ [u·(dv/dx) + v·(du/dx)] dx
    
    u·v = ∫ u·(dv/dx) dx + ∫ v·(du/dx) dx
                """,
                """Rearranging:
    ∫ u·(dv/dx) dx = u·v - ∫ v·(du/dx) dx
                """,
                """Using Differential Notation:
Let dv = v'(x)dx and du = u'(x)dx:
    ∫ u dv = uv - ∫ v du
    
This is the integration by parts formula.
                """,
                """Why it Works - The Intuition:
We're essentially reversing the product rule. When we can't integrate a 
product directly, we transform it into a different integral that might be 
easier by "trading" one part of the product for another through differentiation 
and integration.
                """,
            ],
            applications=[
                "∫ x·e^x dx  [u=x, dv=e^x dx]",
                "∫ x·cos(x) dx  [u=x, dv=cos(x) dx]",
                "∫ ln(x) dx  [u=ln(x), dv=dx]",
                "∫ x²·sin(x) dx  [may need to apply twice]"
            ]
        )
        
        # Pythagorean Theorem
        techniques['pythagorean-theorem'] = MathDerivation(
            name="Pythagorean Theorem",
            category="Geometry",
            origin="""
The Pythagorean theorem is one of the oldest known mathematical results, dating 
back to ancient Babylonian and Indian mathematics (around 2000-1500 BCE). While 
named after Pythagoras (c. 570-495 BCE), he likely provided one of the first 
rigorous proofs rather than discovering the relationship itself.

The theorem states that in a right triangle with legs a and b and hypotenuse c:
    a² + b² = c²
            """,
            derivation=[
                """Geometric Proof by Rearrangement:
Consider a square with side length (a+b), which has area (a+b)².
                """,
                """Divide the square in two ways:

METHOD 1: The square contains:
- A smaller square of side c (the hypotenuse) with area c²
- Four right triangles, each with area (1/2)ab
Total area: c² + 4·(1/2)ab = c² + 2ab
                """,
                """METHOD 2: The large square has area:
    (a+b)² = a² + 2ab + b²
                """,
                """Since both expressions equal the same area:
    c² + 2ab = a² + 2ab + b²
    
Subtracting 2ab from both sides:
    c² = a² + b²
                """,
                """Why it Works - The Intuition:
The theorem relates the areas of squares built on the sides of a right 
triangle. The square on the hypotenuse has the same area as the sum of the 
squares on the other two sides. This is a fundamental relationship in 
Euclidean geometry.
                """,
            ],
            applications=[
                "Finding the distance between two points in a coordinate plane",
                "Calculating diagonal distances in rectangular spaces",
                "Basis for trigonometric identities (sin²θ + cos²θ = 1)",
                "Foundation for the distance formula and dot products in linear algebra"
            ]
        )
        
        # Quadratic Formula
        techniques['quadratic-formula'] = MathDerivation(
            name="Quadratic Formula",
            category="Algebra",
            origin="""
The quadratic formula has ancient origins. Babylonian mathematicians (around 
2000 BCE) could solve quadratic equations, though without modern symbolic 
notation. The general formula as we know it was developed through contributions 
from Indian, Islamic, and European mathematicians over many centuries.

The formula solves ax² + bx + c = 0:
    x = (-b ± √(b²-4ac)) / (2a)
            """,
            derivation=[
                """Starting with the general quadratic equation:
    ax² + bx + c = 0  (where a ≠ 0)
                """,
                """Divide by a to normalize:
    x² + (b/a)x + (c/a) = 0
                """,
                """Move the constant term to the right:
    x² + (b/a)x = -(c/a)
                """,
                """Complete the square on the left side:
Add (b/2a)² to both sides:
    x² + (b/a)x + (b/2a)² = -(c/a) + (b/2a)²
    
    [x + (b/2a)]² = -(c/a) + b²/(4a²)
                """,
                """Simplify the right side:
    [x + (b/2a)]² = (b² - 4ac)/(4a²)
                """,
                """Take the square root of both sides:
    x + (b/2a) = ± √(b² - 4ac)/(2a)
                """,
                """Solve for x:
    x = -(b/2a) ± √(b² - 4ac)/(2a)
    
    x = [-b ± √(b² - 4ac)] / (2a)
                """,
                """Why it Works - The Intuition:
The technique of "completing the square" transforms the quadratic into a 
perfect square that can be easily solved. The discriminant (b²-4ac) determines 
whether solutions are real (≥0) or complex (<0).
                """,
            ],
            applications=[
                "Solving any quadratic equation ax² + bx + c = 0",
                "Finding zeros of parabolas",
                "Analyzing projectile motion in physics",
                "Optimizing quadratic functions in economics and engineering"
            ]
        )
        
        return techniques
    
    def get_technique(self, name: str) -> MathDerivation:
        """Get a specific technique by name"""
        normalized = name.lower().strip()
        return self.techniques.get(normalized)
    
    def list_techniques(self) -> List[str]:
        """List all available techniques"""
        return sorted(self.techniques.keys())
    
    def search(self, query: str) -> List[str]:
        """Search for techniques by keyword"""
        query = query.lower()
        results = []
        
        for key, technique in self.techniques.items():
            if (query in key.lower() or 
                query in technique.name.lower() or 
                query in technique.category.lower()):
                results.append(key)
        
        return results


def main():
    """Main entry point for the application"""
    import sys
    
    db = MathOriginsDatabase()
    
    if len(sys.argv) < 2:
        print("Mathematical Origins and Derivations")
        print("=" * 70)
        print("\nUsage: python math_origins.py <technique-name>")
        print("       python math_origins.py list")
        print("       python math_origins.py search <keyword>")
        print("\nAvailable techniques:")
        for technique in db.list_techniques():
            tech = db.get_technique(technique)
            print(f"  • {technique:30} [{tech.category}]")
        print("\nExample: python math_origins.py u-substitution")
        return
    
    command = sys.argv[1].lower()
    
    if command == "list":
        print("\nAvailable Mathematical Techniques:\n")
        for technique in db.list_techniques():
            tech = db.get_technique(technique)
            print(f"  • {technique:30} [{tech.category}]")
    
    elif command == "search":
        if len(sys.argv) < 3:
            print("Usage: python math_origins.py search <keyword>")
            return
        
        query = sys.argv[2]
        results = db.search(query)
        
        if results:
            print(f"\nSearch results for '{query}':\n")
            for result in results:
                tech = db.get_technique(result)
                print(f"  • {result:30} [{tech.category}]")
        else:
            print(f"\nNo techniques found matching '{query}'")
    
    else:
        technique = db.get_technique(command)
        if technique:
            technique.display()
        else:
            print(f"\nTechnique '{command}' not found.")
            print("Use 'python math_origins.py list' to see available techniques.")


if __name__ == "__main__":
    main()
