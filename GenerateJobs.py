import pandas as pd
bosses_df = pd.read_csv('Bosses1.csv')
jobs_df = pd.read_csv('Jobs.csv')

combined_df = bosses_df.merge(jobs_df, how='cross')
combined_df.to_csv('Jobs_with_bosses.csv', index=False)