import pandas as pd

data = pd.DataFrame(
    [(1, 2, 3, 4),
    (0, 3, 0, 8),
    (2, 0, 5, 0),
    (1, 1, 1, 4)], columns=['dogs', 'cats', 'bears', 'duck']
)

print(data.cov())