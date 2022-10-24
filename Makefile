ingress:
		cp data/input/AllComet_metaData_slideFile_102222.csv data/processed/comet_metadata.csv

##Out of date spreadsheet.
convert:
		python src/convert_xls_csv.py data/input/COMET_DATA_010322.xlsx data/processed/comet_metadata.csv
split:
		python src/testtrainsplit.py data/processed/comet_metadata.csv data/output/comet_metadata_split.csv

all: ingress split