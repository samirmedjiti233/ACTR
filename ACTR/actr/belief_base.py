# actr/belief_base.py
from typing import Set, List
from actr.conditional import Conditional


class BeliefBase:
    """
    Eine Belief Base ist eine Sammlung von Conditionals (Regeln).
    Sie unterstützt das Hinzufügen, Iterieren und Abfragen von Atomen.
    """

    def __init__(self):
        # interne Liste für alle Conditionals
        self.rules: List[Conditional] = []

    def add(self, rule: Conditional) -> None:
        """Fügt eine neue Regel zur Belief Base hinzu."""
        self.rules.append(rule)

    def atoms(self) -> Set[str]:
        """Gibt die Menge aller Atome zurück, die in den Regeln vorkommen."""
        all_atoms: Set[str] = set()
        for r in self.rules:
            all_atoms |= r.atoms()
        return all_atoms

    def __len__(self) -> int:
        """Erlaubt len(base), um Anzahl der Regeln zu bekommen."""
        return len(self.rules)

    def __iter__(self):
        """Erlaubt for-Schleifen über die Base."""
        return iter(self.rules)

    def __str__(self) -> str:
        """Schöne Ausgabe aller Regeln untereinander."""
        return "\n".join(str(r) for r in self.rules)


# Kleiner Selbsttest
if __name__ == "__main__":
    base = BeliefBase()
    base.add(Conditional("b"
