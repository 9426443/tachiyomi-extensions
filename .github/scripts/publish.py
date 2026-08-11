import gzip
import html
import json
import os
import shutil
from pathlib import Path

from google.protobuf import json_format

import index_pb2

ROOT = Path(__file__).resolve().parents[2]
EXT_DIR = ROOT / "src" / "zh" / "roumanwu"
INFO_FILE = EXT_DIR / "build" / "keiyoushi-source-info.json"

PUBLIC = ROOT / "public"
APK_DIR = PUBLIC / "apk"
JAR_DIR = PUBLIC / "jar"
ICON_DIR = PUBLIC / "icons"
for d in (APK_DIR, JAR_DIR, ICON_DIR):
    d.mkdir(parents=True, exist_ok=True)

info = json.loads(INFO_FILE.read_text(encoding="utf-8"))
apk = next((EXT_DIR / "build" / "outputs" / "apk" / "release").glob("*.apk"))
jar = next((EXT_DIR / "build" / "outputs" / "jar" / "release").glob("*.jar"))
icon = EXT_DIR / "res" / "mipmap-xhdpi" / "ic_launcher.png"

shutil.copy2(apk, APK_DIR / apk.name)
shutil.copy2(jar, JAR_DIR / jar.name)
shutil.copy2(icon, ICON_DIR / "ic_launcher.png")

repo_url = os.environ["REPO_URL"].rstrip("/")
signing_key = os.environ["SIGNING_KEY"].strip()

ext = index_pb2.Extension(
    name=info["name"],
    packageName=info["packageName"],
    resources=index_pb2.Resources(
        apkUrl=f"{repo_url}/apk/{apk.name}",
        jarUrl=f"{repo_url}/jar/{jar.name}",
        iconUrl=f"{repo_url}/icons/ic_launcher.png",
    ),
    extensionLib=info["extensionLib"],
    versionCode=info["versionCode"],
    versionName=info["versionName"],
    contentWarning=info["contentWarning"],
    sources=[
        index_pb2.Source(
            id=int(source["id"]),
            name=source["name"],
            language=source["lang"],
            homeUrl=source["baseUrl"],
            mirrorUrls=source.get("mirrorUrls", []),
        )
        for source in info["sources"]
    ],
)

index = index_pb2.Index(
    name="Roumanwu",
    badgeLabel="RM",
    signingKey=signing_key,
    contact=index_pb2.Contact(website=repo_url),
    extensionList=index_pb2.ExtensionList(extensions=[ext]),
)

(PUBLIC / "index.json").write_text(
    json_format.MessageToJson(
        index,
        always_print_fields_with_no_presence=False,
        preserving_proto_field_name=True,
    ),
    encoding="utf-8",
)
(PUBLIC / "index.pb").write_bytes(gzip.compress(index.SerializeToString(deterministic=True)))

with (PUBLIC / "index.html").open("w", encoding="utf-8") as f:
    f.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>apks</title>\n</head>\n<body>\n<pre>\n')
    f.write(f'<a href="{html.escape(ext.resources.apkUrl)}">Tachiyomi: {html.escape(ext.name)}</a>\n')
    f.write("</pre>\n</body>\n</html>\n")

print(f"published: {ext.name} v{ext.versionName} ({len(index_pb2.Index.SerializeToString(index))} bytes index)")
