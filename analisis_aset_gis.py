from pathlib import Path
import csv, math

ROOT = Path(__file__).resolve().parents[1]
KANTOR_LAT, KANTOR_LON = -3.8000, 102.2655

def jarak_km(lat1, lon1, lat2, lon2):
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = math.radians(lat2-lat1), math.radians(lon2-lon1)
    a = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*r*math.asin(math.sqrt(a))

with (ROOT/"data"/"laporan_aset.csv").open(newline="", encoding="utf-8") as f:
    laporan = list(csv.DictReader(f))
for x in laporan:
    x["jarak_km"] = jarak_km(KANTOR_LAT, KANTOR_LON, float(x["latitude"]), float(x["longitude"]))
laporan.sort(key=lambda x: x["jarak_km"])
print("Laporan aset, dari yang terdekat:")
for x in laporan:
    print(f'{x["id_laporan"]} | {x["aset"]} | {x["jarak_km"]:.2f} km | {x["status"]}')
print("\nPrioritas pemeriksaan:")
for x in laporan:
    if x["status"] == "Perlu diperiksa":
        print(f'{x["aset"]}: {x["jarak_km"]:.2f} km')
