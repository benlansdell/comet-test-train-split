import pandas as pd 
import argparse 
import os

parser = argparse.ArgumentParser(description='Convert XLS to CSV')
parser.add_argument('input', help='XLS file to convert')
parser.add_argument('output', help='CSV file to create')

args = parser.parse_args(['../data/input/COMET_DATA_010322.xlsx', '../data/processed/comet_data.csv'])

def main(args):
    df = pd.DataFrame()
    xl_dict = pd.read_excel(args.input, engine='openpyxl', sheet_name = None, skiprows = 2)
    for sheet in xl_dict:
        if 'files' in sheet:
            this_sheet = xl_dict[sheet]
            this_sheet['sheet name'] = sheet
            df = pd.concat([df, this_sheet], axis = 0)

    df = df[['sheet name', 'SJID', 'Slide Scan File', 'Disease']]
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    df.to_csv(args.output, index=False)

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)