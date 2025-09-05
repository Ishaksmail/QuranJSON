import os
import re
import json

# 🔹 مجلد الإدخال والإخراج
INPUT_DIR = "data"
OUTPUT_DIR = "output"

# 🔹 تعبيرات لاكتشاف السورة والآيات
SURAH_PATTERN = re.compile(r"^سُورَةُ\s+.+$")
AYAH_PATTERN = re.compile(r"(.*?)(?:\s+([٠-٩]+))")

# 🔹 أسماء الروايات
RAWAYAT = {
    "Hafs.txt": 1,
    "Warsh.txt": 2,
    "Douri.txt": 3,
    "Qaloun.txt": 4,
    "Sousi.txt": 5,
    "Shuba.txt": 6,
}

# 🔹 تحويل الرقم العربي إلى int
def arabic_to_int(s):
    trans = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
    return int(s.translate(trans))

# 🔹 تقسيم النص إلى آيات
def split_ayahs(line):
    ayahs = []
    for match in AYAH_PATTERN.finditer(line):
        text = match.group(1).strip()
        ayah_number = arabic_to_int(match.group(2)) if match.group(2) else None
        if ayah_number is not None and text:
            ayahs.append({
                "ayah_number": ayah_number,
                "text": text
            })
    return ayahs

# 🔹 المعالجة
def process_file(filename, riwaya_id):
    with open(os.path.join(INPUT_DIR, filename), "r", encoding="utf-8") as f:
        text = f.read()

    # إزالة الأسطر الفارغة
    lines = [l.strip() for l in text.splitlines() if l.strip()]

    surahs = []
    surah_index = 0
    current_ayahs = []

    for line in lines:
        # بداية سورة
        if SURAH_PATTERN.match(line):
            if current_ayahs:
                # حفظ السورة السابقة
                surahs.append({
                    "novel": riwaya_id,
                    "surah_number": surah_index,
                    "number_of_ayahs": len(current_ayahs)
                })
                surah_file = os.path.join(OUTPUT_DIR, f"{filename[:-4]}/surah_{surah_index:03}.json")
                os.makedirs(os.path.dirname(surah_file), exist_ok=True)
                with open(surah_file, "w", encoding="utf-8") as sf:
                    json.dump({
                        "surah_number": surah_index,
                        "ayahs": current_ayahs
                    }, sf, ensure_ascii=False, indent=2)
                current_ayahs = []

            surah_index += 1
            continue

        # آيات
        ayahs_in_line = split_ayahs(line)
        current_ayahs.extend(ayahs_in_line)

    # آخر سورة
    if current_ayahs:
        surahs.append({
            "novel": riwaya_id,
            "surah_number": surah_index,
            "number_of_ayahs": len(current_ayahs)
        })
        surah_file = os.path.join(OUTPUT_DIR, f"{filename[:-4]}/surah_{surah_index:03}.json")
        os.makedirs(os.path.dirname(surah_file), exist_ok=True)
        with open(surah_file, "w", encoding="utf-8") as sf:
            json.dump({
                "surah_number": surah_index,
                "ayahs": current_ayahs
            }, sf, ensure_ascii=False, indent=2)

    # حفظ surahs.json
    os.makedirs(os.path.join(OUTPUT_DIR, filename[:-4]), exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, filename[:-4], "surahs.json"), "w", encoding="utf-8") as f:
        json.dump(surahs, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    for file, riwaya_id in RAWAYAT.items():
        print(f"⏳ معالجة {file} ...")
        process_file(file, riwaya_id)
    print("✅ تم إنشاء الملفات في output/")
