from module.campaign.campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger
from campaign.campaign_main.campaign_12_4_leveling import Config


MAP = CampaignMap()
MAP.shape = 'H6'
MAP.map_data = '''
    ME -- ME ME -- -- ++ ++
    ++ ME -- ++ ME ME ME ME
    ++ __ ME ++ ++ __ ME --
    -- ME -- ME ME ME -- ME
    ME ++ ++ SP SP -- ++ MB
    ME -- ME ME -- ME ++ MB
'''
#MAP.camera_data = ['D3', 'D5', 'F3', 'F5']
MAP.spawn_data = [
    {'battle': 0, 'enemy': 2},
    {'battle': 1, 'enemy': 2},
    {'battle': 2, 'enemy': 1},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 1},
    {'battle': 5},
    {'battle': 6, 'boss': 1},
]

A1, B1, C1, D1, E1, F1, G1, H1, \
A2, B2, C2, D2, E2, F2, G2, H2, \
A3, B3, C3, D3, E3, F3, G3, H3, \
A4, B4, C4, D4, E4, F4, G4, H4, \
A5, B5, C5, D5, E5, F5, G5, H5, \
A6, B6, C6, D6, E6, F6, G6, H6, \
    = MAP.flatten()

road_main = RoadGrids([F4, H4])


class Campaign(CampaignBase):
    MAP = MAP

    def battle_0(self):
        self.fleet_2_push_forward()

        if self.clear_roadblocks([road_main]):
            return True
        if self.clear_potential_roadblocks([road_main]):
            return True

        return self.battle_default()

    def battle_6(self):
        boss = self.map.select(is_boss=True)
        if boss:
            if not self.check_accessibility(boss[0], fleet=2):
                if self.clear_roadblocks([road_main]):
                    return True

        return self.fleet_2.clear_boss()