# length.py

def convert_length(from_unit, to_unit, from_value, _=None):
    if _ is None:
        # Fallback if no translation function provided
        def _(s): return s
    
    # Conversion rates from meter (base unit)
    units_in_meters = {
        "mm": 0.001,    # mm to meters
        "cm": 0.01,     # cm to meters
        "m": 1,         # m to meters
        "km": 1000,     # km to meters
        "in": 0.0254,   # in to meters
        "ft": 0.3048,   # ft to meters
        "yd": 0.9144,   # yd to meters
        "mi": 1609.34   # mi to meters
    }

    unit_names = {
        "mm": _("Millimeter (mm)"),
        "cm": _("Centimeter (cm)"),
        "m": _("Meter (m)"),
        "km": _("Kilometer (km)"),
        "in": _("Inch (in)"),
        "ft": _("Foot (ft)"),
        "yd": _("Yard (yd)"),
        "mi": _("Mile (mi)")
    }

    if from_unit in units_in_meters and to_unit in units_in_meters:
        # Convert the input value to meters
        value_in_meters = from_value * units_in_meters[from_unit]
        
        # Convert from meters to the target unit
        result = value_in_meters / units_in_meters[to_unit]

        # Return the result and unit names
        desc_result = f"{from_value} {unit_names[from_unit]} {_('is equal to')} {result} {unit_names[to_unit]}"
        short_result = f"{result}"
        return desc_result, short_result
    else:
        return _("Invalid unit selection. Please choose from the available units."), ""

