ingress:
		cp data/input/AllComet_metaData_12162022.csv data/processed/comet_metadata.csv

##Out of date spreadsheet.
convert:
		python src/convert_xls_csv.py data/input/COMET_DATA_010322.xlsx data/processed/comet_metadata.csv
split:
		python src/testtrainsplit.py data/processed/comet_metadata.csv data/output/comet_metadata_split.csv --test_size 0.5 --val_size 0.0 --onlysampleswslides

valsplit:
		python src/testtrainsplit.py data/processed/comet_metadata.csv data/output/comet_metadata_trainvalsplit.csv --onlysampleswslides

crossvalsplit:
		python src/testtrainsplit_nfolds.py data/processed/comet_metadata.csv data/output/cv/comet_metadata_trainvalsplit.csv --onlysampleswslides

all: ingress split valsplit