import pandas as pd 
import argparse 
import os
from sklearn.model_selection import StratifiedShuffleSplit

SEED = 42

parser = argparse.ArgumentParser(description='Assign slides to test or train group')
parser.add_argument('input', help='CSV file to compute test train split for')
parser.add_argument('output', help='Output csv file with test train assignments')
parser.add_argument('--test_size', type=float, default=0.5, help='Fraction of data to assign to test group')

args = parser.parse_args(['../data/processed/comet_metadata.csv', '../data/output/comet_metadata_split.csv'])

def main(args):
    df = pd.read_csv(args.input)

    df = df[~pd.isna(df['SJID'])]
    df = df[~pd.isna(df['Disease'])]
    if 'SheetName' in df.columns:
        df = df[~pd.isna(df['SheetName'])]
        df['Slide Scan File'] = df['Slide.Scan.File']
        df = df[['SheetName', 'SJID', 'Slide Scan File', 'Disease']]
        df['disease_sheet_name'] = df['SheetName'].apply(lambda x: x.split(' ')[0])
        df = df.drop(columns = 'SheetName')
        df['Slide Scan File'] = df['Slide Scan File'].apply(lambda x: str(int(x)) if not pd.isna(x) else x)
    else:
        df['disease_sheet_name'] = df['sheet name'].apply(lambda x: x.split(' ')[0])
    df['test'] = False

    splitter = StratifiedShuffleSplit(n_splits=1, test_size=args.test_size, random_state=SEED)
    for train_index, test_index in splitter.split(df, df['disease_sheet_name']):
        df.iloc[test_index.astype(int), -1] = True

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    df.to_csv(args.output, index=False)

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)