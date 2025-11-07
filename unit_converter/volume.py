def Convert_volume(from_unit, to_unit, from_value, _=None):
    if _ is None:
        def _(s): return s
    
    unit_names = {
        1: _("Milliliters (ml)"),
        2: _("Liters (L)"),
        3: _("Cubic centimeters (cc)"),
        4: _("Cubic meters (m³)"),
        5: _("Teaspoon (tsp)"),
        6: _("Tablespoon (tbsp)"),
        7: _("Fluid ounces (fl oz)"),
        8: _("Cups"),
        9: _("Pints"),
        10: _("Gallons")
    }

    # All conversions to Liters (base unit)
    units_in_liters = {
        1: 0.001,        # ml
        2: 1,            # L
        3: 0.001,        # cc
        4: 1000,         # m³
        5: 0.00492892,   # tsp
        6: 0.0147868,    # tbsp
        7: 0.0295735,    # fl oz
        8: 0.24,         # cups (standard metric cup)
        9: 0.473176,     # pint
        10: 3.78541      # gallon
    }

    if from_unit in units_in_liters and to_unit in units_in_liters:
        value_in_liters = from_value * units_in_liters[from_unit]
        result = value_in_liters / units_in_liters[to_unit]

        desc_result = f"{from_value} {unit_names[from_unit]} {_('is equal to')} {result} {unit_names[to_unit]}"
        short_result = f"{result}"
        return desc_result, short_result
    else:
        return _("Invalid unit selection. Please choose from the available units."), ""