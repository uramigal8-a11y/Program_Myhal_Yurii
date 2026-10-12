class Employee:
    """Базовий клас працівника компанії"""

    raise_rate = 0.05
    def __init__(self, name: str, base: float) -> None:
        self.name = name
        self.base = float(base)

    def salary(self) -> float:
        return self.base

    def give_raise(self) -> None:
        self.base = self.base * (1 + self.raise_rate)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}')"

class Developer(Employee):
    """Клас розробника з фіксованими надбавками за рівнем кваліфікації"""

    raise_rate = 0.1
    all_levels = {"junior": 0.0, "middle": 5000.0, "senior": 15000.0}
    def __init__(self, name: str, base: float, level: str) -> None:
        super().__init__(name, base)
        self.level = level

    def salary(self) -> float:
        return super().salary() + self.all_levels.get(self.level, 0.0)

class Manager(Employee):
    """Клас менеджера, чий оклад залежить від кількості підлеглих у команді"""

    def __init__(self, name: str, base: float, team: list | None = None) -> None:
        super().__init__(name, base)
        self.team = list(team) if team is not None else []

    def salary(self) -> float:
        return super().salary() + (1000.0 * len(self.team))

class Department:
    """Клас відділу, що містить список працівників"""

    def __init__(self, name: str, *employees: Employee) -> None:
        self.name = name
        self.employees = list(employees)

    def payroll(self) -> float:
        return sum(emp.salary() for emp in self.employees if isinstance(emp, Employee))

    def top(self) -> Employee | None:
        if not self.employees:
            return None

        return max(self.employees, key=lambda emp: emp.salary())

if __name__ == "__main__":
    d1 = Developer("Олена", 40000, "senior")
    d2 = Developer("Андрій", 30000, "junior")
    m = Manager("Марта", 45000, [d1, d2])

    print(d1.salary(), d2.salary(), m.salary())

    dep = Department("R&D", d1, d2, m)
    print(dep.payroll(), dep.top())

    d2.give_raise()
    m.give_raise()
    print(d2.base, m.base)