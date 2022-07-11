class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, *args):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = args if len(args) <= 4 else args[0:self.total_mem_slots]

    def get_config(self):
        config_list = []
        config_list.append(f"Материнская плата: {self.name}")
        config_list.append(f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}")
        config_list.append(f"Слотов памяти: {self.total_mem_slots}")
        mem_spec = [f'{m.name}-{m.volume}' for m in self.mem_slots]
        config_list.append(f"Память: {';'.join(mem_spec)}")
        return config_list

mb = MotherBoard("MSI", CPU(name="AMD", fr=3700), Memory(name="MSI", volume=16), Memory(name="MSI", volume=16))
print(mb.get_config())


