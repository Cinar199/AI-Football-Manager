
class Player:
    def __init__(
        self,
        name,
        position,
        pac,
        sho,
        pas,
        dri,
        defending,
        phy,
        sta
    ):
        self.name = name
        self.position = position
        self.pac = pac
        self.sho = sho
        self.pas = pas
        self.dri = dri
        self.defending = defending
        self.phy = phy
        self.sta = sta

    @property
    def ovr(self):
        weights = {
            "GK": (0, 0, 0, 0, 0.6, 0.4),
            "DEF": (0.1, 0, 0.2, 0, 0.4, 0.3),
            "MID": (0.15, 0.15, 0.3, 0.2, 0.1, 0.1),
            "FWD": (0.2, 0.35, 0.15, 0.2, 0, 0.1)
        }

        values = [
            self.pac,
            self.sho,
            self.pas,
            self.dri,
            self.defending,
            self.phy
        ]

        selected = weights.get(
            self.position,
            weights["MID"]
        )

        return round(sum(
            value * weight
            for value, weight in zip(values, selected)
        ))

    def info(self):
        return {
            "name": self.name,
            "position": self.position,
            "OVR": self.ovr,
            "PAC": self.pac,
            "SHO": self.sho,
            "PAS": self.pas,
            "DRI": self.dri,
            "DEF": self.defending,
            "PHY": self.phy,
            "STA": self.sta
        }
        
