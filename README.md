# InsightChallenge
Insight Data Challenge for Data Engineer

Scripts
-----------------
Run find_political_donors.py as following:
python ./src/find_political_donors.py -i ./input/itcont.txt -oz ./output/medianvals_by_zip.txt -od ./output/medianvals_by_date.txt

or simply run run.sh

In general, script has arguments as follows:

python find_political_donors.py -i INPUT_FILE -oz OUTPUT_FILE_FOR_ZIP -od OUTPUT_FILE_FOR_DATE

Input Data
------------------
Data is taken from FEC website for 2017-2018 year and follows INDIV Data Dictionary. 
