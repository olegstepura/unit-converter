def Convert_time(from_unit, to_unit, from_value, _=None):
    if _ is None:
        # Fallback if no translation function provided
        def _(s): return s
    
    # Conversion rates to seconds (base unit)
    units_in_seconds = {
        1: 1,            # Seconds
        2: 60,           # Minutes
        3: 3600,         # Hours
        4: 86400,        # Days
        5: 604800,       # Weeks
        6: 2592000,      # Months (30 days)
        7: 31536000      # Years (365 days)
    }

    unit_names = {
        1: _("Seconds"),
        2: _("Minutes"),
        3: _("Hours"),
        4: _("Days"),
        5: _("Weeks"),
        6: _("Months"),
        7: _("Years")
    }

    if from_unit in units_in_seconds and to_unit in units_in_seconds:
        value_in_seconds = from_value * units_in_seconds[from_unit]
        result = value_in_seconds / units_in_seconds[to_unit]

        desc_result = f"{from_value} {unit_names[from_unit]} {_('is equal to')} {result} {unit_names[to_unit]}"
        short_result = f"{result}"
        return desc_result, short_result
    else:
        return _("Invalid unit selection. Please choose from the available units."), ""

