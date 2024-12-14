**Summary**
The program main_run.py was created in order to help logging attendance for students. The data folder is supposed to contain the OCR scans of each individual attendance sheets. The program takes one attendance sheet text file , and data.csv ( dataframe of all students) as an input and outputs missing_all_results.csv that contains name of students that have 2 or more fields missing. Additionally for further detail, comparison_results.csv tabulizes thye fields of each student and gives a true or false value bbased on whether they were found in the document. The comparison returns true with a tolerance of 0.8 ( 80 % match) and does not require an exact match to return true

**File structure :**
All OCR scanned sheets are stored as .txt in data folder, additionally a csv called data.csv is stored that has the classlist as a csv. the program outputs two files - comparison_results.csv and missing_all_results.csv.

**Some limitations :**
(1) Limitations with OCR as OCR is never 100 percent accurate.
(2) Some students have common names - even if they are absent, their names field will indicate true in these cases.
(3) if the NetIDS are a perfect match than the student is ofcourse present
(4) Take an OCR scan of a sheet first and observe carefully for bad handwriting . See if OCR recognizes this, if not make special note of these names.

**Future work :**
(1) Incorporating the fact that a match of NetId means present
(2) Tweaking tolerance vaue for optimal output
(3) Algorithm is generally slow - there should be a faster way but it works for a small dataset as in here.
