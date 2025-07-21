from pathlib import Path
import os

for f in ["enrollments.csv", Path("data") / "Students_for_Internship_Review.xlsx"]:
    try:
        os.remove(f)
        print(f"Deleted {f}")
    except:
        print(f"Couldn't find {f} to delete")
