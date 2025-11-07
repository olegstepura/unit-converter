def Convert_energy(from_unit,to_unit,from_value, _=None):
    if _ is None:
        def _(s): return s
    
    unit_names = {
        1: _("Joules (J)"),
        2: _("Kilojoules (kJ)"),
        3: _("Calories (cal)"),
        4: _("Kilocalories (kcal)"),
        5: _("Watt-hour (Wh)"),
        6: _("Kilowatt-hour (kWh)")
    }

    # Conversion rates to Joules (base unit)
    units_in_joules = {
        1: 1,                        # Joules to Joules
        2: 1000,                     # Kilojoules to Joules
        3: 4.184,                    # Calories to Joules
        4: 4184,                     # Kilocalories to Joules
        5: 3600,                     # Watt-hour to Joules (1 Wh = 3600 J)
        6: 3600000                  # Kilowatt-hour to Joules (1 kWh = 3600000 J)
    }


 

    if from_unit in units_in_joules and to_unit in units_in_joules:
        value_in_joules = from_value * units_in_joules[from_unit]
        result = value_in_joules / units_in_joules[to_unit]

        desc_result = f"{from_value} {unit_names[from_unit]} {_('is equal to')} {result} {unit_names[to_unit]}"
        short_result = f"{result}"
        return desc_result, short_result
                
    else:
         return _("Invalid unit selection. Please choose from the available units."), ""