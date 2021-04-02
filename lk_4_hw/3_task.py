import pandas as pd
import pprint

pprint.pprint(pd.date_range('2021', end='2022', freq='W-MON').strftime('%Y-%m-%d').tolist(), indent=4)