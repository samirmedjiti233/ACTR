# actr/conditional.py
from dataclasses import dataclass
from typing import Set
import re

@dataclass
class Conditional:
    """
    Repräsentiert ein Conditional (B | A) mit:
      - antecedent: A (z. B. "p & b" oder "b")
      - consequent: B (z. B. "f")
    Die Klasse ist bewusst einfach gehalten; atoms() extrahiert die verwendeten Atom-Namen.
    """
    antecedent: str
    consequent: str

    def __str__(self) -> str:
        # menschenlesbare Darstellung: "(B|A)"
        return f"({self.consequent}|{self.antecedent})"

    def atoms(self) -> Set[str]:
        """
        Liefert die Menge der Atome, die in antecedent oder consequent vorkommen.
        Aktuelle Implementation: findet Wortgruppen (alphanumerisch + _).
        Beispiele:
          "p & b" -> {"p","b"}
          "a or (b & c)" -> {"a","b","c"}
        """
        def parse_atoms(formula: str) -> Set[str]:
            if not formula:
                return set()
            # finde alle "Wörter" (Buchstaben/Zahlen/Unterstrich)
            found = re.findall(r'\w+', formula)
            return {f.lower() for f in found if f.strip() != ""}

        at = parse_atoms(self.antecedent) | parse_atoms(self.consequent)
        return at


# Kleiner Selbsttest, wenn die Datei direkt ausgeführt wird:
if __name__ == "__main__":
    c1 = Conditional("b", "f")
    print(c1)               # Ausgabe: (f|b)
    print(c1.atoms())       # Ausgabe: {'b','f'}

    c2 = Conditional("p & b", "f")
    print(c2)               # Ausgabe: (f|p & b)
    print(c2.atoms())       # Ausgabe: {'p','b','f'}
