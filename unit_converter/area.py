def convert_area(from_unit, to_unit, from_value, _=None):
    if _ is None:
        def _(s): return s
    
    unit_names = {
        1: _("Square meter (m²)"),
        2: _("Square kilometer (km²)"),
        3: _("Square foot (ft²)"),
        4: _("Square yard (yd²)"),
        5: _("Acre"),
        6: _("Hectare")
    }

    # All conversions to Square Meters (base unit)
    units_in_square_meters = {
        1: 1,               # m²
        2: 1e6,             # km²
        3: 0.092903,        # ft²
        4: 0.836127,        # yd²
        5: 4046.86,         # acre
        6: 10000            # hectare
    }

    

    if from_unit in units_in_square_meters and to_unit in units_in_square_meters:
        value_in_square_meters = from_value * units_in_square_meters[from_unit]
        result = value_in_square_meters / units_in_square_meters[to_unit]

        desc_result = f"{from_value} {unit_names[from_unit]} {_('is equal to')} {result} {unit_names[to_unit]}"
        short_result = f"{result}"
        return desc_result, short_result
                
    else:
        return _("Invalid unit selection. Please choose from the available units."), ""