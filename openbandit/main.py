import glob
files = glob.glob('/content/staging/obd/**/*.csv', recursive=True)
files

import pandas as pd
from pathlib import Path

for f in files:
    pd.read_csv(f, index_col=[0]).to_parquet('openbandit/'+Path(f).stem+'.parquet.snappy', compression='snappy')

!git status -u

!dvc add openbandit/*.snappy
!dvc commit openbandit/*.snappy
!dvc push openbandit/*.snappy