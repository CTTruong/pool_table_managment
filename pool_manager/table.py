_PoolTableProto = {
        'number': 0,
        'occupied': False,
        'start_time': 0,    # 0 if not occupied, datetime string otherwise
        'end_time': 0,      # 0 if not occupied or the game is in progress, datetime string otherwise
        'cost': 0           # 0 if not occupied or the game is in progress, a number otherwise
        }

class PoolTable():
    # A class for accessing the table data

    # The rate is $30 per hour, one cent is 0.01
    service_charge = 30

    def __init__(self, data = _PoolTableProto):
        # A bit dirty but effective solution, no attributes should be missing
        for key in _PoolTableProto:
            setattr(self, key, _PoolTableProto[key])

        if data != _PoolTableProto:
            for key in data:
                setattr(self, key, data[key])


