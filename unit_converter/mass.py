def convert_mass(from_unit, to_unit, from_value, _=None):
    if _ is None:
        def _(s): return s
    
    # Conversion rates from kilogram (base unit)
    units_in_kg = {
        1: 0.000001,     # mg to kg
        2: 0.001,        # g to kg
        3: 1,            # kg to kg
        4: 1000,         # tonne to kg
        5: 0.0283495,    # oz to kg
        6: 0.453592,     # lb to kg
        7: 6.35029       # stone to kg
    }

    unit_names = {
        1: _("Milligram (mg)"),
        2: _("Gram (g)"),
        3: _("Kilogram (kg)"),
        4: _("Metric Tonne (t)"),
        5: _("Ounce (oz)"),
        6: _("Pound (lb)"),
        7: _("Stone (st)")
    }

    if from_unit in units_in_kg and to_unit in units_in_kg:
            value_in_kg = from_value * units_in_kg[from_unit]
            result = value_in_kg / units_in_kg[to_unit]

            desc_result = f"{from_value} {unit_names[from_unit]} {_('is equal to')} {result} {unit_names[to_unit]}"
            short_result = f"{result}"
            return desc_result, short_result
    else:
        return _("Invalid unit selection. Please choose from the available units."), "" 