import math
class SampleClassStat():
    def sampleReturnFunction():
        return "Hello World!"

    def hpReturn(basehp,iv,ev,lvl):
        return ((((2 * basehp + iv + (ev / 4)) * lvl) / 100) + lvl + 10)

    def attackReturn(baseatk,iv,ev,lvl,atknat):
        return math.trunc((((((2 * baseatk + iv + (ev / 4)) * lvl) / 100) + 5) * atknat))
        
    def defenseReturn(basedef,iv,ev,lvl,defnat):
        return math.trunc((((((2 * basedef + iv + (ev / 4)) * lvl) / 100) + 5) * defnat))

    def spattackReturn(basespatk,iv,ev,lvl,spatknat):
        return math.trunc((((((2 * basespatk + iv + (ev / 4)) * lvl) / 100) + 5) * spatknat))  

    def spdefenseReturn(basespdef,iv,ev,lvl,spdefnat):
        return math.trunc((((((2 * basespdef + iv + (ev / 4)) * lvl) / 100) + 5) * spdefnat))

    def speedReturn(basespd,iv,ev,lvl,spdnat):
        return math.trunc((((((2 * basespd + iv + (ev / 4)) * lvl) / 100) + 5) * spdnat))  

    def sampleFunctionWithoutReturn():
        print("Stat")
