

```markdown
# 📖 QuranJSON

مشروع **QuranJSON** يهدف إلى توفير نصوص القرآن الكريم في صيغة **JSON منظمة** مع دعم عدة روايات:  
**حفص، ورش، الدوري، قالون، السوسي، شعبة**.  

> ✨ تمت إزالة **البسملة** من ملفات النص (`.txt`) لتسهيل عملية تقسيم السور والآيات بدقة.

---

## 🌍 English Description

**QuranJSON** provides the Quran text in a structured **JSON format**, supporting multiple recitations:  
**Hafs, Warsh, Douri, Qaloun, Sousi, Shuba**.  

> ✨ The **Basmala** was intentionally removed from `.txt` files to simplify surah and ayah splitting.


## 📂 هيكلة المشروع | Project Structure
data/                  # ملفات الإدخال (نصوص الروايات)
│── Hafs.txt
│── Warsh.txt
│── Douri.txt
│── Qaloun.txt
│── Sousi.txt
│── Shuba.txt

output/                # ملفات الإخراج (JSON منظم)
│── Hafs/
│   │── surahs.json        # قائمة السور (رقم وعدد الآيات)
│   │── surah\_001.json     # آيات سورة الفاتحة
│   │── surah\_002.json     # آيات سورة البقرة
│   ...
│── Warsh/
│   │── surahs.json
│   │── surah\_001.json
│   ...

````

📌 **ملفات JSON المنتَجة:**
- `surahs.json` → قائمة السور (الرقم + عدد الآيات).  
- `surah_<n>.json` → نصوص الآيات للسورة المطلوبة.  


### ⚙️ كيفية الاستخدام | Usage

```bash
python process.py
````

3. ستجد ملفات JSON الجاهزة داخل مجلد `output/` لكل رواية.

---

### ✅ التحقق | Verification

* قارن عدد الآيات في كل سورة مع المصحف الشريف.
* إذا وجدت خطأ في النص أو التقسيم:

  * افتح **Issue** للتبليغ.
  * أو أرسل **Pull Request** مع التصحيح.

---

### 🤝 المساهمة | Contributing

مرحب بأي مساهمة في:

* تحسين الكود.
* إضافة روايات جديدة.
* تحسين ملفات النصوص `.txt`.

> 🔧 الهدف هو جعل المشروع مصدرًا مفتوحًا موثوقًا للنص القرآني بصيغة JSON.

---

### 📜 الترخيص | License

هذا المشروع مرخّص تحت رخصة **MIT License**.
انظر ملف [LICENSE](LICENSE) لمزيد من التفاصيل.