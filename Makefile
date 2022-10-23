convert:
		python src/convert_xls_csv.py data/input/COMET_DATA_010322.xlsx data/processed/comet_metadata.csv
split:
		python src/testtrainsplit.py data/processed/comet_metadata.csv data/output/comet_metadata_split.csv

all: convert split