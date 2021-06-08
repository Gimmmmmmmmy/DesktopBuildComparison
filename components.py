import pandas as pd
NvidiaGraphicsCard = {
    "Name":["3060", "3060Ti", "3070", "3070Ti", "3080", "3080Ti", "3090"],
    "MSRP":[329.00, 399.00, 499.00, 599.00, 699.00, 1199.00, 1499.00],
    "TDP":[170, 200, 220, 290, 320, 350, 350],
    "Memory":[12, 8, 8, 8, 10, 12, 24],
    "GDDR6X":[False, False, False, True, True, True, True],
    "Passmark":[16751, 19748, 21798, 0, 24399, 25343, 25773],
    "Clock":[1777, 1665, 1730, 0, 1710, 1665, 1695]
}
AMDGraphicsCard = {
    "Name":["6700XT", "6800", "6800XT", "6900XT"],
    "MSRP":[479, 579, 649, 999],
    "TDP":[230, 250, 300, 300],
    "Memory":[12, 16, 16, 16],
    "GDDR6X":[False, False, False, False],
    "Passmark":[18713, 20759, 23556, 26082],
    "Clock":[2424, 2105, 2250, 2250]
}
AMDProcessor = {
    "Name":["5600x", "5800x", "5900x", "5950x"],
    "MSRP":[279.99, 399.99, 549.99, 836.79],
    "TDP":[65, 105, 105, 105],
    "Core":[6, 8, 12, 16],
    "Single":[599, 629, 636, 649],
    "Multi":[4569, 6046, 8545, 10435]
}
IntelProcessor = {
    "Name":["11600k", "11700k", "11900k"],
    "MSRP":[169.99, 349.99, 499.99],
    "TDP":[125, 125, 125],
    "Core":[6, 8, 8],
    "Single":[598, 612, 645],
    "Multi":[4293, 5615, 6214]
}
N_GPU = pd.DataFrame(NvidiaGraphicsCard)
A_GPU = pd.DataFrame(AMDGraphicsCard)
A_CPU = pd.DataFrame(AMDProcessor)
I_CPU = pd.DataFrame(IntelProcessor)
N_GPU.index = [60, 62, 70, 72, 80, 82, 90]
A_GPU.index = [72, 80, 82, 99]
A_CPU.index = [61, 81, 91, 96]
I_CPU.index = [60, 70, 90]
N_GPU.to_csv('NvidiaGraphicsCard.csv')
A_GPU.to_csv('AMDGraphicsCard.csv')
A_CPU.to_csv('AMDProcessor.csv')
I_CPU.to_csv('IntelProcessor.csv')