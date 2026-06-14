import os

dest_dir = r"c:\Users\Anant Chauhan\OneDrive\Documents\Anant Chauhan mains\portfolio"

mapping = {
    "cert_2.png": "ibm_data.png",
    "cert_3.png": "oneroadmap_ai.png",
    "cert_4.png": "oneroadmap_data.png",
    "cert_5.png": "internshala_selection.png",
    "cert_6.png": "cognitiveclass_python_tdd.png",
    "cert_7.png": "google_analytics.png",
    "cert_8.png": "unstop_stonks.png",
    "cert_9.png": "anthropic_claude_code.png",
    "cert_10.png": "coer_poster_contest.png",
    "cert_11.png": "cisco_cybersecurity.png",
    "cert_12.png": "csai_membership.png",
    "cert_13.png": "enginow_iq_test.png",
    "cert_14.png": "leap_reverse_engineering.png",
    "cert_15.png": "tcs_mastercraft_dataplus.png"
}

for src_name, dest_name in mapping.items():
    src_path = os.path.join(dest_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    if os.path.exists(src_path):
        if os.path.exists(dest_path):
            os.remove(dest_path)
        os.rename(src_path, dest_path)
        print(f"Renamed {src_name} to {dest_name}")
    else:
        print(f"Source file {src_name} not found")

# remove find_unique.py, check_ocr.py, dhash_compare.py, run_ocr.ps1, inspect_images.py, read_transcript.py
to_remove = ["find_unique.py", "check_ocr.py", "dhash_compare.py", "run_ocr.ps1", "inspect_images.py", "read_transcript.py", "cert_1.png"]
for f in to_remove:
    path = os.path.join(dest_dir, f)
    if os.path.exists(path):
        os.remove(path)
        print(f"Removed temporary file: {f}")
