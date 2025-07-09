# 📊 מערכת ניהול ותחזית נתונים

מערכת זו נועדה לקרוא קובצי CSV, לנקות את הנתונים, לאמן מודל הסתברותי פשוט ולבצע בדיקות על נתוני בדיקה.
הפרויקט כתוב ב־Python ומותאם לעבודה עם ספריית Pandas.

---

## ✨ יכולות עיקריות

* קריאת קובצי CSV והמרתם ל־DataFrame
* ניקוי נתונים (הסרת ערכים חסרים)
* חלוקה לסט אימון וסט בדיקה
* חישוב סטטיסטיקות הסתברות לפי עמודת מטרה
* בדיקת נתונים חדשים והשוואתם לקבוצות לימוד
* ניהול תהליך כולל באמצעות מחלקת Controller

---

## 🧰 דרישות מערכת

* Python 3.7+
* pandas

### התקנה

```bash
pip install pandas
```

project/
│
├── data_manage/
│   ├── dal.py               # קריאת הנתונים
│   └── cleaner.py           # ניקוי וחלוקת הנתונים
│
├── classification/
│   ├── train_a_model.py     # יצירת מודל הסתברותי
│   └── check_data.py        # בדיקת נתונים חדשים
│
├── main.py                  # Controller - ניהול תהליך מלא
└── README.md


from data_manage.dal import Dal
from data_manage.cleaner import clean_data
from classification.train_a_model import train_a_model
from classification.check_data import check_data

# קריאת הנתונים
dal = Dal()
data = dal.read_the_csv_to_df()

# ניקוי וחלוקה
cleaner = clean_data(data)
clean_data_set = cleaner.remove_none()
train_data = cleaner.cat_data()
test_data = cleaner.chaing_from_df_to_dict()

# אימון מודל
model = train_a_model(train_data)
dict_result, target_column = model.check_statistics()

# בדיקה
checker = check_data(dict_result, test_data)
results = checker.tests()

print(results)


flowchart TD
    A[טעינת קובץ CSV] --> B[ניקוי נתונים]
    B --> C[חלוקה לסט אימון ובדיקה]
    C --> D[אימון מודל הסתברותי]
    D --> E[בדיקת נתונים חדשים]
    E --> F[תוצאה סופית]
