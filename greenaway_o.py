class Film:
    def __init__(self, cim, ev):
        self.cim = cim
        self.ev = int(ev)

    def __str__(self):
        return f"Könyv címe: {self.cim}\nKiadás éve: {self.ev}"
