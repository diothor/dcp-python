class DistanceConverter:

    def __init__(self, basic_unit='m'):
        self.basic_unit = basic_unit
        self.units = {self.basic_unit: 1}

    def add_unit(self, unit, conversion_to_basic):
        self.units[unit] = conversion_to_basic

    def add_mapping(self, units, values):
        known_unit, new_unit = units
        if known_unit not in self.units:
            raise ValueError('Mapping to unregistered measure unit: ' + known_unit)
        self.add_unit(new_unit, self.units[known_unit] * values[0] / values[1])

    def convert(self, from_unit, value, to_unit):
        try:
            return value if from_unit == to_unit else round(value * self.units[from_unit] / self.units[to_unit], 2)
        except KeyError:
            return None


distance_metrics = DistanceConverter()
distance_metrics.add_unit('cm', 0.01)
distance_metrics.add_unit('km', 1000)
assert distance_metrics.convert('km', 1, 'cm') == 100_000
assert distance_metrics.convert('m', 1, 'dummy') is None

distance_metrics = DistanceConverter(basic_unit='inch')
distance_metrics.add_mapping(("inch", "foot"), (12, 1))
distance_metrics.add_mapping(("foot", "yard"), (3, 1))
distance_metrics.add_mapping(("yard", "chain"), (22, 1))
assert distance_metrics.convert("inch", 24, "foot") == 2.0
assert distance_metrics.convert("inch", 36, "yard") == 1
assert distance_metrics.convert("inch", 48, "yard") == 1.33
assert distance_metrics.convert("foot", 4, "yard") == 1.33
assert distance_metrics.convert("chain", 2, "inch") == 1584.0
assert distance_metrics.convert("chain", 3, "foot") == 198.0
